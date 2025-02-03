import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


# Aggregate data for different visualizations
monthly_sales = kt_clean_df.groupby('month-year').agg({'total_value': 'sum', 'quantity': 'sum'}).reset_index()
category_sales = kt_clean_df.groupby('anonymized_category').agg({'total_value': 'sum', 'quantity': 'sum'}).reset_index()
top_products = kt_clean_df.groupby('anonymized_product').agg({'total_value': 'sum', 'quantity': 'sum'}).reset_index().nlargest(10, 'total_value')
top_businesses = kt_clean_df.groupby('anonymized_business').agg({'total_value': 'sum'}).reset_index().nlargest(10, 'total_value')

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Sales Performance Dashboard", style={'textAlign': 'center'}),
    
    # Total Quantity and Value by Category
    dcc.Graph(
        id='category-sales',
        figure=px.bar(category_sales, x='anonymized_category', y=['total_value', 'quantity'],
                      title="Total Sales Value and Quantity by Category",
                      barmode='group', labels={'value': 'Total Sales', 'quantity': 'Total Quantity'})
    ),
    
    # Top-Performing Products
    dcc.Graph(
        id='top-products',
        figure=px.bar(top_products, x='anonymized_product', y='total_value',
                      title="Top 10 Best-Selling Products",
                      labels={'product_name': 'Product', 'total_value': 'Sales Value'})
    ),
    
    # Top Businesses
    dcc.Graph(
        id='top-businesses',
        figure=px.bar(top_businesses, x='anonymized_business', y='total_value',
                      title="Top 10 Businesses by Sales",
                      labels={'business_name': 'Business', 'total_value': 'Sales Value'})
    ),
    
    # Time-Series Chart of Sales Trends
    dcc.Graph(
        id='sales-trends',
        figure=px.line(monthly_sales, x='month-year', y=['total_value', 'quantity'],
                       title="Sales Trends Over Time", labels={'month-year': 'Date', 'value': 'Sales'})
    ),
    
      # Customer Segmentation Table
    html.H3("Customer Segmentation Summary"),
    dash_table.DataTable(
        id='customer-segmentation',
        columns=[{"name": i, "id": i} for i in ['segment', 'total_value', 'total_quantity']],
        data=kt_business_df.groupby('segment').agg({'total_value': 'sum', 'total_quantity': 'sum'}).reset_index().to_dict('records'),
        style_table={'overflowX': 'auto'},
    ),
    
   
    # Segmentation Scatter Plot
    html.H3("Customer Segmentation Based on Purchasing Behavior"),
    dcc.Graph(
        id='segmentation-plot',
        figure=px.scatter(
            business_grouped,  # Make sure this DataFrame exists
            x='total_value',
            y='quantity',
            color='group',
            size='frequency',
            hover_data=['anonymized_business'],  
            title='Customer Segmentation Based on Purchasing Behavior'
        )
    )
])



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
