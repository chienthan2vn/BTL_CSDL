from . import db
from datetime import datetime
import calendar
import json
from flask import jsonify

# Get collection
def get_collection(collection_name):
    collection = db[collection_name]
    # Lấy tất cả tài liệu trong bộ sưu tập
    documents = collection.find()
    return documents
        

#get fields
def get_fields(collection_name):
    collection = db[collection_name]
    document = collection.find_one()

    if document:
        field_names = list(document.keys())  # Lấy danh sách tên các trường
    return field_names


#get services price
def get_services():
    info = dict()
    temp = get_collection("services")
    for doc in temp:
        info[doc['IdService']] = [doc['name'], doc['base_price'], doc['IdService']]
    return info


#used service quantity
def get_used_service_quantity():
    info = dict()
    tempCompanies = get_collection("companies")
    for doc in tempCompanies:
        for ser in doc['used_service']:
            start_time = ser['start_date']
            month, year = start_time.month, start_time.year
            if check_datetime(month, year) and not ser['paied']:
                if ser['service_id'] not in info:
                    info[ser['service_id']] = 1
                else: 
                    info[ser['service_id']] += 1
    return info


#get office employees quantity
def get_office_employees_quantity():
    info = dict()
    tempCompanies = get_collection("buildingEmployees")
    for doc in tempCompanies:
        if doc['position'] not in info:
            info[doc['position']] = 1
        else: 
            info[doc['position']] += 1
    return info


# day month year process
def today():
    return datetime.now().day

def days_in_current_month():
    today = datetime.now()
    year = today.year
    month = today.month
    num_days = calendar.monthrange(year, month)[1]
    return num_days

def check_datetime(month, year):
    today = datetime.now()
    yearN = today.year
    monthN = today.month
    if year==yearN and month==monthN:
        return True
    return False


#get total expense
def get_total_expense(company, monthC, yearC):
    companies = dict()
    tempCompanies = get_collection("companies")
    services_price = get_services()
    for doc in tempCompanies:
        del doc['_id']
        companies[doc['name']] = doc

    total_expense = 5000000*companies[company]['area']
    dup_area, dup_emp = 0,0
    if (companies[company]['area']-100) > 0: dup_area = (companies[company]['area']-100)
    if (companies[company]['employee_count']-10) > 0: dup_emp = (companies[company]['employee_count']-10)
    dup = 1 + 0.05*(dup_area//10 + dup_emp//5)

    for ser in companies[company]['used_service']:
        start_time = ser['start_date']
        day, month, year = start_time.day, start_time.month, start_time.year
        if month==monthC and year==yearC and not ser['paied']:
            if check_datetime(monthC, yearC):
                total_expense += round(dup*((today()-day)/days_in_current_month())*services_price[ser['service_id']][1])
            else:
                total_expense += round(dup*services_price[ser['service_id']][1])
    return total_expense


#get salary staff
def get_salary_staff_office(name):
    staff = dict()
    tempStaff = get_collection("buildingEmployees")
    uesd_service_quantity = get_used_service_quantity()
    office_employees_quantity = get_office_employees_quantity()
    services_price = get_services()
    for doc in tempStaff:
        del doc['_id']
        staff[doc['name']] = doc

    salary = 1000000*staff[name]['level'] + (services_price[staff[name]['position']][1]*uesd_service_quantity[staff[name]['position']])/office_employees_quantity[staff[name]['position']]
    return salary


#get name of field
def get_name(collection, field):
    temp = get_collection(collection)
    results = []
    for doc in temp:
        results.append(doc[field])
    results.append("ALL")
    return results


#add data
def add_company(company):
    collection = db["companies"]
    x = company["tax_code"]
    if company["tax_code"] not in get_name("companies", "tax_code"):
        collection.insert_one(company)
        return jsonify({"message": "Công ty đã được thêm thành công!"}), 201  # Trả về mã trạng thái 201
    else:
        return jsonify({"message": "Mã thuế đã tồn tại!"}), 400 


def add_employ(employ):
    collection = db["employees"]
    if employ["identity_card"] not in get_name("employees", "identity_card"):
        collection.insert_one(employ)


def add_office(employ):
    collection = db["buildingEmployees"]
    if employ["phone"] not in get_name("buildingEmployees", "phone"):
        collection.insert_one(employ)

    

#del data
def del_company(data):
    collection = db["companies"]
    result = collection.delete_one(data)
    if result.deleted_count > 0:
        return jsonify({"message": "Công ty đã được xóa thành công!"}), 201
    else:
        return jsonify({"message": "Not Found"}), 404

    
def del_employ(employ, cmt):
    collection = db["employees"]
    query = {'name':employ, 'identity_card':cmt}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        return result

def del_office(employ, phone):
    collection = db["buildingEmployees"]
    query = {'name':employ, 'phone':phone}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        return result


#update data
def update_company(query, data):
    collection = db["companies"]
    change = {'$set': data}
    result = collection.update_one(query, change)
    if result.modified_count > 0:
        return jsonify({"message": "Công ty đã được cập nhập thành công!"}), 201
    else:
        return jsonify({"message": "Not Found"}), 404
    
def update_employ(employ, cmt, data):
    collection = db["employees"]
    query = {'name':employ, 'tax_code':cmt}
    change = {'$set': data}
    result = collection.update_one(query, change)
    if result.modified_count > 0:
        return result

def update_office(employ, phone, data):
    collection = db["buildingEmployees"]
    query = {'name':employ, 'tax_code':phone}
    change = {'$set': data}
    result = collection.update_one(query, change)
    if result.modified_count > 0:
        return result
    
#update service
def update_service(company, mst, data):
    collection = db["companies"]
    query = {'name':company, 'tax_code':mst}
    change = {'$push': data}
    result = collection.update_one(query, change)
    if result.modified_count > 0:
        return result