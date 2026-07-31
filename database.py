import sqlite3
import pandas as pd

data = pd.read_csv("data/transactions.csv")

connection = sqlite3.connect("financial_data.db")
cursor=connection.cursor()
data.to_sql(
    "transactions",
    connection,
    if_exists="replace",
    index=False
)
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "CustomerName": ["Ahmed", "Mohamed", "Omar", "Ali", "Hassan"]
})
customers.to_sql(
    "customers",
    connection,
    if_exists="replace",
    index=False
)
accounts = pd.DataFrame({
    "AccountID": [101, 102, 103],
    "CustomerID": [1, 2, 3],
    "Balance": [15000, 22000, 8000],
    "AccountType": ["Savings", "Current", "Savings"]
})

accounts.to_sql(
    "Accounts",
    connection,
    if_exists="replace",
    index=False
)
cursor.execute("""
CREATE TABLE IF NOT EXISTS financial_products (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT,
    ProductType TEXT,
    InterestRate REAL
)
""")
cursor.execute("DELETE FROM financial_products")

cursor.executemany("""
INSERT INTO financial_products
(ProductID, ProductName, ProductType, InterestRate)
VALUES (?, ?, ?, ?)
""", [
    (1, "Personal Loan", "Loan", 18.5),
    (2, "3-Year Certificate", "Certificate", 22.0),
    (3, "Savings Account", "Deposit", 16.0)
])
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_products (
    CustomerID INTEGER,
    ProductID INTEGER,
    Balance REAL
)
""")

cursor.execute("DELETE FROM customer_products")

cursor.executemany("""
INSERT INTO customer_products
(CustomerID, ProductID, Balance)
VALUES (?, ?, ?)
""", [
    (1, 1, 50000),
    (1, 2, 100000),
    (2, 3, 7000),
    (3, 1, 30000)
])

connection.commit()
connection.close()

print("Database created successfully")