import streamlit as st
import pandas as pd

st.set_page_config(page_title="Knjige – dashboard", layout="wide")

st.title("📚 Dashboard knjiga")

najskuplje = [
    ("The Death of Humanity; and the Case for Life", 58.11),
    ("Slow States of Collapse: Poems", 57.31),
    ("Our Band Could Be Your Life: Scenes...", 57.25),
    ("The Past Never Ends", 56.50),
    ("The Pioneer Woman Cooks: Dinner...", 56.41),
    ("The Secret of Dreadwillow Carse", 56.13),
    ("The Electric Pencil: Drawings...", 56.06),
    ("Birdsong: A Story in Pictures", 54.64),
]

najjeftinije = [
    ("In Her Wake", 12.84),
    ("Starving Hearts (Triangular Trade Trilogy, #1)", 13.99),
    ("Untitled Collection: Sabbath Poems 2014", 14.27),
    ("Sophie's World", 15.94),
    ("Tsubasa: WoRLD CHRoNiCLE 2", 16.28),
    ("The Life-Changing Magic of Tidying Up", 16.77),
    ("Thirst", 17.27),
    ("Set Me Free", 17.46),
]

prosjek = 35.708375

df_skupe = pd.DataFrame(najskuplje, columns=["naslov", "cijena"])
df_jeftine = pd.DataFrame(najjeftinije, columns=["naslov", "cijena"])

col1, col2, col3 = st.columns(3)
col1.metric("Prosječna cijena", f"{prosjek:.2f} €")
col2.metric("Najskuplja knjiga", f"{df_skupe['cijena'].max():.2f} €")
col3.metric("Najjeftinija knjiga", f"{df_jeftine['cijena'].min():.2f} €")

st.markdown("---")

left, right = st.columns(2)

with left:
    st.subheader("Top 8 najskupljih knjiga")
    st.dataframe(df_skupe, use_container_width=True)
    st.bar_chart(df_skupe.set_index("naslov")["cijena"])

with right:
    st.subheader("Top 8 najjeftinijih knjiga")
    st.dataframe(df_jeftine, use_container_width=True)
    st.bar_chart(df_jeftine.set_index("naslov")["cijena"])
