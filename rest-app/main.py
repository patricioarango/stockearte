from app import create_app
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import logging
import os,requests

logger = logging.getLogger(__name__)

app = create_app('flask.cfg')

def checkSessionManager():
    if 'user_id' not in session or session['roleName']!='manager':
        return redirect('/login')
    
def checkSessionAdmin():
    if 'user_id' not in session or session['roleName']!='admin':
        return redirect('/login')
    
def checkSession():
    if 'user_id' not in session:
        return redirect('/login')    

@app.route("/nuevohome", methods=["GET"])
def nuevohome():
    checkSession()
    return render_template('home.html')

@app.route("/login", methods=['POST'])
def login():
    url = os.getenv("ENDPOINT_LOGIN")
    
    payload = {
        "username": request.form['username'],
        "password": request.form['password']
    }
    response = requests.post(url, json=payload)
    response_data = response.json()
    if response_data["message"]["status"] == "success":
        session['user_id'] = response_data["user"]["id_user"]
        session['username'] = response_data["user"]["username"]
        session['roleName'] = response_data["user"]["role"]
        session['name'] = response_data["user"]["name"]
        session['lastname'] = response_data["user"]["lastname"]
        session['user_store_id'] = response_data["user"]["id_store"]
        session['user_store_name'] = response_data["user"]["storeName"]
        return redirect('/nuevohome')
    else:
        flash(response_data["message"]["status"], 'danger')
        return redirect('/')
    
    



@app.route("/logout",methods = ['GET'])
def logout():
    logger.info("/logout")
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('roleName', None)
    session.pop('name', None)
    session.pop('lastname', None)
    session.pop('user_store_id', None)
    return redirect('/')

@app.route("/", methods=["GET"])
def index():
    return render_template('login.html')

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5003, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)