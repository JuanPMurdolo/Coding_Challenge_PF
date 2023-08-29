import os
from flask import Flask,request
from flask_smorest import Api, Blueprint, abort

def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "PF Coding Challenge"
    app.config["API_VERSION"] = "v0.1"
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    
    api = Api(app)

    

    return app
