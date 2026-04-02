import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract month
data['Month'] = data['Date'].dt.month

# Monthly sales aggregation
monthly_sales = data.groupby('Month')['Sales'].sum()

# Category sales aggregation
category_sales = data.groupby('Category')['Sales'].sum()

# Line chart (sales over time)
plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.savefig("line_chart.png")
plt.show()

# Bar chart (category comparison)
plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("bar_chart.png")
plt.show()

# Pie chart (sales share)
plt.figure(figsize=(6,6))
plt.pie(category_sales.values, labels=category_sales.index, autopct='%1.1f%%')
plt.title("Category Sales Share")
plt.savefig("pie_chart.png")
plt.show()

print("Charts saved successfully!")