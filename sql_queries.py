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

print(df.sort_values("ProductBalance", ascending=False))