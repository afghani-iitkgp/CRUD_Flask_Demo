"""
Imports all necessary packages
"""

# importing app level modules
from flask import Flask
import flask_compress
from flask_cors import CORS
# from blueprints import api

from Scripts.main import app #Importing a variable...
from Utility import utility_file

## Declaring APP::
mr_app = Flask(__name__)

## Compressing the Response (Archiving)::
flask_compress.Compress(mr_app)

# ## Connecting all services (for Multiple API services)::
mr_app.register_blueprint(app)

CORS(mr_app, resources={r"/*": {"origins": "*"}})



if __name__ == '__main__':
    mr_app.run(host=utility_file.config["settings"]["ip"], port=utility_file.config["settings"]["port"], debug=True, threaded=True, use_reloader=False)