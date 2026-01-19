import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
df = pd.read_csv("sales_data.csv")
df.fillna(0, inplace=True)

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# =======================
# SEABORN PLOTS (STATIC)
# =======================

# 1. Line Plot – Sales Trend
plt.figure()
sns.lineplot(data=df, x="Date", y="Total_Sales")
plt.title("Sales Trend Over Time")
plt.show()

# 2. Bar Plot – Sales by Product
plt.figure()
sns.barplot(data=df, x="Product", y="Total_Sales", estimator=sum)
plt.title("Total Sales by Product")
plt.show()

# 3. Box Plot – Customer Spending Distribution
plt.figure()
sns.boxplot(data=df, x="Region", y="Total_Sales")
plt.title("Customer Spending by Region")
plt.show()

# =======================
# PLOTLY (INTERACTIVE)
# =======================

# 4. Interactive Line Chart – Sales Over Time
fig1 = px.line(df, x="Date", y="Total_Sales", title="Interactive Sales Trend")
fig1.show()

# 5. Interactive Pie Chart – Sales by Region
region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()
fig2 = px.pie(region_sales, names="Region", values="Total_Sales",
              title="Sales Distribution by Region")
fig2.show()

# 6. Interactive Bar Chart – Product Performance
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()
fig3 = px.bar(product_sales, x="Product", y="Total_Sales",
              title="Product Performance Dashboard")
fig3.show()
