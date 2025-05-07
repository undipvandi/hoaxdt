import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Interaktif",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styling CSS untuk tampilan menarik
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    .metric-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk membuat data dummy
@st.cache_data
def load_data():
    np.random.seed(42)
    data = {
        'Tanggal': pd.date_range(start='2025-01-01', periods=100, freq='D'),
        'Penjualan': np.random.randint(50, 200, 100),
        'Kategori': np.random.choice(['A', 'B', 'C'], 100)
    }
    return pd.DataFrame(data)

# Load data
df = load_data()

# Sidebar untuk navigasi tab
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Dashboard", "Testing", "Tentang"])

# Halaman Dashboard
if page == "Dashboard":
    st.title("📈 Dashboard Interaktif")
    st.markdown("Selamat datang di dashboard interaktif! Visualisasi data secara real-time.")

    # Layout kolom untuk metrik
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label="Total Penjualan", value=f"{df['Penjualan'].sum():,}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label="Rata-rata Penjualan", value=f"{int(df['Penjualan'].mean())}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label="Kategori Unik", value=f"{df['Kategori'].nunique()}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Filter interaktif
    st.subheader("Filter Data")
    kategori = st.multiselect("Pilih Kategori:", options=df['Kategori'].unique(), default=df['Kategori'].unique())
    filtered_df = df[df['Kategori'].isin(kategori)]

    # Visualisasi
    st.subheader("Visualisasi Penjualan")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.line(filtered_df, x='Tanggal', y='Penjualan', title="Tren Penjualan", color='Kategori')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.histogram(filtered_df, x='Penjualan', color='Kategori', title="Distribusi Penjualan")
        st.plotly_chart(fig, use_container_width=True)

# Halaman Testing
elif page == "Testing":
    st.title("🧪 Halaman Testing")
    st.markdown("Halaman ini digunakan untuk menguji fitur atau fungsi baru.")

    # Contoh input interaktif
    st.subheader("Uji Input Data")
    user_input = st.text_input("Masukkan teks untuk diuji:", "Contoh Teks")
    if st.button("Proses"):
        st.write(f"Anda memasukkan: **{user_input}**")
    
    # Contoh visualisasi testing
    st.subheader("Grafik Tes")
    test_data = pd.DataFrame({
        'x': range(10),
        'y': np.random.randn(10)
    })
    fig = px.scatter(test_data, x='x', y='y', title="Scatter Plot Tes")
    st.plotly_chart(fig, use_container_width=True)

# Halaman Tentang
else:
    st.title("ℹ️ Tentang")
    st.markdown("""
    ### Tentang Dashboard Ini
    Dashboard ini dibuat menggunakan **Streamlit**, sebuah framework open-source untuk membangun aplikasi web interaktif dengan Python.
    
    **Fitur Utama:**
    - Visualisasi data interaktif menggunakan Plotly.
    - Navigasi mudah melalui sidebar dengan tab Dashboard, Testing, dan Tentang.
    - Desain responsif yang dioptimalkan untuk Streamlit Cloud.
    
    **Tujuan:**
    Dashboard ini dirancang untuk menampilkan data secara menarik, memungkinkan pengujian fitur baru, dan memberikan informasi tentang aplikasi.
    
    **Kontak:**
    Dibuat oleh [Nama Anda]. Untuk pertanyaan, hubungi [email@contoh.com](mailto:email@contoh.com).
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 Dashboard Interaktif. Dibuat dengan Streamlit.")