import streamlit as st
import base64
from pathlib import Path

st.title("📄 Mon CV")

# --- chemin du PDF ---
PDF_PATH = Path(__file__).parent.parent / "assets" / "CV_Kamel_Touchal.pdf"

if PDF_PATH.exists():
    with open(PDF_PATH, "rb") as f:
        pdf_bytes = f.read()

    # Bouton de téléchargement
    st.download_button(
        label="📥 Télécharger mon CV (PDF)",
        data=pdf_bytes,
        file_name=PDF_PATH.name,
        mime="application/pdf",
        use_container_width=True,
    )

        # Affichage via Google Docs Viewer (compatible Cloud)
    from urllib.parse import quote

    RAW_URL = "https://raw.githubusercontent.com/kamel201178/portfolio-streamlit/main/assets/CV_Kamel_Touchal.pdf"
    viewer_url = f"https://docs.google.com/gview?embedded=1&url={quote(RAW_URL, safe=':/')}"
    st.components.v1.iframe(viewer_url, height=900)

