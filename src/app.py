#!/usr/bin/python3

from flask import Flask, redirect, url_for, render_template, Markup
#import threading
#import subprocess


app = Flask(__name__)

# event = threading.event

@app.route("/")
def index():
	temperatur = 0
	feuchtigkeit = 0
	#with open('log.txt','r') as log :
		#temperatur = log[:]
		#feuchtigkeit = log[:]
	return render_template("index.html",{
		'TEMPERATUR': temperatur,
		'FEUCHTIGKEIT': feuchtigkeit
	})

@app.route("/kontroll")
def kontroll():
	kontroll_daten = {
		'licht_an': True,
		'licht_auto' : True,
		'ventil_an': True,
		'ventil_auto' : True,
		'befeuchter_an': True,
		'befeuchter_auto' : True,
	}
	kontroll_daten_text = "kontroll_daten = {'licht_an': True,'licht_auto' : True,'ventil_an': True,'ventil_auto' : True,'befeuchter_an': True,'befeuchter_auto' : True,}"
	return kontroll_daten_text



if __name__ == '__main__':
	app.run(debug=True)
	subprocess.run(['python','schaltung.py'])
