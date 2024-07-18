def create_data(domain_name, data):
    return {
        "domain_name": domain_name,
        "status": data.get("status", []),
        "registrant_id": data.get("registrant_id", "Отсутствует"),
        "registrant_name": data.get("registrant_name", "Отсутствует"),
        "organization": data.get("organization", "Отсутствует"),
        "address": data.get("address", "Отсутствует"),
        "city": data.get("city", "Отсутствует"),
        "region": data.get("region", "Отсутствует"),
        "country": data.get("country", "Отсутствует"),
        "phone": data.get("phone", "Отсутствует"),
        "email": data.get("email", "Отсутствует"),
        "registrar": data.get("registrar", "Отсутствует"),
        "nameservers": data.get("nameservers", []),
        "expiration_date": data.get("expiration_date", "Отсутствует")
    }
