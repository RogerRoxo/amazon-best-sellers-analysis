# Amazon Best Sellers Analysis

This project aims to serve as a data analysis study. I used a dataset containing Amazon best-selling books from 2009 to 2019.
The following tools were used for the analysis:
- Python
- Pandas
- Plotly
- Streamlit

The dataset is based on the following information: book title, author, user rating, number of reviews, price, year in which the book became a best-seller, and genre (Fiction and Non-Fiction).

##  Interactive Search

Since the dataset contains several fields that can be easily filtered, I created a search tab where users can filter table items based on selectable criteria. The filters were divided into "Author", "User Rating", "Publication Year", and "Genre".

## Temporal Analysis

###  Best Sellers by Year

Each year contains 50 best-selling books.

###  Total Reviews per Year
The number of reviews increased steadily from 2009 to 2012, after which it stabilized between 600,000 and 800,000 reviews for the annual best sellers. This pattern may reflect increased customer engagement or a growing number of buyers during that period, although review counts alone cannot confirm the cause.

###  Mean Prices per Year
Since 2014, the average price of Amazon best-selling books has been declining. This trend may suggest a shift toward lower-priced books among customers, although additional data would be required to understand the factors behind this change.

###  Fiction VS Non-Fiction
From 2009 to 2019, Amazon's best-selling books were predominantly non-fiction. The only exception occurred in 2014, when fiction titles exceeded non-fiction by 38%. As this differs noticeably from the overall pattern, it may represent a temporary shift in consumer preferences or an isolated variation, although additional data would be needed to determine the reason.

## Additional Insights
Criei gráficos adicionais para destacar as classificações do conjunto de dados:
- Top 10 Most Reviewed Books
- Lowest-Priced Books & Highest-Priced Books
  - It demonstrates a significant difference between the values of best-selling books.
- Top 10 Best-Selling Authors | 2009 - 2019

