import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Enhanced Sales Dashboard", page_icon=":chart_with_upwards_trend:", layout="wide")

# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # Add 'hour' column to dataframe
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Filter Options")
city = st.sidebar.multiselect(
    "Select City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range:",
    value=(df["Date"].min(), df["Date"].max())
)

df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender & Date >= @date_range[0] & Date <= @date_range[1]"
)

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

# ---- DOWNLOAD FILTERED DATA ----
st.sidebar.download_button(
    label="Download Filtered Data",
    data=df_selection.to_csv(index=False),
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

# ---- MAINPAGE ----
st.title(":chart_with_upwards_trend: Enhanced Sales Dashboard")
st.markdown("### Key Performance Indicators")

# Metrics
total_sales = int(df_selection["Total"].sum())
st.metric(label="Total Sales", value=f"US $ {total_sales:,}")

average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = "⭐" * int(round(average_rating, 0))
st.metric(label="Average Rating", value=f"{average_rating} {star_rating}")

average_sale_by_transaction = round(df_selection["Total"].mean(), 2)
st.metric(label="Average Sales per Transaction", value=f"US $ {average_sale_by_transaction}")

st.markdown("""---""")

# ---- REUSABLE FUNCTIONS FOR CHARTS ----
def create_donut_chart(data, values, names, title, color_scheme):
    return px.pie(
        data,
        values=values,
        names=names,
        title=title,
        hole=0.4,
        color_discrete_sequence=color_scheme
    )

def create_bubble_chart(data, x, y, size, color, title, color_scheme):
    return px.scatter(
        data,
        x=x,
        y=y,
        size=size,
        color=color,
        title=title,
        template="ggplot2",
        color_discrete_sequence=color_scheme
    )

def create_area_chart(data, x, y, title, color):
    return px.area(
        data,
        x=x,
        y=y,
        title=title,
        markers=True,
        color_discrete_sequence=[color]
    )

def create_radial_chart(data, r, theta, title, color, color_scheme):
    return px.bar_polar(
        data,
        r=r,
        theta=theta,
        title=title,
        color=color,
        color_continuous_scale=color_scheme,
        template="seaborn"
    )

def create_sankey_chart(data, dimensions, color, color_scheme):
    return px.parallel_categories(
        data,
        dimensions=dimensions,
        color=color,
        color_continuous_scale=color_scheme
    )

# ---- VISUALIZATIONS ----
sales_by_product_line = df_selection.groupby(by=["Product line"])[["Total"]].sum()
fig_product_sales_donut = create_donut_chart(
    sales_by_product_line,
    values="Total",
    names=sales_by_product_line.index,
    title="Sales Distribution by Product Line",
    color_scheme=px.colors.sequential.Reds
)

sales_by_city_gender = df_selection.groupby(by=["City", "Gender"])[["Total"]].sum().reset_index()
fig_city_gender_bubble = create_bubble_chart(
    sales_by_city_gender,
    x="City",
    y="Total",
    size="Total",
    color="Gender",
    title="Sales Distribution by City and Gender",
    color_scheme=px.colors.qualitative.Set1  # Use Set1 for categorical colors
)

sales_by_hour = df_selection.groupby(by=["hour"])[["Total"]].sum()
fig_hourly_sales_area = create_area_chart(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="Hourly Sales Trend",
    color="#FF6347"  # Red color shade
)

sales_by_payment = df_selection.groupby(by=["Payment"])[["Total"]].sum().reset_index()
fig_payment_donut = create_donut_chart(
    sales_by_payment,
    values="Total",
    names="Payment",
    title="Sales by Payment Method",
    color_scheme=px.colors.sequential.Reds
)

# ---- DISPLAY VISUALIZATIONS ----
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_product_sales_donut, use_container_width=True)
    st.plotly_chart(fig_city_gender_bubble, use_container_width=True)
with col2:
    st.plotly_chart(fig_hourly_sales_area, use_container_width=True)
    st.plotly_chart(fig_payment_donut, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)