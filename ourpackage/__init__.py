# import Flask
# import Flask
from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# import Dash framework
import dash

# initialize new Flask app
server = Flask(__name__)
# add configurations and database
server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# connect flask_sqlalchemy to the configured flask app
db = SQLAlchemy(server)

#create new Dash app and use existing Flask app as our Dash app's server
app = dash.Dash(__name__, server=server)

#import our routes after our database has been configured
from ourpackage import routes
