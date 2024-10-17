# get companies info detail
from . import get_collection

def get_companies_info_detail():
    companies, services = [], []
    tempCompanies, tempServices = get_collection("companies"), get_collection("services")

    for doc in tempCompanies:
        doc['_id'] = str(doc['_id'])
        companies.append(doc)
    for doc in tempServices:
        doc['_id'] = str(doc['_id'])
        services.append(doc)
    
    