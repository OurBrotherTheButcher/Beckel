from flask import Flask
from flask import request, render_template, url_for, redirect, flash, session 




app = Flask(__name__,static_folder='static')


@app.route('/', methods = ['GET','POST'])
def main():
	return render_template("home.html")


@app.route('/about', methods = ['GET','POST'])
def about():
	return render_template("AboutMe.html")


@app.route('/pod_cast_demo.xml',methods = ['GET'])
def podcast():
	return render_template('pod_cast_demo.xml')


if (__name__ == '__main__'):
	app.run()
	app.debug == True		
