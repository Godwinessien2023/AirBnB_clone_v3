#!/usr/bin/python3
"""
create new flask app: register blueprint
app_views to flask instance
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_engine(exception):
    """
    
    """
    storage.close()

@app.errohandler(404)
def not_found(error):
    """
    
    """
    response = {"error": "Not found"}
    return jasonify(response), 404

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT,  threaded=True)
