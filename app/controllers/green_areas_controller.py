from config import Config
from flask import jsonify
import requests

class GreenAreasController():
    @classmethod
    def get_green_areas(cls):
        entry = []
        kobo_data = requests.get(
            f'https://kc.kobotoolbox.org/api/v1/data/{Config.FORM_ID}', headers=Config.HEADER
        )
        api = kobo_data.json()
        for data in api:
            new_entry = {
                "nombre": data["Nombre"],
                "tipo": data["Tipo"],
                "calle": data["Calle"],
                "ordenanza": data["Ordenanza"],
                "tiene_juegos": data["_Tiene_juegos_infantiles"],
                "tiene_bancos": data["_Tiene_bancos"]
            }
            entry.append(new_entry)
        return jsonify(entry), 200