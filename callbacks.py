from dash import Dash, html, dcc, dash_table, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import logging
import datetime
import string

alphabet = "abcdefghijklmnopqrstuvwyxzæøå"
alphabet += alphabet
alphabet_upper = alphabet.upper()

logger = logging.getLogger("callbacks.py")
	
@callback(
	Output("result", "value"), 
	[
		Input("valg", "value"), 
		Input("key1", "value"), 
		Input("key2", "value"), 
		Input("text-input", "value"), 
		Input("retning", "value")
	]
)
def encode(valg, key1, key2, text_input, retning):
	if not key1.isnumeric() or not key2.isnumeric():
		return text_input

	key1 = int(key1)
	key2 = int(key2)

	key1 = key1 % len(alphabet)
	key2 = key2 % len(alphabet)

	if retning:
		key1 = -key1
		key2 = -key2

	if valg == "Ingen":
		return text_input
	if valg == "Caesar":
		new_string = ""

		for bokstav in text_input:
			if bokstav in alphabet:
				new_string += alphabet[alphabet.index(bokstav) + key1]
			elif bokstav in alphabet_upper:
				new_string += alphabet_upper[alphabet_upper.index(bokstav) + key1]
			else:
				new_string += bokstav

		return new_string

	if valg == "Dobbel Caesar":
		new_string = ""
		idx = 0
		keys = [key1, key2]

		for bokstav in text_input:
			if bokstav in alphabet:
				new_string += alphabet[alphabet.index(bokstav) + keys[idx%2]]
			elif bokstav in alphabet_upper:
				new_string += alphabet_upper[alphabet_upper.index(bokstav) + keys[idx%2]]
			else:
				new_string += bokstav
			idx += 1

		return new_string
	return "Hei"