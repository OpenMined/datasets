import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("sales.csv")

# Compute total sale for each row
df["total_sale"] = df["quantity"] * df["price_per_unit"]

# 1️⃣ Total sales per region
region_sales = df.groupby("region")["total_sale"].sum()
print(region_sales)

# 2️⃣ Total sales per product
product_sales = df.groupby("product")["total_sale"].sum()
print(product_sales)

# 3️⃣ Count of transactions per region
region_counts = df["region"].value_counts()
print(region_counts)

# 4️⃣ Visualize total sales by region
region_sales.plot(kind="bar", title="Total Sales by Region", color="skyblue")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Region")
plt.show()

# 5️⃣ Visualize sales trend over time
daily_sales = df.groupby("date")["total_sale"].sum()
daily_sales.plot(kind="line", title="Sales Trend Over Time", marker="o")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Date")
plt.show()
