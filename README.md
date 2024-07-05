<h3 align="center">Kobo EcoMonitor</h3>

---

 KoboEcoMonitor es un sistema de monitoreo de zonas verdes que utiliza encuestas realizadas a través de KoboToolbox. Este proyecto integra KoboToolbox con Flask para recopilar, procesar y visualizar datos sobre la condición y características de áreas verdes urbanas. 

---

## 📝 Tabla de Contenidos
- [Estructura del Proyecto](#project_structure)
- [Instalación/Ejecucion](#getting_started)
- [KOBO API - Endpoints usados](#api)
<!-- - [Autores](#authors) -->

### Estructura:

    .
    ├── app/         
    │   ├── controllers/                             
    │   │   ├── __init__.py
    │   │   └── green_areas_controller.py                
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   └── green_areas.py
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   └── green_areas.py
    │   ├── static/
    │   │   ├── __init__.py
    │   │   ├── muniISO.svg
    │   │   └── favicon.png
    │   └── templates/
    │       ├── green_areas/
    │       │   ├── edit.html
    │       │   ├── index.html
    │       │   └── new.html
    │       ├── layout/
    │       │   └── base.html
    │       └── __init__.py
    ├── test/
    ├── .gitignore                   
    ├── README.md                    
    ├── config.py 
    ├── requirements.txt             
    ├── .env                         
    └── run.py

## 🏁 Instalación/Ejecución <a name = "getting_started"></a>

Clonar el repositorio backend

```bash
git clone clone https://github.com/Mettralla/KoboEcoMonitor.git
```

Ir al directorio del proyecto

```bash
cd KoboEcoMonitor
```

Crear entorno virtual

```bash
python -m venv env
```

Activar entorno

```bash
source env/Scripts/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Cambiar el nombre del archivo `.env.example` a `.env` e ingresar credenciales solicitadas

```bash
# ./.env
API_KEY = "[API KEY]"
FORM_ID = "[FORM_ID]"
FORM_ID_STRING = "[FORM_ID_STRING]"
UUID = "[UUID]"
```

Iniciar App

```bash
python run.py
```

Ingresar a la web

```bash
http://127.0.0.1:5000/green_areas
```
## KOBO API - Endpoints Usados <a name = "api"></a>

### Obtener Zonas Verdes

**URL:** `https://kc.kobotoolbox.org/api/v1/data/{FORM_ID}`

**Método:** `GET`

**Descripción:** Obtiene una lista de todas las zonas verdes registradas.

**Respuesta Exitosa:**

- **Código:** `200 OK`
- **Cuerpo:**

```json
[
	{
		"_id": 349048510,
		"formhub/uuid": "{UUID}",
		"start": "2024-06-13T16:05:28.442-03:00",
		"end": "2024-06-13T16:09:31.088-03:00",
		"Nombre": "GLORIAS DEL AUTOMOVILISMO ARGENTINO",
		"Tipo": "plaza_barrial",
		"Calle": "TADEO TADIA",
		"Ordenanza": "3982/84",
		"_Tiene_juegos_infantiles": "si",
		"_Tiene_bancos": "si",
		"__version__": "{VERSION}",
		"meta/instanceID": "{INSTANCEID}",
		"_xform_id_string": "{FORM_ID_STRING}",
		"_uuid": "{_UUID}",
		"_attachments": [],
		"_status": "submitted_via_web",
		"_geolocation": [
			null,
			null
		],
		"_submission_time": "2024-06-13T19:10:01",
		"_tags": [],
		"_notes": [],
		"_validation_status": {},
		"_submitted_by": "daniel_tejerina"
	}, {...}, {...}
]
```

### Crear Zona Verde

**URL:** `https://kc.kobotoolbox.org/api/v1/submissions`

**Método:** `POST`

**Descripción:** Crea una nueva zona verde.

**Parámetros del Cuerpo:**

- **Código:** `201 CREATED`

**Parámetros del Cuerpo:**

- **nombre** (string): Nombre de la zona verde.
- **tipo** (string): Tipo de la zona verde.
- **calle** (string): Calle donde se encuentra la zona verde.
- **ordenanza** (string): Ordenanza relacionada con la zona verde.
- **tiene_juegos** (string): Indica si tiene juegos infantiles (`si` o `no`).
- **tiene_bancos** (string): Indica si tiene bancos (`si` o `no`).

**Ejemplo de Cuerpo de Solicitud:**

```json
{
	"id": "{FORM_ID_STRING}",
	"submission": {
		"formhub/uuid": "{UUID}",
		"start": "2024-06-13T16:05:28.442-03:00",
        "end": "2024-06-13T16:09:31.088-03:00",
		"Nombre": "Plaza de los Héroes",
		"Tipo": "Plaza Barrial",
		"Calle": "Av. Siempre Viva 123",
		"Ordenanza": "4567/74",
		"_Tiene_juegos_infantiles": "si",
		"_Tiene_bancos": "no",
	}
}
```

**Respuesta:**

```json
{
	"message": "Successful submission.",
	"formid": "{FORM_ID_STRING}",
	"encrypted": false,
	"instanceID": "{INSTANCEID}",
	"submissionDate": "2024-06-30T21:34:20.231994+00:00",
	"markedAsCompleteDate": "2024-06-30T21:34:20.232008+00:00"
}
```

### Obtener Zona Verde Especifica

**URL:** `https://kc.kobotoolbox.org/api/v1/data/{FORM_ID}/{_ID}`

**Método:** `GET`

**Descripción:** Obtiene una sola zona verde por ID.

**Respuesta Exitosa:**

- **Código:** `200 OK`
- **Cuerpo:**

```json
[
	{
		"_id": 349048510,
		"formhub/uuid": "{UUID}",
		"start": "2024-06-13T16:05:28.442-03:00",
		"end": "2024-06-13T16:09:31.088-03:00",
		"Nombre": "GLORIAS DEL AUTOMOVILISMO ARGENTINO",
		"Tipo": "plaza_barrial",
		"Calle": "TADEO TADIA",
		"Ordenanza": "3982/84",
		"_Tiene_juegos_infantiles": "si",
		"_Tiene_bancos": "si",
		"__version__": "{VERSION}",
		"meta/instanceID": "{INSTANCEID}",
		"_xform_id_string": "{FORM_ID_STRING}",
		"_uuid": "{_UUID}",
		"_attachments": [],
		"_status": "submitted_via_web",
		"_geolocation": [
			null,
			null
		],
		"_submission_time": "2024-06-13T19:10:01",
		"_tags": [],
		"_notes": [],
		"_validation_status": {},
		"_submitted_by": "daniel_tejerina"
	}, {...}, {...}
]
```

### Editar Zona Verde

**URL:** `https://kf.kobotoolbox.org/api/v2/assets/{FORM_ID_STRING}/data/bulk/`

**Método:** `PATCH`

**Descripción:** Editar zona verde.

**Parámetros del Cuerpo:**

- **Código:** `200 OK`

**Parámetros del Cuerpo:**

- **nombre** (string): Nombre de la zona verde.
- **tipo** (string): Tipo de la zona verde.
- **calle** (string): Calle donde se encuentra la zona verde.
- **ordenanza** (string): Ordenanza relacionada con la zona verde.
- **tiene_juegos** (string): Indica si tiene juegos infantiles (`si` o `no`).
- **tiene_bancos** (string): Indica si tiene bancos (`si` o `no`).

**Ejemplo de Cuerpo de Solicitud:**

```json
{
	"payload": {
		"submission_ids": ["{_ID}"],
		"data": {
			"Nombre": "VIEJAS GLORIAS DEL AUTOMOVILISMO ARGENTINO"
		}
	}
}
```

**Respuesta:**

```json
{
	"count": 1,
	"successes": 1,
	"failures": 0,
	"results": [
		{
			"uuid": "{UUID}",
			"status_code": 201,
			"message": "Something went wrong"
		}
	]
}
```

### Eliminar Zona Verde

**URL:** `https://kc.kobotoolbox.org/api/v1/data/{FORM_ID}/{_ID}`

**Método:** `DELETE`

**Descripción:** Eliminar zona verde.

**Parámetros del Cuerpo:**

- **Código:** `204 NO RESULT`


<!-- ## ✍️ Autores <a name = "authors"></a> -->