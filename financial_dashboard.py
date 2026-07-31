import sqlite3
import pandas as pd

connection = sqlite3.connect("financial_data.db")

query = """
SELECT
    c.CustomerName,
    a.AccountType,
    a.Balance AS AccountBalance,
    fp.ProductName,
    cp.Balance AS ProductBalance
FROM Customers c
JOIN Accounts a
    ON c.CustomerID = a.CustomerID
LEFT JOIN Customer_Products cp
    ON c.CustomerID = cp.CustomerID
LEFT JOIN Financial_Products fp
    ON cp.ProductID = fp.ProductID;
"""

df = pd.read_sql_query(query, connection)

connection.close()

print("\n===== Financial KPIs =====")

print("Total Customers:", df["CustomerName"].nunique())

print("Total Account Balance:", df["AccountBalance"].sum())

print("Average Account Balance:", df["AccountBalance"].mean())

print("Highest Account Balance:", df["AccountBalance"].max())

print("Total Product Balance:", df["ProductBalance"].sum())

print("\nAccount Balance by Account Type")
print(df.groupby("AccountType")["AccountBalance"].sum())

print("\nProduct Balance by Product")
print(df.groupby("ProductName")["ProductBalance"].sum())

print("\nTop Customers")
print(df.sort_values("AccountBalance", ascending=False))