# get companies info detail
from .utils import *

def get_companies_info_detail():
    start_companies = "2024-09".split("-")
    companies = dict()
    tempCompanies = get_collection("companies")
    services_price = get_services()

    for doc in tempCompanies:
        del doc['_id']
        companies[doc['name']] = doc
        temp = dict()
        for i in range(int(start_companies[0]), int(datetime.now().year+1)):
            for j in range(int(start_companies[1]), int(datetime.now().month+1)):
                temp[f"{i}_{j}"] = get_total_expense(doc['name'], j, i)
        companies[doc['name']]['total_expense'] = temp
    return companies


def get_staff_info_detail():
    staffs = dict()
    tempStaffs = get_collection("employees")
    for doc in tempStaffs:
        del doc['_id']
        staffs[doc['name']] = doc
        temp = dict()
        temp_tl = doc['timestamp_location'].copy()
        for tl in doc['timestamp_location']:
            time = tl['date']
            day, month, year = time.day, time.month, time.year
            if day != today() or not check_datetime(month, year):
                temp_tl.remove(tl)
        staffs[doc['name']]["timestamp_location"] = temp_tl
    return staffs


def get_staff_office():
    staffs = dict()
    tempStaffs = get_collection("buildingEmployees")
    for doc in tempStaffs:
        del doc['_id']
        staffs[doc['name']] = doc  
        staffs[doc['name']]['total_salary'] = get_salary_staff_office(doc['name'])

    return staffs
