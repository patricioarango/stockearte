from . import endpoints_informes_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json
from sqlalchemy import text
from flask import current_app as app
import datetime
from app.models import db

@endpoints_informes_blueprint.route("/endpoint_informes", methods=["GET"])
def endpoint_informes():
    result = db.session.execute(text("select oi.product_code,SUM(case when po.state <> 'RECHAZADA' then requested_amount else 0 end) as cantidad_pedida,po.id, created_at,po.state, id_store,oi.product_code,oi.id, purchase_order_id, color, size, product_code, send, requested_amount,created_at, id_dispatch_order, purchase_order_date, observation, reception_date, state, id_store from order_item oi inner join purchase_order po on po.id=oi.purchase_order_id group by oi.product_code"))

    result_list = []
    for row in result:
        row_dict = {
            "product_code": row[0],
            "cantidad_pedida": row[1],
            "created_at": row[2],
            "state": row[3],
            "id_store": row[4]
        }
        result_list.append(row_dict)

    return jsonify(result_list)

@endpoints_informes_blueprint.route("/endpoint_validate_user", methods=["POST"])
def endpoint_validate_user():
    username = request.json.get('username') 
    password = request.json.get('password')
    
    query = text("SELECT u.id_user, u.username, r.role, u.name, u.lastname, s.id_store, s.store "
                 "FROM user u "
                 "JOIN role r ON u.id_role = r.id_role "
                 "JOIN store s ON u.id_store = s.id_store "
                 "WHERE u.username = :username AND u.password = :password")
    
    result = db.session.execute(query, {'username': username, 'password': password}).fetchone()

    if result:
        user_data = {
            "idUser": result[0],
            "username": result[1],
            "role": {
                "roleName": result[2]
            },
            "name": result[3],
            "lastname": result[4],
            "store": {
                "idStore": result[5],
                "storeName": result[6]
            }
        }
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "Datos incorrectos"}), 401
