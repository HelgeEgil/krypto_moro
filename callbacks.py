from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import logging
import datetime
import string

alphabet = "abcdefghijklmnopqrstuvwyxæøå"
alphabet += alphabet
alphabet_upper = alphabet.upper()

logger = logging.getLogger("callbacks.py")
	@app.callback([Output("key1", "options")],[Output("key2", "options"), Input("valg", "value")]):
	def set_options_disabled(valg):
		if valg == "Ingen":
			return [{'disabled': True}], [{'disabled': True}]
		elif valg == "Caesar":
			return [{'disabled': False}], [{'disabled': True}]
		else:
			return [{'disabled': False}], [{'disabled': False}]

	@app.callback(Output("resultat", "value"), 
		[Input("valg", "value"), Input("key1", "value"), Input("key2", "value"), Input("text_input", "value"), Input("retning", "value")])
	def encode(valg, key1, key2, text_input, retning):
		if valg == "Ingen":
			return text_input
		if valg == "Caesar":
			new_string = ""

			for bokstav in text_input:
				if bokstav in alphabet:
					new_string = alphabet[alphabet.index() + key1]
				elif bokstav in alphabet_upper:
					new_string = alphabet_upper[alphabet_upper.index() + key1]
				else:
					new_string += bokstav

			return new_string

		if valg == "Dobbel Caesar":
			idx = 0
			keys = [key1, key2]

			for bokstav in text_input:
				if bokstav in alphabet:
					new_string = alphabet[alphabet.index() + keys[idx%2]]
				elif bokstav in alphabet_upper:
					new_string = alphabet_upper[alphabet_upper.index() + keys[idx%2]]
				else:
					new_string += bokstav
				idx += 1
			return new_string
