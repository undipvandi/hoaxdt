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
st.title("📰 Pendeteksi Berita Hoax")
st.subheader("Tugas Transformasi Digital")
st.write("Aplikasi pendeteksi berita hoax dengan studi kasus tusuk jarum pencegah stroke.")

# Input teks dari pengguna
user_input = st.text_area("Masukkan Teks Berita:", "Pasien stroke diobati dengan tusuk jarum")

# Tombol untuk memicu prediksi
if st.button("Deteksi"):
    if not user_input.strip():
        st.error("🚨 Teks tidak boleh kosong!")
    else:
        # Muat model
        model = load_model()
        
        # Prediksi
        prediction = model.predict([user_input])[0]
        result = "🚨 Berita ini terdeteksi sebagai HOAX!" if prediction == 1 else "✅ Berita ini terdeteksi sebagai berita ASLI."
        
        # Tampilkan hasil
        # st.success(f"Prediksi: **{result}**")

        if prediction == 1:
            st.error(f"**{result}**")
        else:
            st.success(f"**{result}**")

# Tampilkan metrik evaluasi model
if st.checkbox("Tampilkan metrik"):
    _, accuracy, report = train_model()
    st.write(f"**Akurasi Model:** {accuracy:.2f}")
    st.write(f"**Model:** SVM")
    st.write(f"**Dataset:** https://raw.githubusercontent.com/undipvandi/hoaxdt/refs/heads/main/data1.csv")
    st.write("**Laporan Klasifikasi:**")
    st.json(report)

footer_html = """
<div style='text-align: center;'>
<p>Dikembangan oleh Kelompok 2 ❤️</p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)