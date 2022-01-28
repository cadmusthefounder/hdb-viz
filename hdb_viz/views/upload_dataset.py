import streamlit as st

from hdb_viz.settings import Settings


def handle_submit(c):
    # c.write(st.session_state.upload_dataset_form_name)
    # c.write(st.session_state.upload_dataset_form_period)
    c.markdown("**Dataset uploaded successfully!**")


def load_content(settings: Settings):
    c = st.container()

    c.title("Upload Dataset")

    form = c.form(key="upload_dataset_form")
    form.text_input("Dataset Name", key="upload_dataset_form_name")
    form.slider(
        "Period",
        min_value=1990,
        max_value=2022,
        value=[1990, 2022],
        key="upload_dataset_form_period",
    )

    form.file_uploader(
        "Upload HDB resale flat prices dataset.",
        type=["csv"],
        key="upload_dataset_form_file",
    )
    form.form_submit_button(label="Upload", on_click=handle_submit, args=(c,))
