# Sales Dashboard and Forecasting

## Project Overview

This project involves building a **Sales Dashboard** using **Dash** (a Python framework for building analytical web applications) to visualize and analyze sales performance. The dashboard includes key visualizations for monthly sales trends, product performance, and customer retention. Additionally, I apply time series forecasting (ARIMA) to predict future sales, enabling data-driven decision-making.

### Key Features:
- **Time Series Analysis**: Visualize historical sales data and forecast future trends.
- **Product Analysis**: Display the top-selling products and their total value.
- **Business Performance**: Evaluate business performance based on total quantity and value.
- **Customer Retention**: Identify businesses with declining purchase frequency and suggest strategies for re-engagement.

## Business Understanding

### Stakeholder and Key Business Questions:
- **Stakeholders**: Business owners, sales managers, marketing teams, and inventory managers.
- **Key Business Questions**:
  1. Which products generate the highest sales, and which products should be prioritized for marketing campaigns?
  2. What are the seasonal sales trends, and how can we forecast sales for the next few months?
  3. Are there any products or businesses that show a decrease in sales over time, indicating the need for customer retention strategies?
  4. What operational improvements can be made in inventory management to optimize product performance based on historical data?

## Data Understanding and Analysis

### Source of Data:
The dataset used in this analysis is sourced from a business's transaction history, including product sales across various categories, businesses, and locations. The dataset contains information such as product quantities, unit prices, and total sales values over time.

### Description of Data:
The dataset includes the following columns:
- `DATE`: The date of the transaction.
- `ANONYMIZED CATEGORY`: The product category.
- `ANONYMIZED PRODUCT`: The specific product sold.
- `ANONYMIZED BUSINESS`: The business making the transaction.
- `ANONYMIZED LOCATION`: The location where the transaction occurred.
- `QUANTITY`: Number of units sold.
- `UNIT PRICE`: Price per unit of the product.

### Sample Data:

| Anonymized Product | Quantity | Total Value |
|--------------------|----------|-------------|
| Product-66e0       | 46957    | 185,626,186 |
| Product-e805       | 42602    | 262,787,281 |
| Product-8f75       | 37566    | 158,797,460 |
| Product-29ee       | 35940    | 68,248,274  |
| Product-4156       | 28487    | 56,956,007  |

### Visualizations:
1. **Total Sales Over Time**: A time series plot showing total sales and trends across different months.

![Total Sales over Time](images\Total Sales Over Time.png)

2. **Top 5 Products by Quantity**: A bar chart showcasing the top-selling products based on quantity sold.

![Top 5 by Quantity](images\Top 5 Most Frequently Purchased Products.png)

3. **Top 5 Products by Value**: A bar chart illustrating the highest-value products based on total sales value.
![Top 5 by value](images\Top 5 Products by value.png)

4. 
## Steps Taken

### 1. Data Cleaning:
- **Removed Duplicate Rows**: Duplicate entries were detected and deleted to ensure the integrity of the data.
- **Handled Missing Values**: No missing values were found, ensuring data completeness.
- **Data Type Conversion**: Converted `DATE` to `datetime` format and `UNIT PRICE` to numeric types for further analysis.

### 2. Exploratory Data Analysis (EDA):
- **Unique Values**: Explored the unique values in each column.
- **Descriptive Statistics**: Calculated basic statistics for numerical columns.
- **Data Visualization**: Plotted the top-selling products, business performance, and sales trends.

### 3. Forecasting:
- **ARIMA Forecasting**: Used the ARIMA model to forecast future sales for the next three months.

![Forecast](images\Total Sales Forecast for Next 3 Months.png)

### 4. Insights:
- **Sales Trends**: Visualized trends in sales values and quantities over time.
- **Top 5 Products**: Identified top products by quantity and total value.
- **Customer Retention**: Suggested strategies to re-engage customers with reduced purchase frequency based on historical data.


## Conclusion

### Summary of Conclusions:
- **Sales Performance Trends**: There is a clear seasonal pattern in the sales data, with fluctuations in sales quantity and value based on the month of the year.
- **Top Products**: The analysis shows that certain products are consistently top performers in terms of quantity and value, indicating that these should be prioritized in marketing campaigns.
- **Customer Retention**: Businesses with declining purchase frequencies over time need to focus on personalized marketing strategies and customer re-engagement efforts to maintain long-term customer loyalty.

### Three Relevant Findings:
1. **High-Volume Products**: The most frequently purchased products have the highest quantities sold, highlighting popular items for inventory focus.
2. **Seasonality Impact**: Seasonal fluctuations in sales provide opportunities for targeted marketing and inventory adjustments.
3. **Forecasting**: ARIMA forecasting helps predict future sales trends, allowing businesses to plan for demand fluctuations and operational changes.

## Deployment

The dashboard can be accessed via a deployed web application using platforms such as **Heroku** or **Render**.

### Deployment Steps:
1. **Create a Heroku Account**: Sign up at [Heroku](https://www.heroku.com/).
2. **Set Up Your App**: 
   - Push your code to a GitHub repository.
   - Link your GitHub repository to your Heroku app.
   - Deploy the app using Heroku's buildpacks.
3. **Access the Dashboard**: Once deployed, your dashboard will be accessible via a public URL provided by Heroku (e.g., `https://your-app-name.herokuapp.com/`).

## Usage

Once the dashboard is deployed, users can:
- View monthly sales performance, including trends and forecasts.
- Filter products based on sales performance.
- Explore insights on top-performing businesses and products.
- Use forecasting features to predict sales for future months.

### Example Code:
```python
# Example of loading the data and setting up a Dash app

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Load your dataset
df = pd.read_csv('sales_data.csv')

# Set up your Dash app
app = dash.Dash(__name__)

# Define your layout
app.layout = html.Div([
    html.H1('Sales Dashboard'),
    dcc.Graph(
        id='sales-graph',
        figure={
            'data': [
                {'x': df['DATE'], 'y': df['total_value'], 'type': 'line', 'name': 'Total Value'},
            ],
            'layout': {
                'title': 'Sales Over Time'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

