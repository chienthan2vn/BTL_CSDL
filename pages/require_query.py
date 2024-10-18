import streamlit as st
import requests
import pandas as pd

def companies_info_detail():
    data = requests.get("http://localhost:5000/api/companies").json()
    # Chuyển đổi dữ liệu thành DataFrame
    df = pd.DataFrame.from_dict(data, orient='index')
    # Hiển thị dữ liệu
    st.title("Thông Tin Công Ty")
    st.dataframe(df)

    detail = st.selectbox("Chọn công ty để xem chi tiết:", df.index)

    if detail:
        st.subheader(f"Chi tiết về {detail}")
        st.dataframe(data[detail])

        sub_detail = st.selectbox("Chọn thuộc tính để xem chi tiết:", data[detail].keys())
        try:
            st.dataframe(data[detail][sub_detail])
        except:
            st.write(data[detail][sub_detail])


def employees_info_detail():
    data = requests.get("http://localhost:5000/api/staff").json()
    # Chuyển đổi dữ liệu thành DataFrame
    df = pd.DataFrame.from_dict(data, orient='index')

    # Hiển thị dữ liệu
    st.title("Thông Tin Nhân Viên")
    st.dataframe(df)

    detail = st.selectbox("Chọn nhân viên để xem chi tiết:", df.index)

    if detail:
        st.subheader(f"Chi tiết về {detail}")
        st.dataframe(data[detail])

        sub_detail = st.selectbox("Chọn thuộc tính để xem chi tiết:", data[detail].keys())
        try:
            st.dataframe(data[detail][sub_detail])
        except:
            st.write(data[detail][sub_detail])


def office_info_detail():
    data = requests.get("http://localhost:5000/api/office").json()
    # Chuyển đổi dữ liệu thành DataFrame
    df = pd.DataFrame.from_dict(data, orient='index')

    # Hiển thị dữ liệu
    st.title("Thông Tin Nhân Viên Toà Nhà")
    st.dataframe(df)

    detail = st.selectbox("Chọn nhân viên tòa nhà để xem chi tiết:", df.index)

    if detail:
        st.subheader(f"Chi tiết về {detail}")
        st.dataframe(data[detail])

        sub_detail = st.selectbox("Chọn thuộc tính để xem chi tiết:", data[detail].keys())
        try:
            st.dataframe(data[detail][sub_detail])
        except:
            st.write(data[detail][sub_detail])