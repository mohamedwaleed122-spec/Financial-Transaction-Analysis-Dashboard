import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect("financial_data.db")

df = pd.read_sql_query("SELECT * FROM Accounts", connection)


connection.close()

print(df.columns)
print(df.head())

summary = df.groupby("AccountType")["Balance"].sum()

plt.figure(figsize=(8, 5))
bars = plt.bar(summary.index, summary.values)

plt.title("Account Balances")
plt.xlabel("Account Type")
plt.ylabel("Balance")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center",
        va="bottom"
    )

plt.show()