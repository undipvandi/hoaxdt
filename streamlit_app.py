import streamlit as st

# Set the title and description of the app
st.title("📰 Hoax News Detector")
st.subheader("Deteksi Berita Hoax dengan Mudah")
st.write(
    "Masukkan teks berita yang ingin Anda periksa, dan aplikasi ini akan membantu mendeteksi apakah berita tersebut hoax atau tidak."
)

# Create a form for user input
with st.form("hoax_detection_form"):
    # Input field for news text
    news_text = st.text_area("Masukkan teks berita di sini:", height=200)
    
    # Submit button
    submitted = st.form_submit_button("Deteksi Berita")

# Process the input when the form is submitted
if submitted:
    if news_text.strip() == "":
        st.warning("Silakan masukkan teks berita terlebih dahulu.")
    else:
        # Placeholder for detection logic
        st.info("Sedang memproses...")
        
        # Simulasi hasil deteksi (ganti dengan model deteksi sebenarnya)
        import random
        is_hoax = random.choice([True, False])
        
        if is_hoax:
            st.error("🚨 Berita ini terdeteksi sebagai HOAX!")
        else:
            st.success("✅ Berita ini terdeteksi sebagai berita ASLI.")