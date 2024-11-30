import streamlit as st

# Set konfigurasi aplikasi
st.set_page_config(
    page_title="Aplikasi Prediksi Diabetes",
    page_icon="🩺",
    layout="centered",
)

# Menyimpan informasi halaman saat ini di session state
if "current_page" not in st.session_state:
    st.session_state.current_page = "Halaman Awal"

# Fungsi untuk navigasi antar halaman
def navigate_to(page_name):
    st.session_state.current_page = page_name

# Mengatur halaman berdasarkan session state
if st.session_state.current_page == "Halaman Awal":
    from pages.halaman_awal import main as halaman_awal
    halaman_awal(navigate_to)
elif st.session_state.current_page == "Input Data":
    from pages.input_data import main as input_data
    input_data(navigate_to)
elif st.session_state.current_page == "Hasil Analisis":
    from pages.hasil_analisis import main as hasil_analisis
    hasil_analisis(navigate_to)
