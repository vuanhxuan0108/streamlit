import streamlit as st

st.title("Streamlit Text and Display Example")

st.header("This is a header")

st.subheader("This is a subheader")

#text
st.text("This is a text data")

st.write("This is default font")

# markdown
st.markdown("# This is a markdown heading")

st.markdown("## This is a markdown heading")

st.markdown("### This is a markdown heading")

# kiểu chữ
st.markdown("## **This is a Boild text**")

st.markdown("## *This is a Italic text*")

st.markdown("> ## This is a blockquote")

# đường link
st.markdown("## [This is a link](https://www.geeksforgeeks.org/computer-vision/efficientnet-architecture/)")

# 1 danh sách
st.markdown("""
##### - This is a list
1. a
2. b
3. c

- 1
- 2
- 3
##### - This is a code
`print("Hello World)`
            
`>> Hello World`
""")
st.markdown("##### - This is a emojis: :smile:")

st.markdown("### HTML")

html_code = """
        <h1 style='color: Yellow;'>This is a blue heading</h1>
        <p style='color: Green;'>This is a green paragraph</p>
"""

st.markdown(html_code, unsafe_allow_html=True)

# Divider
st.markdown("""---""") ## Đường thẳng
st.divider() # Đường thẳng

# LaTeX
st.latex(r"e^{i\pi} + 1 = 0")
st.latex(r"f(x) = x^2 + 2x + 1")
st.latex(r"g(x) = \frac{1}{x}")
st.latex(r"h(x) = \sqrt{x}")
st.latex(r"y = mx + c")
st.latex(r"a^2 + b^2 = c^2")

# ảnh
st.image("clss.png", caption="This is an image")

