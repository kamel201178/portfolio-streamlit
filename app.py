import streamlit as st

st.set_page_config(page_title="Mon Portfolio", page_icon="🎯", layout="centered")

st.sidebar.success("Navigation : choisissez une page 👇")

st.title("Bonjour, je suis Kamel Touchal")
st.subheader("Data / Projet")
st.write(
    "Bienvenue sur mon portfolio. "
    "Vous trouverez ici une sélection de projets, une courte bio et mon CV."
)

st.divider()

st.header("🧭 À propos")
st.write("""
Fort de plus de **15 ans d’expérience dans le secteur pharmaceutique**, j’ai bâti ma carrière au sein de la **supply chain internationale** en pilotant la **gestion des commandes export** et la **relation client** sur des marchés exigeants et réglementés.

Au fil de ces années, j’ai développé une forte culture du **service client**, du **suivi logistique** et de la **qualité des données** — des compétences clés pour garantir la fluidité des opérations dans un environnement complexe et à forte valeur ajoutée.

Porté par la curiosité et la volonté d’évoluer vers des métiers à impact analytique, j’ai choisi d’amorcer une **reconversion vers le domaine de la data**.  
Aujourd’hui, je me forme aux outils de la **data analyse et de la visualisation** (Python, SQL, Power BI, Streamlit, etc.) avec l’objectif de transformer les données en leviers d’aide à la décision et d’amélioration continue.

Cette transition est pour moi une continuité logique : passer de la maîtrise des flux physiques à la **maîtrise des flux d’information**, au service de la performance et de la stratégie.
""")



st.divider()

st.header("📌 Projets (aperçu)")
cols = st.columns(3)
with cols[0]:
    st.markdown("**Projet 1**  \nAnalyse des ventes — Python/SQL")
with cols[1]:
    st.markdown("**Projet 2**  \nDashboard — Streamlit/Power BI")
with cols[2]:
    st.markdown("**Projet 3**  \nClassification — scikit-learn")

st.divider()

st.header("📬 Contact")
st.write("✉️ kameltouchal@yahoo.fr · 🔗 LinkedIn · 💻 GitHub")
