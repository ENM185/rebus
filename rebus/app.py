#!/usr/bin/env python3

from flask import Flask, jsonify, send_from_directory

app = Flask(__name__) # app is our Flask object

@app.route('/')
def index():
    return send_from_directory("../public/", "index.html")

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory("../public/js", filename)

@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory("../public/css", filename)

@app.route('/puzzle')
def puzzle():
	#TODO
    return jsonify(
		{
			"answer": "Hella",
			"puzzle": ["<b>Pingus</b>","<i>This is on another line</i>"]
		}
	)
