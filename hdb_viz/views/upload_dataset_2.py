import streamlit as st

from hdb_viz.settings import Settings


def load_content(settings: Settings):
    e = st.empty()
    c = e.container()

    c.title("Upload Dataset 2")

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
    submit = form.form_submit_button(label="Upload", args=(c))

    if submit:
        e.empty()
        st.markdown("**Dataset uploaded successfully!**")
