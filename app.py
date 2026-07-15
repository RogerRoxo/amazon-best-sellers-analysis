import pandas as pd
import streamlit as st
import plotly.express as px
import operator
from functools import reduce


st.set_page_config(
    page_title="Amazon Best Salers",
    layout="wide"
)

df = pd.read_csv("data/bestsellers with categories.csv")


st.title("Amazon Best Sellers | 2009 - 2019")

st.subheader("Search")
with st.container(border=True):
    
    st.write("Filters:")

    col1, col2, col3, col4 = st.columns(4)

    # Filter permission
    with col1:
        author_filter_bool = st.checkbox("Author", value=False, width=200)
        author = st.selectbox("Author", sorted(df["Author"].unique()), disabled=not author_filter_bool)
        
    with col2:
        rating_filter_bool = st.checkbox("Rating", value=False)
        rating = st.selectbox("User Rating", ["0-1", "1-2", "2-3", "3-4", "4-5"], disabled=not rating_filter_bool)

    with col3:
        year_filter_bool = st.checkbox("Year", value=False)
        year = st.selectbox("Publication Year", sorted(df["Year"].unique()), disabled=not year_filter_bool)

    with col4:
        genre_filter_bool = st.checkbox("Genre", value=False)
        genre = st.selectbox("Genre", df["Genre"].unique(), disabled=not genre_filter_bool)
   

    # Create Filters conditions
    author_filter = df["Author"] == author
    year_filter = df["Year"] == year
    genre_filter = df["Genre"] == genre

    rating_filter1 = df["User Rating"] >= int(rating[0])
    rating_filter2 = df["User Rating"] < int(rating[-1])
    rating_filter3 = rating_filter1 & rating_filter2


    # Activation filters list
    filters_bool = [author_filter_bool, rating_filter_bool, year_filter_bool, genre_filter_bool]

    filters_list = [author_filter, rating_filter3, year_filter, genre_filter]

    active_filter = []
    for i, active in enumerate(filters_bool):
        if active == True:
            active_filter.append(filters_list[i])

    # Have filters on?
    filter_on = reduce(operator.or_, filters_bool)


    if (filter_on):
        book_filter = reduce(operator.and_, active_filter)
        st.dataframe(df[book_filter])
    else:
        st.dataframe(df)


# Analytics
df["Short_Name"] = df["Name"].str.slice(0, 35)

st.subheader("Analytics")

with st.container():
    analyctic_col1, analyctic_col2, analyctic_col3 = st.columns([0.7,1,1])
    
    with analyctic_col1:
        st.metric("Books Per Year", 50, border=True)

review_col1, review_col2 = st.columns(2)
with review_col1:
    with st.container(border=True):
        st.subheader("Total Reviews per Year")
        
        review_fig1 = px.bar(
            df[["Year", "Reviews"]].groupby("Year").sum(), 
            color_discrete_sequence=["#1ba3c2"]
        )
        
        review_fig1.update_layout(yaxis_title=None)
        review_fig1.update_xaxes(tickmode="linear")
        
        st.plotly_chart(review_fig1)
        
        st.write("The number of reviews increased steadily from 2009 to 2012, after which it stabilized between 600,000 and 800,000 reviews for the annual best sellers. This pattern may reflect increased customer engagement or a growing number of buyers during that period, although review counts alone cannot confirm the cause.")
          
with review_col2:
    with st.container(border=True):
        st.subheader("Top 10 Most Reviewed Books")
        
        top10_reviews = df[["Short_Name", "Reviews"]].groupby("Short_Name").sum().nlargest(10, "Reviews")
        
        review_fig2 = px.bar(
            top10_reviews,
            x="Reviews",
            color=top10_reviews.index,
            color_discrete_sequence=px.colors.qualitative.Dark2
        )
        
        review_fig2.update_layout(
            showlegend=False,
            xaxis_title=None,
            yaxis_title=None
        )
        
        st.plotly_chart(review_fig2)
    

price_col1, price_col2, price_col3 = st.columns([4, 3, 3])
with price_col1:
    with st.container(border=True):
        st.subheader("Mean Prices per Year")
        
        fig2 = px.bar(
            df[["Year", "Price"]].groupby("Year").mean(),
            color_discrete_sequence=["#389931"]
        )
        
        fig2.update_layout(
            showlegend=False,
            yaxis_title=None
        )
        fig2.update_xaxes(tickmode="linear")
        
        st.plotly_chart(fig2)
        
        st.write("Since 2014, the average price of Amazon best-selling books has been declining. This trend may suggest that more affordable books have become increasingly popular among readers, although additional data would be required to determine the underlying causes.")
        
with price_col2:
    with st.container(border=True):
        st.subheader("Lowest-Priced Books")
        
        df_price1 = df[["Short_Name", "Price"]].groupby("Short_Name").sum().nsmallest(10, "Price")
        
        low_price_fig = px.bar(
            df_price1,
            x="Price",
            color=df_price1.index,
        )
        
        low_price_fig.update_layout(
            showlegend=False,
            xaxis_title=None,
            yaxis_title=None
        )
        
        
        st.plotly_chart(low_price_fig)
                
with price_col3:
    with st.container(border=True):
        st.subheader("Highest-Priced Books")
        
        df_price2 = df[["Short_Name", "Price"]].groupby("Short_Name").sum().nlargest(10, "Price")
        
        high_price_fig = px.bar(
            df_price2,
            x="Price",
            color=df_price2.index,
            color_discrete_sequence=px.colors.qualitative.Safe_r
        )
        
        high_price_fig.update_layout(
            showlegend=False,
            xaxis_title=None,
            yaxis_title=None
        )
        
        
        st.plotly_chart(high_price_fig)
    

best_seller_col, fic_nonfic_col =st.columns([2,3])
with best_seller_col:
    with st.container(border=True):
        st.subheader("Top 10 Best-Selling Authors | 2009 - 2019")
        
        top10_author = df["Author"].value_counts().nlargest(10)
        
        author_fig = px.bar(
            top10_author,
            orientation="h",
            color=top10_author.index
        )
        
        author_fig.update_layout(
            showlegend=False, 
            xaxis_title=None,
            yaxis_title=None
        )
        
        st.plotly_chart(author_fig)
    
with fic_nonfic_col:
    with st.container(border=True):
        st.subheader("Fiction Vs Non-Fiction")
        
        genre_fig = px.bar(
            df.groupby(["Year", "Genre"]).size().reset_index(name="Count"),
            x="Year",
            y="Count",
            color="Genre"
        )
        
        genre_fig.update_layout(
            barmode="group",
            yaxis_title=None
            )
        genre_fig.update_xaxes(tickmode="linear")
        
        st.plotly_chart(genre_fig)
        
        st.write("From 2009 to 2019, Amazon's best-selling books were predominantly non-fiction. The only exception occurred in 2014, when fiction titles exceeded non-fiction by 38%. As this differs noticeably from the overall pattern, it may represent a temporary shift in consumer preferences or an isolated variation, although additional data would be needed to determine the reason.")

