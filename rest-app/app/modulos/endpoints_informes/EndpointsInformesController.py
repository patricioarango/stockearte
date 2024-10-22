from . import endpoints_informes_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json
from sqlalchemy import text
from flask import current_app as app
import datetime
from app.models import db

class UserFilter(db.Model):
    __tablename__ = 'user_filters'
    __table_args__ = {'extend_existing': True} 
    id_user_filter = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    filter = db.Column(db.String(255), nullable=False)
    cod_prod = db.Column(db.String(50))
    date_from = db.Column(db.Date)
    date_to = db.Column(db.Date)
    state = db.Column(db.String(50))
    id_store = db.Column(db.Integer)
    enabled = db.Column(db.Boolean, default=True)

@endpoints_informes_blueprint.route("/endpoint_informes", methods=["GET"])
def endpoint_informes():
    result = db.session.execute(text("select oi.product_code,SUM(case when po.state <> 'RECHAZADA' then requested_amount else 0 end) as cantidad_pedida,po.id, created_at,po.state, id_store,oi.product_code,oi.id, purchase_order_id, color, size, product_code, send, requested_amount,created_at, id_dispatch_order, purchase_order_date, observation, reception_date, state, id_store from order_item oi inner join purchase_order po on po.id=oi.purchase_order_id group by oi.product_code"))

    result_list = []
    for row in result:
        row_dict = {
            "product_code": row[0],       
            "cantidad_pedida": row[1],     # SUM(case when po.state <> 'RECHAZADA' then requested_amount else 0 end)
            "id_purchase_order": row[2],   
            "created_at": row[3],          
            "state": row[4],              
            "id_store": row[5]            
        }
        result_list.append(row_dict)


    return jsonify(result_list)


@endpoints_informes_blueprint.route("/guardar_filtro", methods=["POST"])
def guardar_filtro():
    try:
        data = request.get_json()
        print(f"Datos recibidos: {data}") 

        id_user_filter = data.get("id_user_filter")

        if id_user_filter:
            user_filter = UserFilter.query.get(id_user_filter)
            if not user_filter:
                return jsonify({"error": "Filtro no encontrado"}), 404

            user_filter.id_user = data.get("id_user", user_filter.id_user)
            user_filter.filter = data.get("filter", user_filter.filter)
            user_filter.cod_prod = data.get("cod_prod", user_filter.cod_prod)
            user_filter.date_from = datetime.datetime.strptime(data.get("date_from"), "%Y-%m-%d") if data.get("date_from") else user_filter.date_from
            user_filter.date_to = datetime.datetime.strptime(data.get("date_to"), "%Y-%m-%d") if data.get("date_to") else user_filter.date_to
            user_filter.state = data.get("state", user_filter.state)
            user_filter.id_store = data.get("id_store", user_filter.id_store)
            user_filter.enabled = data.get("enabled", user_filter.enabled)

            message = "Filtro editado con éxito"
        else:
            user_filter = UserFilter(
                id_user=data.get("id_user"),
                filter=data.get("filter"),
                cod_prod=data.get("cod_prod"),
                date_from=datetime.datetime.strptime(data.get("date_from"), "%Y-%m-%d") if data.get("date_from") else None,
                date_to=datetime.datetime.strptime(data.get("date_to"), "%Y-%m-%d") if data.get("date_to") else None,
                state=data.get("state"),
                id_store=data.get("id_store"),
                enabled=True
            )

            db.session.add(user_filter)
            message = "Filtro guardado con éxito"

        db.session.commit()

        return jsonify({"message": message, "id_user_filter": user_filter.id_user_filter}), 201

    except Exception as e:
        db.session.rollback()  
        print(f"Error al guardar o editar el filtro: {str(e)}")  
        return jsonify({"error": str(e)}), 400

    
@endpoints_informes_blueprint.route("/endpoint_filtros", methods=["GET"])
def endpoint_filtros():
    id_user = request.args.get("id_user", None)

    if not id_user:
        return jsonify({"error": "id_user is required"}), 400

    result = db.session.execute(text(
        "SELECT id_user_filter, id_user, filter, cod_prod, date_from, date_to, state, id_store, enabled "
        "FROM stockearte_restapp.user_filters "
        "WHERE id_user = :id_user"
    ), {"id_user": id_user}).fetchall()

    result_list = []
    for row in result:
        row_dict = {
            "id_user_filter": row[0],   
            "id_user": row[1],         
            "filter": row[2],           
            "cod_prod": row[3],        
            "date_from": row[4],        
            "date_to": row[5],         
            "state": row[6],         
            "id_store": row[7],        
            "enabled": row[8]         
        }
        result_list.append(row_dict)

    return jsonify(result_list)
  
@endpoints_informes_blueprint.route("/endpoint_filtro", methods=["GET"])
def endpoint_filtro():

    id_user_filter = request.args.get("id_user_filter", None)

    print(f'id_user_filter: {id_user_filter}')

    if not id_user_filter:
        return jsonify({"error": "id_user_filter is required"}), 400


    result = db.session.execute(text(
        "SELECT id_user_filter, id_user, filter, cod_prod, date_from, date_to, state, id_store, enabled "
        "FROM stockearte_restapp.user_filters "
        "WHERE id_user_filter = :id_user_filter"
    ), {"id_user_filter": id_user_filter}).fetchone()

 
    if not result:
        return jsonify({"error": "No filter found with the given id_user_filter"}), 404

    row_dict = {
        "id_user_filter": result[0],  
        "id_user": result[1],          
        "filter": result[2],           
        "cod_prod": result[3],        
        "date_from": result[4],        
        "date_to": result[5],         
        "state": result[6],          
        "id_store": result[7],        
        "enabled": result[8]        
    }

    return jsonify(row_dict)





