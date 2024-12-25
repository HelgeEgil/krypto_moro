from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from callbacks import *
from flask import Flask
from flask.logging import default_handler
import logging

logging.basicConfig(filename="app.log", 
			filemode='a', 
			format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    	datefmt='%Y-%m-%d %H:%M:%S',
                    	level=logging.INFO)

server = Flask(__name__)

app = Dash(
	server=server, 
	external_stylesheets=[
		dbc.themes.FLATLY, 
		dbc.icons.FONT_AWESOME
	], 
	suppress_callback_exceptions=True,  
	url_base_pathname='/', 
	serve_locally=True
)

app.title = "Sigrid og Helge sitt kodeprogram"
server = app.server

for logger in (app.logger,):
	logger.setLevel(logging.INFO)
	logger.addHandler(default_handler)

controls_left = dbc.Card([
	html.Div(
	    [
	        dbc.Label("Skriv inn teksten som skal kodes"),
	        dbc.Input(id="text-input", size="lg", placeholder="...", type="text"),

	    ]
	),
	dbc.Label("Velg kodetype", style={"marginTop": "15px"}),
	dbc.ButtonGroup(
				[
					dbc.RadioItems(
						id="valg",
						className="btn-group",
						inputClassName="btn-check btn-lg",
						labelClassName="btn btn-outline-primary btn-lg",
						labelCheckedClassName="active",
						options=[ {"label": k, "value": k} for k in ["Ingen", "Caesar", "Dobbel Caesar"] ],
						value="Ingen"
					),
				],
				className="radio-group",
			),
	html.Div(
	    [
	        dbc.Label("Første nøkkel"),
	        dbc.Input(id="key1", size="lg", value="1", type="text"),

	    ]
	),
	html.Div(
	    [
	        dbc.Label("Andre nøkkel"),
	        dbc.Input(id="key2", size="lg", value="0", type="text"),

	    ]
	),
    dbc.Switch(
        id="retning",
        label="Kode eller dekode?",
        value=False,
    ),
    ],
	body=True
)

controls_right = dbc.Card(
	[
		dbc.Label("Resultat:"),
        dbc.Textarea(
            invalid=True, size="lg", placeholder="...", id="result"
        ),
    ],
	body=True,
)

app.layout = html.Div([
	dbc.Col(html.H1("Sigrid og Helge sitt kodeprogram", className="text-center"), md=9),
	dbc.Row(
		[
		dbc.Col(
				[
					controls_left,
	   				controls_right
				],
			),
		],
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)