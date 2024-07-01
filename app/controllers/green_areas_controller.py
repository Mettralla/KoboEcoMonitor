from config import Config
from flask import jsonify, render_template, request, url_for, redirect
import requests
from datetime import datetime

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
                "tiene_juegos": data["_Tiene_juegos_infantiles"].lower(),
                "tiene_bancos": data["_Tiene_bancos"].lower()
            }
            greenZone.append(new_entry)
        
        return render_template("green_areas/index.html", items=greenZone)
        # return jsonify(entry), 200
        
    @classmethod
    def new_green_areas(cls):
        return render_template("green_areas/new.html")

    @classmethod
    def create_green_areas(cls):
        nombre = request.form.get('nombre')
        tipo = request.form.get('tipo')
        calle = request.form.get('calle')
        ordenanza = request.form.get('ordenanza')
        tiene_juegos = request.form.get('juegos')
        tiene_bancos = request.form.get('bancos')
        
        new_green_area = {
            "id": Config.PROJECT_UID,
            "submission": {
                "formhub/uuid": Config.UUID,
                "start": datetime.now().isoformat(),
                "end": datetime.now().isoformat(),
                "Nombre":nombre,
                "Tipo": tipo,
                "Calle": calle,
                "Ordenanza": ordenanza,
                "_Tiene_juegos_infantiles": tiene_juegos,
                "_Tiene_bancos": tiene_bancos,
            }
        }
        
        try:
            response = requests.post("https://kc.kobotoolbox.org/api/v1/submissions", json=new_green_area, headers=Config.HEADER)
            if response.status_code == 201:
                return redirect(url_for('green_area_bp.get_green_zones'))
            else:
                return jsonify({'error': 'Failed to submit data.'}), response.status_code
        except requests.exceptions.RequestException as e:
            return jsonify({'error': str(e)}), 500