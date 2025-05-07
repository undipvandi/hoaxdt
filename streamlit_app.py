import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline
import joblib
import os

# Download stopwords
nltk.download('stopwords', quiet=True)

# Fungsi untuk melatih dan menyimpan model
@st.cache_resource
def train_model():
    # Load dataset
    data = pd.read_csv("data1.csv")
    data = data.dropna(subset=["informasi", "label"])
    data['label'] = data['label'].apply(lambda x: 1 if x == 'hoax' else 0)

    # Split data
    X = data['informasi']
    y = data['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Buat dan latih model
    model = make_pipeline(
        TfidfVectorizer(stop_words=stopwords.words('indonesian')),
        SVC(kernel='linear', class_weight='balanced')
    )
    model.fit(X_train, y_train)

    # Evaluasi
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Simpan model
    joblib.dump(model, 'svm_model_hoax_detector.pkl')
    return model, accuracy, report

# Fungsi untuk memuat model
@st.cache_resource
def load_model():
    if os.path.exists('svm_model_hoax_detector.pkl'):
        return joblib.load('svm_model_hoax_detector.pkl')
    else:
        model, _, _ = train_model()
        return model

# Antarmuka Streamlit
st.title("Detektor Berita Hoax")
st.write("Masukkan teks berita untuk memprediksi apakah itu hoax atau valid.")

# Input teks dari pengguna
user_input = st.text_area("Masukkan teks berita:", "Pasien stroke diobati dengan tusuk jarum")

# Tombol untuk memicu prediksi
if st.button("Prediksi"):
    if not user_input.strip():
        st.error("Teks tidak boleh kosong!")
    else:
        # Muat model
        model = load_model()
        
        # Prediksi
        prediction = model.predict([user_input])[0]
        result = "Hoax" if prediction == 1 else "Valid"
        
        # Tampilkan hasil
        st.success(f"Prediksi: **{result}**")

# Tampilkan metrik evaluasi model
if st.checkbox("Tampilkan metrik evaluasi model"):
    _, accuracy, report = train_model()
    st.write(f"**Akurasi Model:** {accuracy:.2f}")
    st.write("**Laporan Klasifikasi:**")
    st.json(report)