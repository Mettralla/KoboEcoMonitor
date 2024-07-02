from flask import Blueprint
from ..controllers.green_areas_controller import GreenAreasController

green_areas = Blueprint("green_area_bp", __name__)

green_areas.route("", methods=["GET"], endpoint="get_green_zones")(GreenAreasController.get_green_areas)
green_areas.route("/new", methods=["GET"], endpoint="new_green_zones")(GreenAreasController.new_green_areas)
green_areas.route("/create", methods=["POST"], endpoint="create_green_zones")(GreenAreasController.create_green_areas)
green_areas.route("/edit/<int:id>", methods=["GET"], endpoint="edit_green_zones")(GreenAreasController.edit_green_areas)
green_areas.route("/update/<string:id>", methods=["POST"], endpoint="update_green_zones")(GreenAreasController.update_green_areas)
green_areas.route("/delete/<string:id>", methods=["DELETE"], endpoint="delete_green_zones")(GreenAreasController.delete_green_areas)
