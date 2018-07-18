# import Flask
from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import dash


# initialize new flask app
server = Flask(__name__)
# add configurations and database
server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(server)

app = dash.Dash(__name__, server=server)


from ourpackage import routes
