import streamlit as st

def main(navigate_to):
    st.title("Aplikasi Prediksi Diabetes")
    st.header("Halaman Awal")

    st.write("""
    Selamat datang di aplikasi prediksi diabetes. Ikuti langkah-langkah berikut:
    1. Isi nama dan umur Anda pada halaman ini.
    2. Klik tombol **Next** untuk melanjutkan ke pengisian data kesehatan.
    3. Hasil prediksi akan ditampilkan di halaman terakhir bersama grafik analisis.
    """)

    # Input nama dan umur
    nama = st.text_input("Masukkan Nama Anda:")
    umur = st.number_input("Masukkan Umur Anda:", min_value=0, max_value=120, step=1)

    # Tombol Next untuk ke halaman berikutnya
    if st.button("Next"):
        if nama and umur:
            navigate_to("Input Data")
            st.session_state["nama"] = nama
            st.session_state["umur"] = umur
        else:
            st.error("Harap isi semua kolom sebelum melanjutkan.")
