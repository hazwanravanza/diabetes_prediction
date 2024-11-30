import streamlit as st
import plotly.express as px

def main(navigate_to):
    st.title("Analisis Grafik Interaktif")

    # Check if Data Exists
    if "user_data" in st.session_state and not st.session_state.user_data.empty:
        df = st.session_state.user_data

        # Grafik BMI vs Diabetes
        st.subheader("BMI vs Diabetes")
        fig = px.scatter(
            df, x="BMI", y="Diabetes", 
            color="Diabetes", 
            title="Hubungan BMI dengan Risiko Diabetes",
            labels={"Diabetes": "Risiko Diabetes (0=Rendah, 1=Tinggi)"}
        )
        st.plotly_chart(fig)

        # Grafik General Health vs Diabetes
        st.subheader("General Health vs Diabetes")
        fig = px.histogram(
            df, x="GeneralHealth", color="Diabetes", 
            barmode="group", 
            title="Distribusi Kesehatan Umum dan Risiko Diabetes",
            labels={"GeneralHealth": "Kesehatan Umum (1=Excellent, 5=Poor)"}
        )
        st.plotly_chart(fig)

        # Grafik Aktivitas Fisik
        st.subheader("Aktivitas Fisik dan Risiko Diabetes")
        fig = px.bar(
            df.groupby("PhysicalActivity")["Diabetes"].mean().reset_index(),
            x="PhysicalActivity", y="Diabetes",
            title="Rata-rata Risiko Diabetes Berdasarkan Aktivitas Fisik",
            labels={"PhysicalActivity": "Aktivitas Fisik (0=Tidak, 1=Ya)", "Diabetes": "Rata-rata Risiko Diabetes"}
        )
        st.plotly_chart(fig)

        if st.button("Kembali ke Halaman Awal"):
            navigate_to("Halaman Awal")

    else:
        st.warning("Belum ada data input dari pengguna. Silakan tambahkan data di halaman 'Input Data & Prediksi'.")
