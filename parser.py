import logging
import re

#логирование для проверки целостности данных
logging.basicConfig(level=logging.INFO)

def parse_whois_html(soup):
    data = {}
    if (registrant_label := soup.find(text="Регистрант:")) and (registrant_td := registrant_label.find_next("td")):
        registrant_info = registrant_td.get_text(separator="").strip()
        parse_registrant_data(data, registrant_info)

    status_td = soup.find(text="Статус:").find_next("td") if soup.find(text="Статус:") else None
    if status_td:
        data["status"] = [ns.text.strip() for ns in status_td.find_all("b")]
            logging.info(f"Status: {data['status']}")

    registrar = soup.find(text="Регистратор:")
    if registrar:
        data["registrar"] = registrar.find_next().text.strip()
        logging.info(f"Registrar: {data['registrar']}")

    nameservers_td = soup.find(text="Серверы имен:").find_next("td") if soup.find(text="Серверы имен:") else None
    if nameservers_td:
        ns_text = nameservers_td.get_text(separator="\n").strip()
        data["nameservers"] = parse_nameservers(ns_text)

            logging.info(f"Nameservers: {data['nameservers']}")

    expiration_date = soup.find(text="Дата окончания:")
    if expiration_date:
        data["expiration_date"] = expiration_date.find_next().text.strip()
        logging.info(f"Expiration Date: {data['expiration_date']}")

    return data

def parse_nameservers(ns_text):
    nameservers = []
    #регулярка для проверки ip адресов после наименования
    pattern = re.compile(r"(\S+)\s+\(([^)]+)\)")
    matches = pattern.findall(ns_text)
    if matches:
        for match in matches:
            nameservers.append(f"{match[0]} ({match[1]})")
    else:
        nameservers = [ns.strip() for ns in ns_text.split("\n") if ns.strip()]
    return nameservers


def parse_registrant_data(data, registrant_info):
    # Словарь для сопоставления ключей с полями данных
    key_mapping = {
        "ID Контакта": "registrant_id",
        "Имя": "registrant_name",
        "Организация": "organization",
        "Адрес": "address",
        "Город": "city",
        "Область": "region",
        "Страна": "country",
        "Телефон": "phone",
        "Email": "email"
    }

    lines = registrant_info.strip().split("\n")
    for line in lines:
        parts = line.split(":", 1)
        if len(parts) == 2:
            key = parts[0].strip()
            value = re.sub(r'<.*?>', '', parts[1].strip())

            if key in key_mapping:
                data[key_mapping[key]] = value
            else:
                print(f"Неизвестное поле: {key}")

    return data
