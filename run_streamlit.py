from pages import require_query
import streamlit as st
from streamlit_option_menu import option_menu
import requests

# Tiêu đề ứng dụng
st.title("Office management system")

def run():
    options = ['Require query','Query','About']
    with st.sidebar:        
        app = option_menu(
            menu_title='Menu',
            options=options,
            icons=['menu-up','sign-intersection','search','cloud-download','reply','info-circle-fill'],
            menu_icon='menu-button-wide',
            default_index=0,
            styles={
                "container": {"padding": "5!important","background-color":'black'},
                "icon": {"color": "white", "font-size": "20px"}, 
                "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},}
            )

    if app == "About":
        st.write("Copyright Thuan Luong")
    if app == "Require query":
        choice = ["","Thông tin công ty", "Thông tin nhân viên", "Thông tin nhân viên tòa nhà"]
        option = st.selectbox("Choice", choice)
        if option == choice[1]:
            require_query.companies_info_detail()
        elif option == choice[2]:
            require_query.employees_info_detail()
        elif option == choice[3]:
            require_query.office_info_detail()
    if app == "Query":
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")
run()