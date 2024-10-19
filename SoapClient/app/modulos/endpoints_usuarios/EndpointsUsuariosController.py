from . import endpoints_usuarios_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json

from flask import current_app as app
import datetime
from app.models import db

@endpoints_usuarios_blueprint.route("/endpoint_usuarios", methods=["GET"])
def endpoint_usuarios():
    resp = jsonify(message="hello world")
    return resp