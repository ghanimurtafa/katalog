import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("katalog_toto.csv")

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="Katalog Harga Produk Toto",
    page_icon="🚽",
    layout="wide"
)

# --- Adaptive CSS for both light & dark modes ---
st.markdown("""
    <style>
    /* Use theme-aware variables provided by Streamlit */
    html, body, [class*="css"] {
        background-color: var(--background-color) !important;
        color: var(--text-color) !important;
    }

    table {
        width: 100%;
        border-collapse: collapse;
    }
    thead {
        background-color: rgba(128, 128, 128, 0.1);
    }
    th, td {
        text-align: left;
        padding: 10px;
    }
    tr:nth-child(even) {
        background-color: rgba(128, 128, 128, 0.05);
    }
    tr:hover {
        background-color: rgba(128, 128, 128, 0.15);
    }
    a {
        color: #1e90ff;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# --- Page Header ---
st.title("🛁 Katalog Harga Produk Toto")
st.markdown("Lihat daftar produk lengkap beserta harga dan tautan katalog resmi Toto Indonesia.")

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Produk")

# Filter by name
search = st.sidebar.text_input("Cari Nama Produk:")
if search:
    df = df[df['Nama'].str.contains(search, case=False, na=False)]

# Filter by discount (if available)
if 'Discount' in df.columns:
    min_discount = st.sidebar.slider("Diskon minimum (%):", 0, 100, 0)
    df = df[df['Discount'] * 100 >= min_discount]

# --- Prepare Data for Display ---
df_display = df.copy()

# Format prices and discounts
if 'Retail Price' in df_display.columns:
    df_display['Retail Price'] = df_display['Retail Price'].apply(lambda x: f"IDR {x:,.0f}")
if 'Final Price' in df_display.columns:
    df_display['Final Price'] = df_display['Final Price'].apply(lambda x: f"IDR {x:,.0f}")
if 'Discount' in df_display.columns:
    df_display['Discount'] = df_display['Discount'].apply(lambda x: f"{x*100:.0f}%")

# 🔗 Make the 'link' column clickable
if 'link' in df_display.columns:
    df_display['link'] = df_display['link'].apply(
        lambda x: f'<a href="{x}" target="_blank">Lihat Produk 🔗</a>' if pd.notnull(x) else ''
    )

# --- Display the Table ---
st.markdown("### 🧾 Daftar Produk")

if df_display.empty:
    st.warning("Tidak ada produk yang cocok dengan filter yang dipilih.")
else:
    st.markdown(df_display.to_html(escape=False, index=False), unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 Katalog Produk Toto | PT Bapak Budiman")

