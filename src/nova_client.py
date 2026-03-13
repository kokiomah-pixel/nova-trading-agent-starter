import os
import requests

API_URL = os.getenv("NOVA_API_URL", "https://api.novaos.ai")
API_KEY = os.getenv("NOVA_API_KEY", "")

def get_context(asset: str, intent: str, size: int):
    headers = {}

    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"

    response = requests.get(
        f"{API_URL}/v1/context",
        params={
            "asset": asset,
            "intent": intent,
            "size": size
        },
        headers=headers,
        timeout=10
    )

    response.raise_for_status()
    return response.json()
