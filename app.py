import streamlit as st
import joblib

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Flipkart Review Sentiment Analysis")

review = st.text_area("Enter your review")

if st.button("Predict"):
    vec = vectorizer.transform([review])
    pred = model.predict(vec)[0]
    st.write("Positive 😊" if pred == 1 else "Negative 😞")
