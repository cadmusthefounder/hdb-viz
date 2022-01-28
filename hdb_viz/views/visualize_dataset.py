import pandas as pd
import plotly.express as px
import streamlit as st

from hdb_viz.settings import Settings


def load_content(settings: Settings):

    c = st.container()
    c.title("Visualize Dataset")

    if all(
        k in st.session_state
        for k in (
            "upload_dataset_form_name",
            "upload_dataset_form_period",
            "upload_dataset_form_file",
        )
    ):
        df = pd.read_csv(st.session_state.upload_dataset_form_file)
        c.write(df.head(10))

        c.write("Plotting AMK prices across time:")

        df_b = df[df["town"].str.contains("ANG MO KIO")]
        fig = px.line(df_b, x="month", y="resale_price")
        c.plotly_chart(fig)
