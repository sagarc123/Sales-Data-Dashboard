## Sales Data DashBoard

## Overview

This **Sales Data Dashboard** is an interactive data visualization project built with **Streamlit**, **Plotly**, and **Pandas**. It allows users to analyze supermarket sales data with real-time filtering options, dynamic key performance indicators (KPIs), and engaging visualizations.

The dashboard is designed to provide businesses with critical insights into their sales performance, customer demographics, payment methods, and sales trends.

## Features

- **Real-Time Data Filtering**: Users can filter data by **City**, **Customer Type**, **Gender**, and **Date Range**.
- **Dynamic KPIs**: Displays essential KPIs such as **Total Sales**, **Average Rating**, and **Average Sales per Transaction**.
- **Interactive Visualizations**:
  - **Donut Charts** for sales distribution by product line and payment method.
  - **Bubble Chart** showing sales distribution by city and gender.
  - **Area Chart** visualizing hourly sales trends.
- **Data Export**: Option to download the filtered data as a CSV file for further analysis.

## Technologies Used

- **Streamlit**: For building the interactive dashboard.
- **Plotly**: For creating interactive charts and visualizations.
- **Pandas**: For data manipulation and analysis.
- **Openpyxl**: For reading Excel files containing sales data.

## Setup and Installation

### Prerequisites

Ensure you have **Python 3.6+** installed. You can check your Python version using:

python --version

### Installation Steps

1. Clone the repository:

git clone https://github.com/sagarc123/Sales-Data-Dashboard.git

2. Navigate to the project directory:

cd Sales-Data-Dashboard

3. Run the Streamlit app:

streamlit run app1.py

This will open the dashboard in your default web browser.

## Data

The data used in this project is a sample supermarket sales dataset (`supermarkt_sales.xlsx`). It includes details such as:

- **Date of the sale**
- **City**, **Customer Type**, **Gender**
- **Product line**, **Total sales**, **Rating**, and **Payment method**
- **Time of the transaction**

The dataset is available in the `supermarkt_sales.xlsx` file, and the dashboard reads the data to perform filtering and visualization.

## How to Use the Dashboard

1. **Filter Options**: Use the sidebar to filter the data based on:
   - **City**
   - **Customer Type**
   - **Gender**
   - **Date Range**
2. **KPIs**:
   - **Total Sales**
   - **Average Rating**
   - **Average Sales per Transaction**
3. **Visualizations**: Explore interactive charts including:

   - **Sales Distribution by Product Line** (Donut Chart)
   - **Sales by City and Gender** (Bubble Chart)
   - **Hourly Sales Trend** (Area Chart)
   - **Sales by Payment Method** (Donut Chart)

4. **Download Data**: You can download the filtered data as a CSV file directly from the sidebar.

## Screenshots

![Dashboard Screenshot 1](screenshots/Image%201.png)
![Dashboard Screenshot 2](screenshots/Image%202.png)
