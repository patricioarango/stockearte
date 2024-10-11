from . import catalogos_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json
from app.models import Catalog,CatalogProducts,Product
from flask import current_app as app
import datetime
from app.models import db

@catalogos_blueprint.route("/catalogos", methods=["GET"])
def catalogos():
    return 200