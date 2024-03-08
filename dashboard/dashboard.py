import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

top_sellers = pd.read_csv("top_sellers.csv")
top_selling_categories = pd.read_csv("top_selling_categories.csv")

# Title
st.header('Fariz Eda Dasboard :sparkles:')
st.subheader('Our Top 5s')

col1, col2 = st.columns(2)


with col1:
    best_selling_category_name = top_selling_categories.iloc[0]['product_category_name_english']
    st.metric("Our best selling categories", value=best_selling_category_name)

with col2:
    best_seller = top_sellers.iloc[0]['seller_id']
    st.metric("Our best seller", value=best_seller)



tab1, tab2 = st.tabs(["Product Categories", "Seller"])

with tab1:
    st.header("Top 5 Best Selling Product Categories")
    top_5_categories = top_selling_categories.head()
    fig, ax = plt.subplots(figsize=(35, 15))
 
    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    
    sns.barplot(x="price", y="product_category_name_english", data=top_5_categories, palette=colors)
    ax.set_ylabel(None)
    ax.set_xlabel("Number of Sales", fontsize=30)
    ax.set_title("Best Performing Product", loc="center", fontsize=50)
    ax.tick_params(axis='y', labelsize=35)
    ax.tick_params(axis='x', labelsize=30)

    st.pyplot(fig)

with tab2:
    st.header("Top 5 Best Sellers")

    top_5_sellers = top_sellers.head()
    fig, ax = plt.subplots(figsize=(35, 15))
 
    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    
    sns.barplot(x="price", y="seller_id", data=top_5_sellers, palette=colors)
    ax.set_ylabel(None)
    ax.set_xlabel("Number of Sales", fontsize=30)
    ax.set_title("Seller ID", loc="center", fontsize=50)
    ax.tick_params(axis='y', labelsize=35)
    ax.tick_params(axis='x', labelsize=30)

    st.pyplot(fig)


    