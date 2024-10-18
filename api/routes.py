from .config import *
from .controllers import *
from flask import Flask, request, jsonify
import json

@app.route("/api/companies", methods=["GET"])
def companies():
    conpanies_info = get_companies_info_detail()
    return jsonify(conpanies_info)
    
@app.route("/api/staff", methods=["GET"])
def staff():
    staff_info = get_staff_info_detail()
    return jsonify(staff_info)
    

@app.route("/api/office", methods=["GET"])
def office():
    office_info = get_staff_office()
    return jsonify(office_info)
    
#==========================================================
@app.route("/api/name_companies", methods=["GET"])
def name_companies():
    name_companies = get_name("companies", "name")
    return jsonify(name_companies)

@app.route("/api/name_service", methods=["GET"])
def name_service():
    name_service = get_name("services", "name")
    return jsonify(name_service)

@app.route("/api/name_employees", methods=["GET"])
def name_employees():
    name_employees = get_name("employees", "name")
    return jsonify(name_employees)

@app.route("/api/name_office", methods=["GET"])
def name_office():
    name_office = get_name("buildingEmployees", "name")
    return jsonify(name_office)


#==========================================================
@app.route("/api/add_companies", methods=["GET"])
def add_companies():
    selector = request.args.get("selector")
    return add_company(selector)

@app.route("/api/add_employees", methods=["GET"])
def add_employees():
    selector = request.args.get("selector")
    return add_company(selector)

@app.route("/api/add_office", methods=["GET"])
def add_office():
    selector = request.args.get("selector")
    return add_company(selector)

#===================================================================
@app.route("/api/del_companies", methods=["GET"])
def del_companies():
    selector = request.args.getlist("company", "mst")
    return del_company(selector[0], selector[1])

#===================================================================
@app.route("/api/update_companies", methods=["GET"])
def update_companies():
    selector = request.args.getlist("company", "mst", "data")
    return update_company(selector[0], selector[1], selector[2])

#===================================================================
@app.route("/api/update_service", methods=["GET"])
def update_service():
    selector = request.args.getlist("company", "mst", "data")
    return update_company(selector[0], selector[1], selector[2])