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

# Pastikan sudah mengunduh stopwords dari nltk
nltk.download('stopwords')

# Judul aplikasi
st.title("Deteksi Hoax dengan Machine Learning")

# Langkah 1: Load dataset
st.write("Mengunggah dataset...")
data = pd.read_csv("data1.csv")

# Langkah 2: Preprocessing
data = data.dropna(subset=["informasi", "label"])
data['label'] = data['label'].apply(lambda x: 1 if x == 'hoax' else 0)

# Langkah 3: Membagi data menjadi train dan test set
X = data['informasi']  # Teks berita
y = data['label']  # Label (hoax atau valid)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Langkah 4: Membuat pipeline untuk preprocessing dan model
model = make_pipeline(TfidfVectorizer(stop_words=stopwords.words('indonesian')), SVC(kernel='linear', class_weight='balanced'))

# Langkah 5: Melatih model
st.write("Melatih model...")
model.fit(X_train, y_train)

# Langkah 6: Evaluasi model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write("Akurasi:", accuracy)
st.write("Classification Report:")
st.text(classification_report(y_test, y_pred))

# Langkah 7: Prediksi
st.write("Masukkan teks untuk prediksi:")
text_to_predict = st.text_input("Teks berita", "tusuk jari bagi pasien stroke berbahaya")
if st.button("Prediksi"):
    prediction = model.predict([text_to_predict])
    result = "Hoax" if prediction[0] == 1 else "Valid"
    st.write("Prediksi:", result)