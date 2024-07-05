import streamlit as st

st.title("Welcome to Data Doodles")
st.header('python')
st.subheader("Java")
st.markdown("I like Python")    #text
st.code("""for i in range(1,5,1):
               print("hello")
        """)



name=st.text_input("Enter your name: ")
fname=st.text_input("Enter your father's name :")
adr=st.text_area("Enter your text: ")
classdata=st.selectbox("Enter your class: ",(1,2,3,4,5))

# making button
button=st.button("Done")
if button:
    st.markdown(f"""
    Name: {name}
    Father's Name: {fname}
    address: {adr}
    class: {classdata}""")