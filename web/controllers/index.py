# project
from web.controllers import percent_controller


def register_routes(app):
    app.include_router(percent_controller.router)
