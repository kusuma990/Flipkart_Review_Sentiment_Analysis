# Flipkart_Review_Sentiment_Analysis
# 🛍️ Sentiment Analysis of Real-Time Flipkart Product Reviews

## 📌 Project Overview

This project focuses on performing **Sentiment Analysis** on Flipkart product reviews using **Machine Learning**. The system classifies customer reviews into **Positive** or **Negative** sentiments and provides real-time predictions through a web application.

The project demonstrates an end-to-end ML pipeline including:

* Data preprocessing
* Feature extraction (TF-IDF)
* Model training
* Model deployment using Flask
* Experiment tracking using MLflow

---

## 🚀 Features

* 🔍 Analyze customer reviews instantly
* 📊 Classify sentiment (Positive / Negative)
* 🌐 Simple web interface using Flask
* 🧠 Pre-trained Machine Learning model
* 📈 MLflow integration for experiment tracking

---

## 🗂️ Project Structure

```
Sentiment Analysis of Real-time Flipkart Product Reviews/
│
├── app.py                                  # Flask web application
├── data.csv                                # Dataset of Flipkart reviews
├── sentiment_model.pkl                     # Trained ML model
├── tfidf_vectorizer.pkl                    # TF-IDF vectorizer
├── requirements.txt                        # Dependencies
├── sentiment analysis of real time flipkart product reviews.ipynb  # Model training notebook
└── README.md                               # Project documentation
```

---

## ⚙️ Technologies Used

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* Pandas & NumPy 📊
* MLflow 📈
* TF-IDF Vectorization
* streamlit

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kusuma990/Flipkart_Review_Sentiment_Analysis
cd Flipkart_Review_Sentiment_Analysis
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Now open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters a product review
2. Text is preprocessed
3. TF-IDF vectorizer converts text into numerical form
4. Trained model predicts sentiment
5. Result is displayed on the web page

---

## 📊 MLflow Tracking

To start MLflow UI:

```bash
mlflow ui
```

Then open:

```
http://127.0.0.1:5000
```

You can view:

* Experiments
* Runs
* Metrics
* Parameters

---

## 📁 Dataset

* The dataset (`data.csv`) contains Flipkart product reviews
* Includes text and sentiment labels

---

## 📌 Future Improvements

* Add Neutral sentiment class
* Deploy on cloud (AWS / Render / Heroku)
* Improve accuracy using Deep Learning (LSTM / BERT)
* Add user authentication

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Scikit-learn
* MLflow
* Open-source datasets

---

## 👨‍💻 Author

Kusuma Kumari Bodduluri
GitHub: https://github.com/kusuma990/Flipkart_Review_Sentiment_Analysis
Huggingface : https://huggingface.co/spaces/Kusuma990/Flipkart_Sentiment_Prediction
LinkedIn: www.linkedin.com/in/kusuma-kumari-bodduluri

---
## ⭐ Support
If you found this project helpful:

⭐ Star this repository 📢 Share it
