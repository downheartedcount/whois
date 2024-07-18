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
   git clone git@github.com:downheartedcount/whois.git 
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
  "registrant_id": "HOST-0000",
  "registrant_name": "Host",
  "organization": "Фамилия Имя",
  "address": "Адрес",
  "city": "Алматы",
  "region": "-",
  "country": "Казахстан",
  "phone": "+774700000",
  "email": "host@host.kz",
  "registrar": "HOST.KZ",
  "nameservers": ["ns1.host.kz", "ns2.host.kz"],
  "expiration_date": "N/A"
}
```
