import streamlit as st
import joblib

vectorizer = joblib.load("models/vectorizer1.jb")
model = joblib.load("models/model1.jb")

st.title("News Filter")
st.write("Enter a News Article below to check whether it is Fake or Real. ")

inputnews = st.text_area("News Article:","")

if st.button("Check News"):
    if inputnews.strip():
        transform_input = vectorizer.transform([inputnews])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.success("The News is Real! ")
        else:
            st.error("The News is Fake! ")
    else:
        st.warning("Please enter some text to Analyze. ") 