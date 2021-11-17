import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.title("Coin CSV")

coin_list = ["LTC", "ETH", "BTC"]
# Read CSV File for the first time
df = pd.read_csv("coin_data.csv")

with st.form("Input"):
    # Input
    coin = st.selectbox("Select a coin", coin_list)
    X1 = st.number_input(
        "Select your X1", min_value=1e-5, max_value=999999999.999999, step=1e-5
    )
    Y1 = st.number_input(
        "Select your Y1", min_value=1e-5, max_value=999999999.999999, step=1e-5
    )
    Z1 = st.number_input(
        "Select your Quantity", min_value=1e-5, max_value=9999999999.9999, step=1e-5
    )

    if st.form_submit_button("Submit"):
        # Preparing input to be appended to CSV
        df_input = pd.DataFrame(
            {
                "Coins": [coin],
                "X1": [X1],
                "Y1": [Y1],
                "Quantity": [Z1],
            }
        )
        # Add the input to csv
        df_input.to_csv("coin_data.csv", mode="a", index=False, header=False)

# Read the CSV File again
df = pd.read_csv("coin_data.csv")
# Table Making
fig = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=list(df.columns),
                fill_color="paleturquoise",
                align="left",
                font=dict(color="black", family="Lato", size=15),
            ),
            cells=dict(
                values=[df.Coins, df.X1, df.Y1, df.Quantity],
                fill_color="lavender",
                align="left",
                font=dict(color="black", family="Lato", size=15),
            ),
        )
    ]
)
# Show Table
st.plotly_chart(fig, use_container_width=True)
