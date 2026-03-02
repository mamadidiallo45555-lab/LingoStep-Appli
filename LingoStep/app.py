import streamlit as st

# --- 1. CONFIGURATION DE L'APPARENCE (Design Épuré) ---
st.set_page_config(
    page_title="LingoStep - Apprendre par étapes",
    page_icon="🚀",
    layout="centered"
)

# Style CSS personnalisé pour un look plus professionnel
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BARRE LATÉRALE (Navigation) ---
with st.sidebar:
    st.title("🌐 LingoStep")
    st.write("---")
    st.info("Votre mois gratuit est activé ! ✅")
    st.progress(0, text="Progression totale : 0%")

# --- 3. CONTENU PRINCIPAL ---
st.title("Bienvenue sur LingoStep")
st.write("L'apprentissage des langues, une étape à la fois.")

# Création du formulaire d'onboarding
with st.container(border=True):
    st.subheader("Configuration de votre profil")
    
    with st.form("onboarding_lingostep"):
        # Choix de la langue
        langue = st.selectbox(
            "Quelle langue souhaitez-vous maîtriser ?",
            ("Anglais", "Français", "Arabe"),
            index=None,
            placeholder="Choisissez une langue..."
        )
        
        # Objectif quotidien
        temps = st.select_slider(
            "Combien de temps pouvez-vous y consacrer par jour ?",
            options=["5 min", "15 min", "30 min"],
            value="15 min"
        )
        
        # Niveau de départ
        niveau = st.radio(
            "Quel est votre niveau actuel ?",
            ["Débutant (A1/A2)", "Intermédiaire (B1/B2)", "Avancé (C1/C2)"],
            horizontal=True
        )

        # Bouton de validation
        submit = st.form_submit_button("Créer mon parcours personnalisé")

# --- 4. LOGIQUE DE VALIDATION ---
if submit:
    if langue is None:
        st.warning("Veuillez choisir une langue pour continuer.")
    else:
        st.success(f"Félicitations ! Votre programme de **{langue}** ({niveau}) est en cours de création.")
        st.balloons()
        
        # Message sur la période d'essai
        st.info(f"Objectif : **{temps}** par jour. Profitez de vos 30 jours gratuits !")