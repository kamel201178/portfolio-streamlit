import streamlit as st
import base64
from pathlib import Path
from urllib.parse import quote

st.title("📘 Livret de Compétences")

st.write("""
Ce livret de compétences présente l’ensemble des savoir-faire que j’ai développés tout au long de ma carrière
et lors de ma reconversion dans la **data analyse**.  
Il illustre mes compétences techniques (Python, SQL, Power BI, Streamlit) ainsi que mes aptitudes métier
en **gestion de projet**, **analyse opérationnelle** et **communication professionnelle**.
""")

# --- chemin du PDF ---
PDF_PATH = Path(__file__).parent.parent / "assets" / "Livret_de_competences.pdf"

if PDF_PATH.exists():
    with open(PDF_PATH, "rb") as f:
        pdf_bytes = f.read()

    # --- Bouton de téléchargement ---
    st.download_button(
        label="📥 Télécharger le livret complet (PDF)",
        data=pdf_bytes,
        file_name=PDF_PATH.name,
        mime="application/pdf",
        use_container_width=True,
    )

    # --- Affichage intégré du PDF ---
    raw_url = "https://raw.githubusercontent.com/kamel201178/portfolio-streamlit/main/assets/Livret_de_competences.pdf"
    viewer_url = f"https://mozilla.github.io/pdf.js/web/viewer.html?file={quote(raw_url, safe='')}"
    st.components.v1.iframe(viewer_url, height=900)
else:
    st.error("⚠️ Le fichier PDF du livret de compétences n’a pas été trouvé. Vérifie qu’il est bien dans le dossier `assets/`.")
