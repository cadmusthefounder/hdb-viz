import streamlit as st

from hdb_viz.constants import Page
from hdb_viz.settings import Settings
from hdb_viz.views import upload_dataset, upload_dataset_2, visualize_dataset


def set_default_session_state(settings: Settings):
    st.session_state["current_page"] = settings.default_page.value


# def change_page():
#     st.write(st.session_state.selected_page)
#     st.session_state["current_page"] = st.session_state.selected_page


def main():
    st.set_page_config(
        page_title="HDB Visualization",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://www.google.com.sg",
            "About": "# Visualize HDB resale flat prices!",
        },
    )
    settings = Settings()

    if "initialized" not in st.session_state or not st.session_state["initialized"]:
        set_default_session_state(settings)
        st.session_state["initialized"] = True

    selected_page = st.sidebar.selectbox(
        "Action",
        [p.value for p in Page],
        help="Navigate to desired page.",
        key="selected_page",
    )

    if Page(selected_page) is Page.UPLOAD_DATASET:
        upload_dataset.load_content(settings)
    elif Page(selected_page) is Page.UPLOAD_DATASET_2:
        upload_dataset_2.load_content(settings)
    elif Page(selected_page) is Page.VISUALIZE_DATASET:
        visualize_dataset.load_content(settings)
    else:
        st.write("hello world")
    st.session_state["initialized"] = False


# asyncio.run(main())

main()
