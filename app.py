from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from callbacks import get_callbacks
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
		dbc.icons.FONT_AWESOME,
		css], 
	suppress_callback_exceptions=True,  
	url_base_pathname='/', 
	serve_locally=True
)

get_callbacks()

app.title = "Sigrid og Helge sitt kodeprogram"
server = app.server

for logger in (app.logger,):
	logger.setLevel(logging.INFO)
	logger.addHandler(default_handler)

input_style = {'margin-left': '5px'}

controls_left = dbc.Card([
	html.Div(
	    [
	        dbc.Label("Skriv inn teksten som skal kodes"),
	        dbc.Input(id="input", size="lg", placeholder="...", type="text"),

	    ]
	),
	dbc.Label("Velg kodetype", style={"margin-top": "15px"}),
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
	        dbc.Input(id="key1", size="lg", placeholder="...", type="text", options={"disabled": True}),

	    ]
	),
	html.Div(
	    [
	        dbc.Label("Andre nøkkel"),
	        dbc.Input(id="key2", size="lg", placeholder="...", type="text", options={"disabled": True}),

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
				dbc.CardGroup(
					[
						controls_left,
		   				controls_right
					],
				),
				md=9
			)
	   		
		],
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)