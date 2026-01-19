
# ==============================
# INTERACTIVE SALES DASHBOARD
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ------------------------------
# 1. LOAD DATA
# ------------------------------
df = pd.read_csv("sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

print("Data Loaded Successfully")
print(df.head())

# ------------------------------
# 2. DATA CLEANING
# ------------------------------
# Handle missing values
df = df.dropna()

# ------------------------------
# 3. AGGREGATIONS
# ------------------------------

# Aggregation 1: Total Sales by Product
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()

# Aggregation 2: Sales by Region
region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()

# Aggregation 3: Daily Sales Trend
daily_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()

# Aggregation 4: Top Customers
top_customers = (
    df.groupby("Customer_ID")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# ------------------------------
# 4. STATIC VISUALIZATIONS (Seaborn / Matplotlib)
# ------------------------------

# BAR CHART – Total Sales by Product
plt.figure()
sns.barplot(data=product_sales, x="Product", y="Total_Sales")
plt.title("Total Sales by Product")
plt.show()

# LINE CHART – Sales Trend Over Time
plt.figure()
sns.lineplot(data=daily_sales, x="Date", y="Total_Sales")
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.show()

# PIE CHART – Sales by Region
plt.figure()
plt.pie(
    region_sales["Total_Sales"],
    labels=region_sales["Region"],
    autopct="%1.1f%%"
)
plt.title("Sales Distribution by Region")
plt.show()

# BOX PLOT – Sales Distribution by Region
plt.figure()
sns.boxplot(data=df, x="Region", y="Total_Sales")
plt.title("Sales Distribution by Region")
plt.show()

# SCATTER PLOT – Quantity vs Total Sales
plt.figure()
sns.scatterplot(data=df, x="Quantity", y="Total_Sales", hue="Product")
plt.title("Quantity vs Total Sales")
plt.show()

# ------------------------------
# 5. INTERACTIVE DASHBOARD (Plotly)
# ------------------------------

# Interactive Line Chart
fig1 = px.line(
    daily_sales,
    x="Date",
    y="Total_Sales",
    title="Interactive Sales Trend"
)
fig1.show()

# Interactive Bar Chart
fig2 = px.bar(
    product_sales,
    x="Product",
    y="Total_Sales",
    title="Interactive Product Performance"
)
fig2.show()

# Interactive Pie Chart
fig3 = px.pie(
    region_sales,
    names="Region",
    values="Total_Sales",
    title="Interactive Sales by Region"
)
fig3.show()

# ------------------------------
# 6. INSIGHTS OUTPUT
# ------------------------------
print("\nTop 10 Customers by Total Sales:")
print(top_customers)

print("\nBest Selling Product:")
print(product_sales.sort_values(by="Total_Sales", ascending=False).head(1))

print("\nProject Completed Successfully ✅")
