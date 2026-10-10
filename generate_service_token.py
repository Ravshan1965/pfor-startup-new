from __future__ import annotations

from datetime import datetime, timedelta
import os

import jwt


SECRET_KEY = os.getenv("SECRET_KEY", "change_this_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
DAYS = int(os.getenv("SERVICE_TOKEN_DAYS", "3650"))


if __name__ == "__main__":
    payload = {
        "sub": "service_account_ollama",
        "role": "admin",
        "exp": datetime.utcnow() + timedelta(days=DAYS),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(f"SERVICE_BACKEND_TOKEN={token}")
