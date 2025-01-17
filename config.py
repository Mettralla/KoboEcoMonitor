from decouple import config

class Config:
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    AUTH_TOKEN = config("API_KEY")
    FORM_ID = config("FORM_ID")
    PROJECT_UID = config("FORM_ID_STRING")
    UUID = config("UUID")
    HEADER = {
        "Authorization": AUTH_TOKEN
    }

    APP_NAME = "KOBO ECOMONITOR"
    APP_VER = "1.0.0"