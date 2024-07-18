from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException
import requests
from db_connection import save_to_db, create_table
from models import WhoisResponse
from parser import parse_whois_html
from whois import create_data

app = FastAPI()
create_table()


@app.get("/lookup_whois", response_model=WhoisResponse)
async def lookup_whois(domain_name: str):
    whois_url = f'https://ps.kz/domains/whois/result?q={domain_name}'

    try:
        response = requests.get(whois_url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Ошибка сбора данных")

    soup = BeautifulSoup(response.text, 'html.parser')
    data = parse_whois_html(soup)

    whois_data = create_data(domain_name, data)

    # Проверки на соответствия необходимому типу данных
    if not isinstance(whois_data["expiration_date"], str):
        whois_data["expiration_date"] = "Отсутствует"

    if not isinstance(whois_data["status"], list):
        whois_data["status"] = []

    if not isinstance(whois_data['nameservers'], list):
        whois_data['nameservers'] = []

    save_to_db(whois_data)

    return whois_data
