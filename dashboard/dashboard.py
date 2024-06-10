# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

@st.cache_resource
def load_data():
    data = pd.read_csv("day.csv")
    return data


data = load_data()

# title
st.title("Bike Sharing")

st.sidebar.title("Dataset Bike Share")

with st.sidebar:
    # Menambahkan gambar
    st.image("https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/image1_hH9B4gs.jpg")
#dataset
if st.sidebar.checkbox("Dataset"):
    st.subheader("Data Bike Sharing")
    st.write(data)

# summary statistics
if st.sidebar.checkbox("Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# layout
col1, col2 = st.columns(2)

with col1:
    # Visualisasi Cuaca

    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit",
                               y="cnt", title="Penggunaan Sepeda berdasarkan cuaca")
    # Mengatur tinggi dan lebar gambar
    st.plotly_chart(fig_weather_count, use_container_width=True, height=400, width=800)

with col2:
    # Visualisasi Musim
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label",
                              y="cnt", title="Penggunaan Sepeda berdasarkan musim")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)






# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Menampilkan visualisasi dari penggunaan sepeda."
)

