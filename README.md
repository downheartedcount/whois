# WHOIS Data Scraping Service

## Описание

Веб-сервис, разработанный на FastAPI выполняет запросы к 
ps.kz WHOIS сервису для получения 
информации о доменах и сохраняет эти 
данные в базу данных SQLite.

## Функционал

- Запрос данных WHOIS по доменному имени.
- Парсинг HTML-ответа и извлечение необходимых данных.
- Возвращение данных в формате JSON.
- Сохранение данных в базу данных SQLite.

## Установка

### 1. Клонирование репозитория

   ```bash
   git clone 
   cd whois_service

python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt

uvicorn app.main:app --reload
```
Теперь приложение будет доступно по адресу http://127.0.0.1:8000.

## Использование

Запрос данных

Для получения информации о домене отправьте GET-запрос на /lookup_whois с параметром domain_name.

Пример запроса:

GET http://127.0.0.1:8000/lookup_whois?domain_name=example.com
```json
{
  "domain_name": "example.com",
  "status": ["clientDeleteProhibited", "clientTransferProhibited"],
  "registrant_id": "HOSTERKZ-472283",
  "registrant_name": "Hostmaster",
  "organization": "Бигали Алишер",
  "address": "Комиссарова 45Г",
  "city": "Караганда",
  "region": "-",
  "country": "Казахстан",
  "phone": "+77470949284",
  "email": "hostmaster@hoster.kz",
  "registrar": "HOSTER.KZ",
  "nameservers": ["ns1.hoster.kz (185.116.195.38)", "ns2.hoster.kz (185.121.81.104)"],
  "expiration_date": "N/A"
}
```
