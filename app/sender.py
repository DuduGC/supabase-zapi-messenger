import requests

from app.config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN,
    ZAPI_SECURITY_TOKEN
)


def send_message(phone, name):

    url = (
        f"https://api.z-api.io/"
        f"instances/{ZAPI_INSTANCE_ID}"
        f"/token/{ZAPI_TOKEN}"
        f"/send-text"
    )

    payload = {
        "phone": phone,
        "message":
        f"Olá, {name} tudo bem com você?"
    }

    headers = {
        "Content-Type": "application/json",
        "Client-Token":
        ZAPI_SECURITY_TOKEN
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.status_code