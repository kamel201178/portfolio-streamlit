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

    # Affichage intégré du PDF
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
    pdf_viewer = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_viewer, unsafe_allow_html=True)
else:
    st.error("⚠️ Le fichier PDF n’a pas été trouvé. Vérifie qu’il est bien dans le dossier `assets/`.")
