from app import create_app
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import logging
from google.protobuf.json_format import MessageToJson


logger = logging.getLogger(__name__)

app = create_app('flask.cfg')


@app.route("/", methods=["GET"])
def index():
    return render_template('home.html')

@app.route("/novedades", methods=["GET"])
def novedades():
    return render_template('novedades.html')




























































if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)