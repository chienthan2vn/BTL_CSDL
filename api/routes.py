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
@app.route("/api/add_companies", methods=["POST"])
def add_companies():
    selector = request.json.get("selector")
    return add_company(selector)

@app.route("/api/add_employees", methods=["POST"])
def add_employees():
    selector = request.json.get("selector")
    return add_company(selector)

@app.route("/api/add_office", methods=["POST"])
def add_office():
    selector = request.json.get("selector")
    return add_company(selector)

#===================================================================
@app.route("/api/del_companies", methods=["POST"])
def del_companies():
    selector = request.json.get("selector")
    print(selector)
    return del_company(selector)

#===================================================================
@app.route("/api/update_companies", methods=["POST"])
def update_companies():
    selector1 = request.json.get("query")
    selector2 = request.json.get("data")
    return update_company(selector1, selector2)

#===================================================================
@app.route("/api/update_service", methods=["POST"])
def update_service():
    selector = request.json.get("company", "mst", "data")
    return update_company(selector[0], selector[1], selector[2])


#===================================================================
@app.route("/api/get_service", methods=["GET"])
def get_service():
    return jsonify(get_services())