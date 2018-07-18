# import Flask
from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import dash


# initialize new flask app
server = Flask(__name__)
# add configurations and database
server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SQLALCHEMY_ECHO'] = True

# connect flask_sqlalchemy to the configured flask app and create the Dash app
db = SQLAlchemy(server)

#creat new Dash app and use existing Flask app as our dashh app's server
app = dash.Dash(__name__, server=server, url_base_pathname = '/dashboard')  #why need to do name again if it uses flask app

#import our routes after our database has been configured
from ourpackage import routes
