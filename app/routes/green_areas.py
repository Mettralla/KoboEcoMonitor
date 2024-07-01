from flask import Blueprint
from ..controllers.green_areas_controller import GreenAreasController

green_areas = Blueprint("green_area_bp", __name__)

green_areas.route("", methods=["GET"])(GreenAreasController.get_green_areas)