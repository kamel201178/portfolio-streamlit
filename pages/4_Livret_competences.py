import streamlit as st
from urllib.parse import quote

st.title("📘 Livret de compétences")

st.write("""
Ce livret de compétences présente l’ensemble des savoir-faire que j’ai développés tout au long de ma carrière et lors de ma reconversion dans la **data analyse**.  
Il illustre mes compétences techniques (**Python, SQL, Power BI, Streamlit**) ainsi que mes aptitudes métier en **gestion de projet**, **analyse opérationnelle** et **communication professionnelle**.
""")

# URL directe vers ton PDF hébergé sur GitHub (format "raw")
RAW_URL = "https://raw.githubusercontent.com/kamel201178/portfolio-streamlit/main/assets/livret_de_competences.pdf"

# Affiche le bouton de téléchargement
st.link_button("📥 Télécharger le livret complet (PDF)", RAW_URL, use_container_width=True)

# Affiche le PDF via le lecteur PDF.js
viewer_url = f"https://mozilla.github.io/pdf.js/web/viewer.html?file={quote(RAW_URL, safe='')}"
st.components.v1.iframe(viewer_url, height=900)
