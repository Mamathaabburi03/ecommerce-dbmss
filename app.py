import streamlit as st
import sqlite3
import pandas as pd
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
)
""")
conn.commit()
st.title("🛒 E-Commerce Management System")
menu = ["Add Product", "View Products"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Add Product":
    st.subheader("Add Product")
    name = st.text_input("Product Name")
    price = st.number_input("Price")
    if st.button("Add"):
        cursor.execute("""
        INSERT INTO products (name, price)
        VALUES (?, ?)
        """, (name, price))
        conn.commit()
        st.success("Product Added Successfully!")
elif choice == "View Products":
    st.subheader("All Products")
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    df = pd.DataFrame(
        rows,
        columns=["ID", "Name", "Price"]
    )
    st.dataframe(df)
conn.close()
