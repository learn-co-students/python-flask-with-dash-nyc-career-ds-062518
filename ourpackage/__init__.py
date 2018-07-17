# import Flask
from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import dash


# initialize new flask app
server = Flask(__name__) #need to make Flask app the server and embed it within our Dash app
# add configurations and database
server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect flask_sqlalchemy to the configured flask app and create the Dash app
db = SQLAlchemy(server)
app = dash.Dash(__name__,server = server, url_base_pathname = '/dashboard') # we did not need the server arugment in the last lab
#if we did not have a flask server set up Dash would have created a Flask server for us like the last lab
#server is an attribute of the Flask app, this is why we embed Flask into Dash
#we can call server by either setting it to a variable server like above
#or we can say app.server


#import our routes after our database has been configured
from ourpackage import routes
