import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Data Objects Example")

# Display JSON data
st.subheader("JSON Data")

# Sample JSON data
json_data = {
    "name": "KGP Talkie",
    "age": 30,
    "city": "Mumbai"
}
st.json(json_data) # Hiển thị dữ liệu dạng JSON theo cấu trúc.

# Sample DataFrame
# Display DataFrame
st.subheader("DataFrame")

df = pd.read_csv("data/auto.csv")
st.dataframe(df.head()) # Cho phép cuộn, sắp xếp cột

# Display DataFrame as table
st.subheader("DataFrame as Table")
st.table(df.head()) # Hiển thị bảng tĩnh — không cuộn hay chỉnh sửa

# Hiển thị mã nguồn
st.subheader("Sample Code")

sample_code = '''
def greet(name):
    return "Hello, " + name + "!"
    
print(greet("KGP Talkie"))
'''
st.code(sample_code, language='python')

# Sample metric
st.subheader("Sample Metric")
st.metric("Accuracy", value=0.85, delta=+0.05) # accuracy tăng thêm 5%

# Sample data editor
st.subheader("Data Editor")
edited_data = st.data_editor(df.head()) # Cho phép chỉnh sửa dữ liệu trực tiếp trên web

st.write("Edited DataFrame:")
st.write(edited_data) # Hiển thị dữ liệu đã được chỉnh sửa

edited_data.to_csv("data/edited_data.csv", index=False)