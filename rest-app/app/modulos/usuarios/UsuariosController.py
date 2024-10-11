from . import usuarios_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json

from flask import current_app as app
import datetime
from app.models import db

@usuarios_blueprint.route("/usuarios", methods=["GET"])
def usuarios():
    resp = jsonify(message="hello world")
    return resp