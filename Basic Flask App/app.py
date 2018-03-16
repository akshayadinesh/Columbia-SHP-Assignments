from flask import Flask, render_template, request, redirect, make_response
import requests
import sqlite3

app = Flask(__name__)

base_url = 'http://api.forismatic.com/api/1.0/?format=json&lang=en&method=getQuote'

@app.route('/get-quote')
def quote():
	response = requests.get(base_url).json()
	return render_template('random_quote.html', quote=response)

@app.route('/')
@app.route('/home')
def home():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	username = request.cookies.get('username', default='null', type=str)
	if username is 'null':
		return render_template('signin.html')
	else:
		c.execute('''select * from quotes where username="'''+username+'''"''')
		return render_template('my_quotes.html', quotes=c.fetchall())
	conn.close()

@app.route('/sign-in')
def signin():
	username = request.args.get('username')
	response = make_response(redirect('/'))
	response.set_cookie('username', username)
	return response

@app.route('/save-quote')
def save():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	quote = request.args.get('quote')
	author = request.args.get('author')
	c.execute('''insert into quotes values(null, "''' + request.cookies.get('username', default='null', type=str) + '''", "'''+ quote +'''", "'''+ author +'''")''')
	conn.commit()
	conn.close()
	return home()

if __name__ == '__main__':
	app.run(host="0.0.0.0")