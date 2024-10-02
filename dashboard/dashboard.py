import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


@st.cache_data
def load_data():
    df_all_clean = pd.read_csv("dashboard/clean_merged_dataset.csv")
    df_Aotizhongxin = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Aotizhongxin_20130301-20170228.csv"
    )
    df_Changping = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Changping_20130301-20170228.csv"
    )
    df_Dingling = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Dingling_20130301-20170228.csv"
    )
    df_Dongsi = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Dongsi_20130301-20170228.csv"
    )
    df_Guanyuan = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Guanyuan_20130301-20170228.csv"
    )
    df_Gucheng = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Gucheng_20130301-20170228.csv"
    )
    df_Huairou = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Huairou_20130301-20170228.csv"
    )
    df_Nongzhanguan = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Nongzhanguan_20130301-20170228.csv"
    )
    df_Shunyi = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Shunyi_20130301-20170228.csv"
    )
    df_Tiantan = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Tiantan_20130301-20170228.csv"
    )
    df_Wanliu = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Wanliu_20130301-20170228.csv"
    )
    df_Wanshouxigong = pd.read_csv(
        "../air-quality-dataset/PRSA_Data_Wanshouxigong_20130301-20170228.csv"
    )

    df_all_clean["date_time"] = pd.to_datetime(df_all_clean["date_time"])

    return (
        df_all_clean,
        df_Aotizhongxin,
        df_Changping,
        df_Dingling,
        df_Dongsi,
        df_Guanyuan,
        df_Gucheng,
        df_Huairou,
        df_Nongzhanguan,
        df_Shunyi,
        df_Tiantan,
        df_Wanliu,
        df_Wanshouxigong,
    )


(
    df_all_clean,
    df_Aotizhongxin,
    df_Changping,
    df_Dingling,
    df_Dongsi,
    df_Guanyuan,
    df_Gucheng,
    df_Huairou,
    df_Nongzhanguan,
    df_Shunyi,
    df_Tiantan,
    df_Wanliu,
    df_Wanshouxigong,
) = load_data()

st.sidebar.image("images/air-quality.png")
st.sidebar.title("Air Quality Index")
menu = st.sidebar.selectbox(
    "Pilih Menu:",
    [
        "Home",
        "Show Dataset",
        "Pertanyaan 1",
        "Pertanyaan 2",
        "Pertanyaan 3",
        "Conclusion",
    ],
)

wilayah_dict = {
    "Aotizhongxin": df_Aotizhongxin,
    "Changping": df_Changping,
    "Dingling": df_Dingling,
    "Dongsi": df_Dongsi,
    "Guanyuan": df_Guanyuan,
    "Gucheng": df_Gucheng,
    "Huairou": df_Huairou,
    "Nongzhanguan": df_Nongzhanguan,
    "Shunyi": df_Shunyi,
    "Tiantan": df_Tiantan,
    "Wanliu": df_Wanliu,
    "Wanshouxigong": df_Wanshouxigong,
}

if menu == "Home":
    st.title("Air Quality Dataset")
    st.markdown(
        """
        Copyright @ 2023 Annas Sovianto | Email: annasstdntyouth@gmail.com\n
    Air quality atau kualitas udara adalah ukuran seberapa bersih atau tercemarnya udara di suatu lingkungan. Kualitas udara dipengaruhi oleh jumlah polutan atau zat berbahaya yang ada di atmosfer, seperti partikel debu, asap, gas beracun (misalnya karbon monoksida, sulfur dioksida), dan zat kimia lainnya. Kualitas udara yang buruk dapat berdampak negatif terhadap kesehatan manusia, lingkungan, dan ekosistem. Pengukuran kualitas udara sering dilakukan melalui Air Quality Index (AQI) yang memberi nilai untuk menunjukkan tingkat polusi udara, dengan kategori mulai dari baik hingga sangat berbahaya.
        """
    )
    st.subheader("Deskripsi Data")
    st.write(df_all_clean.describe())
    st.subheader("Head of Clean Dataframe")
    st.dataframe(df_all_clean.head())
elif menu == "Show Dataset":
    st.title("Air Quality Dataset berdasarkan Wilayah di Beijing, China.")

    selected_wilayah = st.sidebar.selectbox("Pilih Wilayah:", list(wilayah_dict.keys()))

    st.subheader(f"Wilayah: {selected_wilayah}")
    st.subheader("Deskripsi Data")
    st.write(wilayah_dict[selected_wilayah].describe())
    st.subheader(f"Head of {selected_wilayah}")
    st.dataframe(wilayah_dict[selected_wilayah].head())
elif menu == "Pertanyaan 1":
    st.title(
        "Bagaimana perbandingan rata-rata tingkat PM2.5 dan PM10 di berbagai kota dan kota mana yang memiliki tingkat polusi tertinggi dan terendah?"
    )

    # Mengonversi kolom date_time menjadi datetime
    df_all_clean["date_time"] = pd.to_datetime(df_all_clean["date_time"])

    # Menghitung rata-rata PM2.5 dan PM10 untuk setiap kota
    rata_rata_pm25 = df_all_clean.groupby("station")["PM2.5"].mean()
    rata_rata_pm10 = df_all_clean.groupby("station")["PM10"].mean()

    # Membuat DataFrame baru untuk perbandingan
    rata_rata = pd.DataFrame({"PM2.5": rata_rata_pm25, "PM10": rata_rata_pm10})
    rata_rata = rata_rata.sort_values(by="PM2.5", ascending=False)

    # Plotting
    plt.figure(figsize=(15, 10))
    rata_rata.plot(kind="bar", alpha=0.7)
    plt.title("Rata-rata Tingkat PM2.5 dan PM10 di Setiap Kota")
    plt.xlabel("Kota")
    plt.ylabel("Rata-rata Tingkat (µg/m³)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.legend(title="Jenis Partikel")

    # Tampilkan plot di Streamlit
    st.pyplot(plt)

    # Mendapatkan kota dengan PM2.5 dan PM10 tertinggi dan terendah
    kota_pm25_tertinggi = rata_rata_pm25.idxmax()
    kota_pm25_terendah = rata_rata_pm25.idxmin()
    kota_pm10_tertinggi = rata_rata_pm10.idxmax()
    kota_pm10_terendah = rata_rata_pm10.idxmin()

    st.write(
        f"Kota dengan rata-rata tingkat PM2.5 tertinggi adalah {kota_pm25_tertinggi}"
    )
    st.write(
        f"Kota dengan rata-rata tingkat PM2.5 terendah adalah {kota_pm25_terendah}"
    )
    st.write(
        f"Kota dengan rata-rata tingkat PM10 tertinggi adalah {kota_pm10_tertinggi}"
    )
    st.write(f"Kota dengan rata-rata tingkat PM10 terendah adalah {kota_pm10_terendah}")

    # Insight/Kesimpulan
    st.subheader("Insight Grafik:")
    st.markdown(
        f"""
    Berdasarkan data yang ditampilkan, terlihat bahwa **{kota_pm25_tertinggi}** memiliki rata-rata tingkat PM2.5 tertinggi, 
    menunjukkan tingkat polusi udara yang berpotensi berbahaya di wilayah tersebut. Sementara itu, **{kota_pm25_terendah}** memiliki tingkat PM2.5 terendah, 
    yang mengindikasikan kualitas udara yang lebih bersih dibanding kota lainnya. 

    Untuk PM10, **{kota_pm10_tertinggi}** menunjukkan rata-rata tingkat yang paling tinggi, yang juga dapat mengindikasikan masalah kesehatan akibat partikel halus yang lebih besar, 
    yang dapat terhirup dan berkontribusi pada masalah pernapasan. Sebaliknya, **{kota_pm10_terendah}** menunjukkan kualitas udara yang lebih baik dengan tingkat PM10 yang rendah. 

    Faktor geografis, aktivitas industri, serta kebijakan pengendalian polusi di masing-masing kota mungkin berkontribusi terhadap perbedaan tingkat polusi yang terlihat.
    """
    )

elif menu == "Pertanyaan 2":
    st.title(
        "Bagaimana tren tahunan tingkat rata-rata SO2 di berbagai kota dari 2013 hingga 2017 dan apakah ada pola umum yang terlihat?"
    )

    # Mengonversi kolom date_time menjadi datetime
    df_all_clean["date_time"] = pd.to_datetime(df_all_clean["date_time"])

    # Menghitung rata-rata SO2 per tahun untuk setiap kota
    yearly_so2 = (
        df_all_clean.groupby([df_all_clean["date_time"].dt.year, "station"])["SO2"]
        .mean()
        .unstack()
    )

    # Plotting
    plt.figure(figsize=(15, 10))
    yearly_so2.plot(marker="o")
    plt.title("Rata-rata Tingkat SO2 per Tahun untuk Setiap Kota")
    plt.xlabel("Tahun")
    plt.ylabel("Rata-rata Tingkat SO2 (µg/m³)")
    plt.xticks(yearly_so2.index.astype(int), rotation=45)
    plt.legend(title="Kota", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    # Tampilkan plot di Streamlit
    st.pyplot(plt)

    # Menghitung perubahan keseluruhan tingkat SO2 untuk setiap kota
    for city in yearly_so2.columns:
        total_change = yearly_so2[city].iloc[-1] - yearly_so2[city].iloc[0]
        st.write(
            f"Perubahan keseluruhan tingkat SO2 untuk {city} dari {yearly_so2.index[0]} ke {yearly_so2.index[-1]}: {total_change:.2f}"
        )

    # Insight/Kesimpulan
    st.subheader("Insight:")
    st.markdown(
        """
    Dari tren yang terlihat pada tingkat SO2 di berbagai kota dari tahun 2013 hingga 2017, ada penurunan signifikan di sebagian besar kota, 
    menunjukkan peningkatan dalam pengelolaan kualitas udara. Kota-kota yang menunjukkan penurunan terbesar mungkin telah mengambil 
    langkah-langkah lebih agresif dalam mengurangi emisi yang mengandung sulfur. Namun, beberapa kota menunjukkan tren yang stagnan atau bahkan peningkatan, 
    yang bisa menjadi sinyal perlunya intervensi lebih lanjut.
    """
    )

elif menu == "Pertanyaan 3":
    st.title(
        "Bagaimana pola musiman tingkat NO2 di berbagai kota, fluktuasi tertinggi, serta tingkatan NO2 terkotor dan terbersih antar musim di Negara Beijing, China?"
    )

    # Mengonversi kolom date_time menjadi datetime
    df_all_clean["date_time"] = pd.to_datetime(df_all_clean["date_time"])

    # Menambahkan kolom musim berdasarkan bulan
    def get_season(month):
        if month in [3, 4, 5]:
            return "Musim Semi"
        elif month in [6, 7, 8]:
            return "Musim Panas"
        elif month in [9, 10, 11]:
            return "Musim Gugur"
        else:
            return "Musim Dingin"

    df_all_clean["musim"] = df_all_clean["date_time"].dt.month.map(get_season)

    # Menghitung rata-rata NO2 berdasarkan musim dan kota
    rata_rata_musim_no2 = (
        df_all_clean.groupby(["station", "musim"])["NO2"].mean().unstack()
    )

    # Plotting heatmap
    plt.figure(figsize=(14, 8))
    sns.heatmap(rata_rata_musim_no2, annot=True, fmt=".1f", cmap="YlOrRd")
    plt.title("Rata-rata Tingkat NO2 Berdasarkan Musim dan Kota di Beijing, China")
    plt.ylabel("Kota")
    plt.tight_layout()

    # Tampilkan plot di Streamlit
    st.pyplot(plt)

    # Menghitung variasi musiman untuk setiap kota
    variasi_musim = rata_rata_musim_no2.max(axis=1) - rata_rata_musim_no2.min(axis=1)
    kota_variasi_terbesar = variasi_musim.idxmax()

    # Menghitung rata-rata NO2 untuk setiap kota
    rata_rata_no2 = df_all_clean.groupby("station")["NO2"].mean()
    kota_paling_kotor = rata_rata_no2.idxmax()
    kota_paling_bersih = rata_rata_no2.idxmin()

    st.write(f"Kota dengan variasi musiman NO2 terbesar: {kota_variasi_terbesar}")
    st.write(f"Kota dengan tingkat NO2 paling kotor: {kota_paling_kotor}")
    st.write(f"Kota dengan tingkat NO2 paling bersih: {kota_paling_bersih}")

    # Insight/Kesimpulan
    st.subheader("Insight:")
    st.markdown(
        f"""
    **{kota_variasi_terbesar}** mengalami fluktuasi NO2 musiman yang paling signifikan, yang menunjukkan perubahan besar antara musim panas dan musim dingin. 
    Ini kemungkinan berkaitan dengan peningkatan konsumsi bahan bakar untuk pemanasan di musim dingin dan penggunaan kendaraan bermotor yang lebih sedikit di musim panas. 
    Selain itu, musim gugur dan musim semi menunjukkan tingkat NO2 yang lebih stabil, mungkin karena aktivitas manusia yang lebih seimbang sepanjang tahun.

    Berdasarkan rata-rata tingkat NO2, **{kota_paling_kotor}** menunjukkan kualitas udara yang buruk, berpotensi membahayakan kesehatan masyarakat. Sementara itu, **{kota_paling_bersih}** memiliki tingkat NO2 yang lebih rendah, mencerminkan kualitas udara yang lebih baik. 
    Upaya pengendalian polusi dan pengelolaan transportasi di kota-kota ini mungkin dapat menjelaskan perbedaan yang ada.
    """
    )

elif menu == "Conclusion":
    st.title("Kesimpulan Analisis Kualitas Udara (Air Quality)")

    st.subheader("1. Pertanyaan 1: Rata-rata Tingkat PM2.5 dan PM10")
    st.write(
        """
        - Kota dengan rata-rata tingkat PM2.5 tertinggi adalah **Dongsi**.
        - Kota dengan rata-rata tingkat PM2.5 terendah adalah **Dingling**.
        - Kota dengan rata-rata tingkat PM10 tertinggi adalah **Gucheng**.
        - Kota dengan rata-rata tingkat PM10 terendah adalah **Dingling**.

        **Insight Grafik:**
        Berdasarkan data yang ditampilkan, terlihat bahwa **Dongsi** memiliki rata-rata tingkat PM2.5 tertinggi, menunjukkan tingkat polusi udara yang berpotensi berbahaya di wilayah tersebut. 
        Sementara itu, **Dingling** memiliki tingkat PM2.5 terendah, yang mengindikasikan kualitas udara yang lebih bersih dibanding kota lainnya. 
        
        Untuk PM10, **Gucheng** menunjukkan rata-rata tingkat yang paling tinggi, yang juga dapat mengindikasikan masalah kesehatan akibat partikel halus yang lebih besar, 
        yang dapat terhirup dan berkontribusi pada masalah pernapasan. Sebaliknya, **Dingling** menunjukkan kualitas udara yang lebih baik dengan tingkat PM10 yang rendah.
        
        Faktor geografis, aktivitas industri, serta kebijakan pengendalian polusi di masing-masing kota mungkin berkontribusi terhadap perbedaan tingkat polusi yang terlihat.
        """
    )

    st.subheader("2. Pertanyaan 2: Perubahan Tingkat SO2 dari 2013 ke 2017")
    st.write(
        """
        - Perubahan keseluruhan tingkat SO2 untuk Aotizhongxin dari 2013 ke 2017: **-1.55**
        - Perubahan keseluruhan tingkat SO2 untuk Changping dari 2013 ke 2017: **-1.55**
        - Perubahan keseluruhan tingkat SO2 untuk Dingling dari 2013 ke 2017: **0.42**
        - Perubahan keseluruhan tingkat SO2 untuk Dongsi dari 2013 ke 2017: **-2.48**
        - Perubahan keseluruhan tingkat SO2 untuk Guanyuan dari 2013 ke 2017: **-0.36**
        - Perubahan keseluruhan tingkat SO2 untuk Gucheng dari 2013 ke 2017: **3.32**
        - Perubahan keseluruhan tingkat SO2 untuk Huairou dari 2013 ke 2017: **-4.97**
        - Perubahan keseluruhan tingkat SO2 untuk Nongzhanguan dari 2013 ke 2017: **-1.60**
        - Perubahan keseluruhan tingkat SO2 untuk Shunyi dari 2013 ke 2017: **5.73**
        - Perubahan keseluruhan tingkat SO2 untuk Tiantan dari 2013 ke 2017: **-2.77**
        - Perubahan keseluruhan tingkat SO2 untuk Wanliu dari 2013 ke 2017: **-2.50**
        - Perubahan keseluruhan tingkat SO2 untuk Wanshouxigong dari 2013 ke 2017: **-1.80**

        **Insight:**
        Analisis perubahan tingkat SO2 dari tahun 2013 hingga 2017 menunjukkan adanya penurunan yang signifikan di sebagian besar kota, mengindikasikan adanya perbaikan dalam pengelolaan kualitas udara.

        Kota dengan penurunan tertinggi:
        Huairou: -4.97
        Dongsi: -2.48
        Wanliu: -2.50
        Kota-kota ini mungkin telah menerapkan kebijakan lebih ketat untuk mengurangi emisi sulfur.
        Kota dengan peningkatan:

        Gucheng: +3.32
        Shunyi: +5.73
        Dingling: +0.42
        Kenaikan di Gucheng dan Shunyi menunjukkan perlunya tindakan lebih lanjut untuk mengatasi masalah polusi di daerah ini.
        """
    )

    st.subheader("3. Pertanyaan 3: Pola Musiman Tingkat NO2")
    st.write(
        """
        - Kota dengan variasi musiman NO2 terbesar: **Changping**
        - Kota dengan tingkat NO2 paling kotor: **Wanliu**
        - Kota dengan tingkat NO2 paling bersih: **Dingling**

        **Insight:**
        **Changping** mengalami fluktuasi NO2 musiman yang paling signifikan, yang menunjukkan perubahan besar antara musim panas dan musim dingin. 
        Ini kemungkinan berkaitan dengan peningkatan konsumsi bahan bakar untuk pemanasan di musim dingin dan penggunaan kendaraan bermotor yang lebih sedikit di musim panas. 
        Selain itu, musim gugur dan musim semi menunjukkan tingkat NO2 yang lebih stabil, mungkin karena aktivitas manusia yang lebih seimbang sepanjang tahun.

        Berdasarkan rata-rata tingkat NO2, **Wanliu** menunjukkan kualitas udara yang buruk, berpotensi membahayakan kesehatan masyarakat. 
        Sementara itu, **Dingling** memiliki tingkat NO2 yang lebih rendah, mencerminkan kualitas udara yang lebih baik. 
        Upaya pengendalian polusi dan pengelolaan transportasi di kota-kota ini mungkin dapat menjelaskan perbedaan yang ada.
        """
    )
