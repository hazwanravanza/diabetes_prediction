import streamlit as st

def main(navigate_to):
    st.title("Input Data Kesehatan")
    st.header(f"Selamat datang, {st.session_state.get('nama', 'Pengguna')}!")
    st.write("Silakan isi data kesehatan berikut untuk memprediksi risiko diabetes:")

    # Form untuk input data
    with st.form("data_form"):
        bmi = st.number_input("Body Mass Index (BMI):", format="%.2f")
        smoker = st.selectbox("Apakah Anda Merokok?", ("Tidak", "Ya"))
        stroke = st.selectbox("Apakah Anda Pernah Stroke?", ("Tidak", "Ya"))
        activity = st.selectbox("Apakah Anda Aktif Berolahraga dalam Sebulan Terakhir?", ("Tidak", "Ya"))
        fruit = st.selectbox("Apakah Anda Mengonsumsi Buah Setiap Hari?", ("Tidak", "Ya"))
        vegetable = st.selectbox("Apakah Anda Mengonsumsi Sayur Setiap Hari?", ("Tidak", "Ya"))
        alcohol = st.selectbox("Apakah Anda Mengonsumsi Alkohol?", ("Tidak", "Ya"))
        general_health = st.slider("Kesehatan Umum Anda (1 = Excellent, 5 = Poor):", 1, 5)
        Diffwalk = st.selectbox("Apakah Anda Memiliki Masalah dalam Kesulitan Berjalan atau Menaiki Tangga?", ("Tidak", "Ya"))


        submitted = st.form_submit_button("Next")

        if submitted:
            st.session_state["data"] = {
                "BMI": bmi,
                "Smoker": 1 if smoker == "Ya" else 0,
                "Stroke": 1 if stroke == "Ya" else 0,
                "PhysActivity": 1 if activity == "Ya" else 0,
                "Fruits": 1 if fruit == "Ya" else 0,
                "Veggies": 1 if vegetable == "Ya" else 0,
                "HvyAlcoholConsump": 1 if alcohol == "Ya" else 0,
                "GenHlth": general_health,
                "DiffWalk": 1 if Diffwalk == "Ya" else 0
            }
            navigate_to("Hasil Analisis")
