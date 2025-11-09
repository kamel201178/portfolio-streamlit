import streamlit as st
from pathlib import Path
import base64

st.title("📊 Mes Projets")
st.write("""
Voici une sélection de projets illustrant mes compétences en **analyse de données**, **visualisation**, et **présentation de business cases**.  
Chaque projet combine une approche analytique et une restitution visuelle claire.
""")

# --- chemin vers le dossier assets ---
ASSETS_PATH = Path(__file__).parent.parent / "assets"

# --- Projet 1 : Business Case Power BI / Bicycle Horizon ---
st.subheader("🚴‍♂️ Business Case : Bicycle Horizon (Power BI)")
st.write("""
Analyse complète des performances commerciales d'une entreprise de distribution de vélos.  
L’objectif était de proposer des **indicateurs clés (KPI)** pour le suivi des ventes, des profits et du stock.  
Le travail a inclus la **préparation des données (Power Query)**, la **modélisation sous Power BI** et la **création d’un rapport interactif**.
""")

# Afficher les 4 captures du dashboard
cols = st.columns(2)
cols[0].image(str(ASSETS_PATH / "PB1_BC.png"), caption="Page 1 – Synthèse KPI", use_column_width=True)
cols[1].image(str(ASSETS_PATH / "PB2_BC.png"), caption="Page 2 – Détail ventes par région", use_column_width=True)
cols[0].image(str(ASSETS_PATH / "PB3_BC.png"), caption="Page 3 – Analyse produits", use_column_width=True)
cols[1].image(str(ASSETS_PATH / "PB4_BC.png"), caption="Page 4 – Performance commerciale", use_column_width=True)

# Lien de téléchargement du PDF du business case
pdf_path = ASSETS_PATH / "Business case Bicycle HORIZON.pdf"
if pdf_path.exists():
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
    st.download_button(
        label="📥 Télécharger le Business Case complet (PDF)",
        data=pdf_bytes,
        file_name=pdf_path.name,
        mime="application/pdf",
        use_container_width=True,
    )
else:
    st.warning("Le fichier PDF du business case n’a pas été trouvé.")

# --- Autres projets à venir ---
st.divider()
st.subheader("📈 Autres projets en développement")
st.write("""
- **Analyse de la satisfaction client** via données CRM et NLP  
- **Création d’un tableau de bord Streamlit interactif** (Python + Pandas)  
- **Automatisation de reporting mensuel** (Excel → Power BI → Email)
""")
