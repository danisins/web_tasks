import os

config = {
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "MAX_CONTENT_LENGTH": 1024 * 1024,
    "FLAG": "ACTF{1_L0v3_P1CkL3}"
}
