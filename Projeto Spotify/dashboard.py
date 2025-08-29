import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("/Users/imac/Documents/cursoPython/Projeto Spotify/top50.csv", encoding="latin-1")

st.title("🎵 Dashboard Spotify Top 50 em 2019")

# Mostrar lista de todas as músicas
st.subheader("Lista das músicas Top 50")
st.dataframe(df[["Track.Name", "Artist.Name", "Popularity", "Energy", "Danceability"]])

# Gráfico - Energia vs Dançabilidade
fig2 = px.scatter(df, x="Energy", y="Danceability",
                  size="Popularity", color="Artist.Name",
                  hover_data=["Track.Name"],
                  title="Energia vs Dançabilidade")
st.plotly_chart(fig2)
