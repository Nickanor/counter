from flask import Flask, render_template, redirect, session, request
app=Flask(__name__)
app.secret_key='secretkey'

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/increment', methods=['POST'])
def increment():
    session['count'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
