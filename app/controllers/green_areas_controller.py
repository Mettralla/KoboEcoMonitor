from config import Config
from flask import jsonify, render_template
import requests

class GreenAreasController():
    @classmethod
    def get_green_areas(cls):
        greenZone = []
        kobo_data = requests.get(
            f'https://kc.kobotoolbox.org/api/v1/data/{Config.FORM_ID}', headers=Config.HEADER
        )
        api = kobo_data.json()
        for data in api:
            new_entry = {
                "id": data["_id"],
                "nombre": data["Nombre"],
                "tipo": data["Tipo"],
                "calle": data["Calle"],
                "ordenanza": data["Ordenanza"],
                "tiene_juegos": data["_Tiene_juegos_infantiles"],
                "tiene_bancos": data["_Tiene_bancos"]
            }
            greenZone.append(new_entry)
        
        return render_template("green_areas/index.html", items=greenZone)
        # return jsonify(entry), 200

    @classmethod
    def create_green_areas(cls):
        return render_template("green_areas/index.html")