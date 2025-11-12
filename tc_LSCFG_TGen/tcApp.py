import streamlit as st

import tcGenerateLogic as tcGenerateLogic

#Creating the web interface
st.title("UC2TC_gpt-4o")
st.subheader("Automatic Generation of Test Cases from Use Case")

uat = tcGenerateLogic.UATLogic()

user_input = st.text_area(label='Use Case:', value="", height=200)

if st.button("Submit"):
    res =""
    markdown = True
    ans = uat.generateUATfromTestPath(user_input)
    
    for uat in ans:
        st.subheader("TEST: "+uat["ID"])
        st.subheader("TITLE: "+uat["DESCRIPTION"])
        st.subheader("PRECONDITION: "+uat["PRECONDITION"])
        
        table = {}
        table["Step"]=[]
        table["Input"] =[]
        table["Result"] = []
        for row in uat["TEST"]:
            table["Step"].append(row["STEP"])
            table["Input"].append(row["INPUT"])
            table["Result"].append(row["RESULT"])
        st.table(table)
        st.subheader("\n")

        

