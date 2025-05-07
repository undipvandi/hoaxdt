import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Deteksi Hoax App", page_icon="🕵️", layout="wide")

# CSS untuk desain menarik
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .debug-box {
        background-color: #ffcccc;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .title {
        color: #2c3e50;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #34495e;
        font-size: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar untuk navigasi
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Logo Aplikasi")  # Ganti dengan logo kamu
    st.markdown("## Navigasi")
    page = st.radio("Pilih Halaman", ["Deteksi Hoax", "Tentang Pembuat"])

# Halaman Utama: Deteksi Hoax
if page == "Deteksi Hoax":
    st.markdown("<h1 class='title'>Deteksi Hoax Berita</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Masukkan teks berita untuk mendeteksi apakah itu hoax atau bukan!</p>", unsafe_allow_html=True)

    # Layout dengan kolom
    col1, col2 = st.columns([2, 1])

    with col1:
        # Form input
        with st.form("hoax_form"):
            st.markdown("### Masukkan Berita")
            text_input = st.text_area("Teks Berita", height=200, placeholder="Masukkan teks berita di sini...")
            submit_button = st.form_submit_button("Prediksi")

        # Logika prediksi (simulasi)
        if submit_button and text_input:
            # Simulasi hasil prediksi (ganti dengan model ML kamu)
            result = "Hoax" if len(text_input.split()) % 2 == 0 else "Bukan Hoax"
            st.success(f"Hasil Prediksi: **{result}**")
            st.balloons()

    with col2:
        # Tombol Debug
        st.markdown("### Debug Info")
        if st.button("Tampilkan Debug"):
            st.markdown("<div class='debug-box'>", unsafe_allow_html=True)
            st.write(f"**Input Teks**: {text_input}")
            st.write(f"**Panjang Teks**: {len(text_input)} karakter")
            st.write(f"**Jumlah Kata**: {len(text_input.split())} kata")
            st.markdown("</div>", unsafe_allow_html=True)

# Halaman Tentang Pembuat
elif page == "Tentang Pembuat":
    st.markdown("<h1 class='title'>Tentang Pembuat</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Kenali tim di balik aplikasi Deteksi Hoax!</p>", unsafe_allow_html=True)

    # Informasi pembuat
    st.markdown("""
    ### Pembuat Program
    **Nama**: [Nama Kamu]  
    **Deskripsi**: Saya adalah seorang pengembang yang bersemangat menciptakan solusi teknologi untuk masalah dunia nyata.  
    **Kontak**: [email@example.com]  
    **GitHub**: [github.com/username]  

    Aplikasi ini dibuat untuk membantu masyarakat mengenali berita hoax dengan cepat dan mudah. Terima kasih telah menggunakan aplikasi ini!
    """)

    # Ekspander untuk info tambahan
    with st.expander("Visi dan Misi"):
        st.write("**Visi**: Menciptakan dunia yang bebas dari misinformasi.")
        st.write("**Misi**: Memberikan alat yang mudah digunakan untuk mendeteksi berita hoax.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7f8c8d;'>© 2025 Deteksi Hoax App. Dibuat dengan ❤️ menggunakan Streamlit.</p>", unsafe_allow_html=True)