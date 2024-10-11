from . import endpoints_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json

from flask import current_app as app
import datetime
from app.models import db

@endpoints_blueprint.route("/endpoint_index", methods=["GET"])
def endpoint_index():
    resp = jsonify(message="hello world")
    return resp