import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
df = pd.read_csv("sales_data.csv")
print("Initial Data:\n", df)

# Step 2: Add Total Sales column
df["Total_Sales"] = df["Units_Sold"] * df["Unit_Price"]
print("\nData with Total Sales:\n", df)

# Step 3: Group by Region
sales_by_region = df.groupby("Region")["Total_Sales"].sum()
print("\nSales by Region:\n", sales_by_region)

# Step 4: Group by Product
sales_by_product = df.groupby("Product")["Total_Sales"].sum()
print("\nSales by Product:\n", sales_by_product)

# Step 5: Best/Worst Performers
print("\nBest Region:", sales_by_region.idxmax())
print("Worst Region:", sales_by_region.idxmin())

print("Best Product:", sales_by_product.idxmax())
print("Worst Product:", sales_by_product.idxmin())

# Step 6: Bar Chart - Sales by Product
plt.figure(figsize=(8, 5))
sales_by_product.plot(kind="bar", color="orange")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.show()

# Step 7: Pie Chart - Sales by Region
plt.figure(figsize=(6, 6))
sales_by_region.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()
