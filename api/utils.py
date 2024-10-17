from . import db

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


