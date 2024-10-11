from . import endpoints_informes_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json

from flask import current_app as app
import datetime
from app.models import db

@endpoints_informes_blueprint.route("/endpoint_informes", methods=["GET"])
def endpoint_informes():
    resp = jsonify(message="hello world")
    return resp