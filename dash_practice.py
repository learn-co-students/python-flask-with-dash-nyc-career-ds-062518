import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

app.layout=html.Div(children=[
    html.H2('Hello'),
    html.H2('World'),
    dcc.Graph( id = "our graph",
        figure= {
        'data' : [{'x' : ['bart', 'lisa', 'homer', 'marge'], 'y': [8,11,35, 30], "type": 'bar'}],
        'layout':{
            'title' : "our first graph"
                }
        }
    ),
    dcc.Graph( id = "another graph",
        figure ={
        'data' : [],
        'layout':{
            'title' : "Would you look at that an empty graph"
        }
        }
    )




])

app.run_server(debug=True)



# import Flask
from flask import Flask, request, render_template
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate
import pbd
import dash
import dash_html_components as html


# initialize new flask app
server = Flask(__name__)
# add configurations and database
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.SQLAlchemy(server)
migrate = Migrate(server, db)

app = dash.Dash(__name__, server = server, url_base_pathname='/dashboard')

app.layout = html.Div("some words") #send it to a package dashboard and then import it by:
                                    #    from package.dahsboard import *



app.run_server(debug = True)

#pretend this is our package
import dash_html_components as html
import dash_core_components as dcc
from package import app #our dash from before
from package.routes import customer_orders


customer_orders_trace = customer_orders()

app.layout = html.Div(children = [
    dcc.Graph( id = "Simpson graph",
        figure ={
        'data' : [customer_orders_trace ],
        'layout':{
            'title' : "Simpson kids"
        }
        }
    )]



#routes to get the data to view
@server

def customer_orders():
    cust = Customer.query.all()
    customer_names = [customer.name for customer in cust]

    orders_per_customer = [customer.orders.count() for customer in cust]
    return {'x' : customer_names , 'y': orders_per_customer, 'name': "num of orders", "type": 'bar' }
