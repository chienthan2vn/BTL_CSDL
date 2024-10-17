# Kết nối đến MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@b24chkh020.g4tmn.mongodb.net/?retryWrites=true&w=majority&appName=B24CHKH020")  # Thay đổi URI nếu cần
db = client["btl"]


# Khởi tạo flask
from flask import Flask
app = Flask(__name__)
