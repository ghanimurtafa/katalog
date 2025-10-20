import streamlit as st
import pandas as pd
import numpy as np

# df = pd.read_excel(r'c:\Users\USER\Koding\Webscrape\toto.xlsx')
# links=df['link']
# out_xpath1=[]
# out_xpath2=[]
# out_xpath3=[]

# from lxml import html
# import requests

# # Request the page
# for i in range(len(links)):
#      page = requests.get(links[i])

#     # Parsing the page
#      tree = html.fromstring(page.content)

#     # Get element using XPath
#      prices = tree.xpath('//*[@id="comp-ma3gixso"]/div/span')
#      for price in prices:
#           out_xpath1.append(price.text_content())
#      names = tree.xpath('//*[@id="comp-k0f3rwab"]/h1')
#      for name in names:
#           out_xpath2.append(name.text_content())
#      oprices = tree.xpath('//*[@id="comp-k0f3tk01"]/div/span/text()')
#      out_xpath3.append(oprices[0])

# def clean_price(price):
#     # Remove "IDR" and any extra spaces/newlines
#     price = price.replace('IDR', '').strip()
#     # Remove everything after the first newline
#     price = price.split('\n')[0]
#     # Remove commas
#     # price = price.replace(',0', '')
#     price = price.replace(',', '')
#     # Convert to integer
#     return int(price)

# # Apply cleaning
# df["output1"] = out_xpath1
# df["Nama"] = out_xpath2
# df["output3"] = out_xpath3
# df['Retail Price'] = df['output1'].apply(clean_price)
# df['ori_price'] = df['output3'].apply(clean_price)
# df['Final Price'] = df['Retail Price']*(1-df['disc'])
# df['Discount'] = df['disc']

# df = df[['Nama', 'Retail Price', 'Discount', 'Final Price', 'link']]

# ## Streamlit display
# st.set_page_config(
#     page_title="Katalog Harga Produk",
#     page_icon="👋",
# )
# st.write("# Katalog Harga Produk Toto")

# # Format price with thousands separator and discount as %
# df_display = df.copy()
# df_display['Retail Price'] = df_display['Retail Price'].apply(lambda x: f"IDR {x:,.0f}")
# df_display['Final Price'] = df_display['Final Price'].apply(lambda x: f"IDR {x:,.0f}")
# df_display['Discount'] = df_display['Discount'].apply(lambda x: f"{x*100:.0f}%")

# # 🔗 Make link clickable
# df_display['link'] = df_display['link'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')

# # Display as HTML table
# st.markdown(
#     df_display.to_html(escape=False, index=False),
#     unsafe_allow_html=True
# )

import streamlit as st
import pandas as pd

df=pd.read_excel('katalog_toto.xlsx')

# Example Data (remove or replace with your actual df)
# df = pd.read_excel("katalog_toto.xlsx")

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="Katalog Harga Produk Toto",
    page_icon="🚽",
    layout="wide"
)
st.markdown("""
    <style>
    /* Force light mode background and text */
    html, body, [class*="css"] {
        background-color: white !important;
        color: black !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: white !important;
    }
    [data-testid="stSidebar"] {
        background-color: #f7f7f7 !important;
    }
    table, th, td {
        color: black !important;
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

# --- Styling for the Table ---
st.markdown("""
    <style>
    table {
        width: 100%;
        border-collapse: collapse;
    }
    thead {
        background-color: #f2f2f2;
    }
    th, td {
        text-align: left;
        padding: 10px;
    }
    tr:nth-child(even) {
        background-color: #fafafa;
    }
    tr:hover {
        background-color: #f5f5f5;
    }
    a {
        color: #007bff;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# --- Display the Table ---
st.markdown("### 🧾 Daftar Produk")

if df_display.empty:
    st.warning("Tidak ada produk yang cocok dengan filter yang dipilih.")
else:
    st.markdown(df_display.to_html(escape=False, index=False), unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 Katalog Produk Toto | PT Bapak Budiman")
