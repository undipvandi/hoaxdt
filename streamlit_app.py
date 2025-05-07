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

# Pastikan stopwords sudah diunduh
nltk.download('stopwords')

# Judul aplikasi
st.title("Hoax Detector dengan SVM")

# Langkah 1: Upload dataset
uploaded_file = st.file_uploader("Unggah file CSV", type="csv")

if uploaded_file is not None:
    # Membaca dataset
    data = pd.read_csv(uploaded_file)
    st.write("Dataset:")
    st.write(data.head())

    # Langkah 2: Preprocessing
    if "informasi" in data.columns and "label" in data.columns:
        # Menghapus baris dengan nilai null
        data = data.dropna(subset=["informasi", "label"])

        # Mengonversi label menjadi 0 dan 1
        data['label'] = data['label'].apply(lambda x: 1 if x == 'hoax' else 0)

        # Langkah 3: Membagi data menjadi train dan test set
        X = data['informasi']  # Teks berita
        y = data['label']  # Label (hoax atau valid)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Langkah 4: Membuat pipeline untuk preprocessing dan model
        model = make_pipeline(
            TfidfVectorizer(stop_words=stopwords.words('indonesian')),
            SVC(kernel='linear', class_weight='balanced')
        )

        # Langkah 5: Melatih model
        if st.button("Latih Model"):
            model.fit(X_train, y_train)
            st.success("Model berhasil dilatih!")

            # Langkah 6: Evaluasi model
            y_pred = model.predict(X_test)
            st.write("Accuracy:", accuracy_score(y_test, y_pred))
            st.write("Classification Report:")
            st.text(classification_report(y_test, y_pred))

            # Menyimpan model
            joblib.dump(model, 'svm_model_hoax_detector.pkl')
            st.success("Model disimpan sebagai 'svm_model_hoax_detector.pkl'.")

        # Langkah 7: Prediksi
        st.subheader("Prediksi")
        text_to_predict = st.text_input("Masukkan teks untuk diprediksi:")
        if st.button("Prediksi"):
            if text_to_predict:
                prediction = model.predict([text_to_predict])
                st.write("Prediksi:", "Hoax" if prediction[0] == 1 else "Valid")
            else:
                st.warning("Masukkan teks untuk diprediksi.")
    else:
        st.error("Dataset harus memiliki kolom 'informasi' dan 'label'.")
else:
    st.info("Unggah file CSV untuk memulai.")