import streamlit as st

from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group

def main():
    page = page_group("p")

    with st.sidebar:
        st.title("Validez votre choix")

        with st.expander("RSA Application", True):
            page.item("Streamlit gallery", apps.gallery, default=True)

        with st.expander(" COMPONENTS", True):
            page.item("Génerer une clé", components.ace_editor)
            page.item("chiffrer le message", components.disqus)
            page.item("décchiffrer le message", components.elements)
            page.item("Pandas profiling", components.pandas_profiling)
            page.item("Quill editor", components.quill_editor)
            page.item("React player", components.react_player)

    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Gallery by Okld", page_icon="🎈", layout="wide")
    main()
