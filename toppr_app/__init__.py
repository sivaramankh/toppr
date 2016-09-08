from flask import Flask

app = Flask(__name__)

app.secret_key = 'development key'

#MongoDB Settings. Change this when deploying locally.
MONGODB_HOST = 'mongodb://localhost:28017/'
MONGODB_DB = 'got_battles'
MONGODB_COL = 'battle_col'

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .api import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')
