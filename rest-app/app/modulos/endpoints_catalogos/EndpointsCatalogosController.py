from . import endpoints_catalogos_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json

from flask import current_app as app
import datetime
from app.models import db

@endpoints_catalogos_blueprint.route("/endpoint_catalogos", methods=["GET"])
def endpoint_catalogos():
    resp = jsonify(message="hello world")
    return resp