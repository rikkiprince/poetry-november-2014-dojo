#!/bin/usr/python

from flask import Flask, render_template
from five import five
from seven import seven
import random

images = [ "static/1.jpg","static/2.jpg","static/3.jpg","static/4.jpg", "static/5.jpg" ]

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html', image=random.choice(images), line1=random.choice(five),line2=random.choice(seven),line3=random.choice(five))

if __name__ == "__main__":
	app.debug = True
	app.run()

