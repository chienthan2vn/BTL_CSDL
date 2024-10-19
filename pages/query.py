import streamlit as st
import requests
from datetime import datetime

def add_company():
    name = st.text_input("Tên công ty")
    tax_code = st.text_input("Mã số thuế")
    charter_capital = st.text_input("Vốn điều lệ")
    industry = st.text_input("Lĩnh vực")
    employee_count = st.text_input("Số lượng nhân viên")
    address = st.text_input("Địa chỉ")
    phone = st.text_input("Số điện thoại")
    area = st.text_input("Diện tích thuê")
    labels = requests.get("http://localhost:5000/api/get_service").json()
    choice = [f"Mã: {i[2]}, Tên: {i[0]}, giá: {i[1]}" for i in labels.values()]
    st.markdown(choice)
    services = st.multiselect("Dịch vụ cần thuê:", labels)

    if st.button("Gửi"):
        sum_ser = []
        for ser in services:
            temp = dict()
            temp["service_id"] = ser
            temp["start_date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            temp["paied"] = 0
            sum_ser.append(temp)

        data = {
            "name": name, 
            "tax_code": tax_code,
            "charter_capital": charter_capital,
            "industry": industry,
            "employee_count": employee_count,
            "address": address,
            "phone": phone,
            "area": area,
            "used_service": sum_ser
        }
        try: 
            response = requests.post("http://localhost:5000/api/add_companies", json={"selector":data})
            st.success("Dữ liệu đã được gửi thành công!")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Có lỗi xảy ra: {e}")



def del_company():
    name = st.text_input("Tên công ty")
    tax_code = st.text_input("Mã số thuế")

    if st.button("Gửi"):
        data = {
            "name": name, 
            "tax_code": tax_code
        }
        try: 
            response = requests.post("http://localhost:5000/api/del_companies", json={"selector": data})
            st.success("Dữ liệu đã được gửi thành công!")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Có lỗi xảy ra: {e}")


def update_company():
    name = st.text_input("Tên công ty")
    tax_code = st.text_input("Mã số thuế")
    st.write("Thông tin cần thay đổi (không nhập thông tin sẽ giữ nguyên)")
    labels = {
        "Tên công ty": "name",
        "Mã số thuế": "tax_code",
        "Vốn điều lệ": "charter_capital",
        "Lĩnh vực": "industry",
        "Số nhân viên": "employee_count",
        "Địa chỉ": "address",
        "SĐT": "phone",
        "Diện tích thuê": "area"
    }

    nameC = st.text_input("Tên công ty thay đổi", "")
    tax_codeC = st.text_input("Mã số thuế thay đổi", "")
    charter_capital = st.text_input("Vốn điều lệ thay đổi", "")
    industry = st.text_input("Lĩnh vực thay đổi", "")
    employee_count = st.text_input("Số lượng nhân viên thay đổi", "")
    address = st.text_input("Địa chỉ thay đổi", "")
    phone = st.text_input("Số điện thoại thay đổi", "")
    area = st.text_input("Diện tích thuê thay đổi", "")

    if st.button("Gửi"):
        temp = {
            "name": nameC, 
            "tax_code": tax_codeC,
            "charter_capital": charter_capital,
            "industry": industry,
            "employee_count": employee_count,
            "address": address,
            "phone": phone,
            "area": area,
        }
        data = temp.copy()
        for i in temp:
            if temp[i] == "":
                del data[i]
        query = {"name": name, "tax_code": tax_code}
        try: 
            response = requests.post("http://localhost:5000/api/update_companies", json={"data":data, "query": query})
            st.success("Dữ liệu đã được gửi thành công!")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Có lỗi xảy ra: {e}")
