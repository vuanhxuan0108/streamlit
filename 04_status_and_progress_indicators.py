import streamlit as st
import time

# Title
st.title("Streamlit Status and Progress Indicator Examples")

# Thay đổi
st.subheader("Empty Element")
empty_elem = st.empty() # Chỗ trống để ghi đè nội dung sau này
empty_elem.text("This text will be replaced after 3 seconds...")
time.sleep(3)
empty_elem.text("Replaced!") # Sau 3s, ghi đè

# Thanh tiến trình
st.subheader("Progress Bar")
progress_bar = st.progress(1) # Thanh tiến trình
status_text = st.empty() # Chỗ trống để ghi đè nội dung sau này

for i in range(1, 101):
    time.sleep(0.05)
    progress_bar.progress(i) # Cập nhật thanh tiến tình sau mỗi 0.05s
    status_text.text(f"Progress: {i}%")
status_text.text("Progress: Done!")

# Spinner xoay khi đang xử lý
st.subheader("Spinner")
with st.spinner("Waiting..."): # Hiển thị vòng xoay “Waiting…” trong 5 giây
    time.sleep(5)
st.success("Process completed!") # Hiện thông báo “Process completed!”

# Trạng thái
st.subheader("Status")
st.status("This is a status message")

# Hiển thị các loại cảnh báo
st.subheader("Toast")
st.warning("This is a warning message") # Cảnh báo
st.error("This is an error message") # Lỗi
st.success("This is a success message") # Hoàn thành
st.info("This is an info message") 

# Hiệu ứng hình ảnh
st.subheader("Snow")
st.snow() # Tuyết rơi

st.subheader("Balloons")
st.balloons() # Bóng bay


