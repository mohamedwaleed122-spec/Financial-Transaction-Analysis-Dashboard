# ======================
# Numpy Analysis
# ======================

import numpy as np
transactions=np. array([
    [1000,1,1],
    [2500,2,1],
    [700,1,0],
    [3200,2,1],
    [4500,1,1]
])
print(transactions[:2])
print(transactions[0])
print(transactions.shape)
print(transactions[2:])
print(transactions[1:4])
print(transactions.ndim)
print(transactions.size)
print(transactions.sum())
print(transactions.mean())
print(transactions.max())
print(transactions.min())

# ======================
# Pandas Analysis
# ======================

import numpy as np
amounts=np.array([1000, 2500, 700, 3200, 4500])
print("===== Daily Financial Report=====")
print("Total Transactions :", amounts.sum())
print("Average Transaction:", amounts.mean())
print("Highest Transaction:", amounts.max())
print("Lowest Transaction :", amounts.min())
print("Number of Transactions:", amounts.size)

import pandas as pd
data=pd.read_csv("data/transactions.csv")
print(data)
print(data.shape)
print(data["Amount"])
print(data["TransactionType"])
print(data["Amount"].sum())
print(data["Amount"].mean())
print(data["Amount"].max())
print(data["Amount"].min())
print(data["TransactionType"].value_counts())
print(data["Status"].value_counts())
print(data[data["TransactionType"]=="Deposit"]["Amount"].sum())
print(data[data["TransactionType"]=="Withdrawal"]["Amount"].sum())
print(data.head())
print(data.tail())
data.info()
print(data.describe())
print(data[data["Amount"]>3000])
print(data[data["Status"]=="Success"])
print(data[
    (data["TransactionType"]=="Deposit")&
    (data["Status"]=="Success")])
print(data[
    (data["TransactionType"]=="Withdrawal")&
    (data["Status"]=="Success")])
print(data.sort_values(by="Amount"))
print(data.sort_values(by="Amount", ascending=False).head(2))
print(data.isnull())
print(data.isnull().sum())
data.loc[2, "Amount"] = None

print(data)

print(data.dropna())

data.loc[2, "Amount"] = None

data["Amount"] = data["Amount"].fillna(data["Amount"].mean())

print(data)
print(data.groupby("TransactionType")["Amount"].sum())
print(data.groupby("Status")["Amount"].sum())
print(data.groupby(["TransactionType", "Status"])["Amount"].sum())
print(data.groupby(["TransactionType"])["Amount"].mean())
data["Amount"] = data["Amount"] * 1.1
print(data)
data["Amount_After_Fees"] = data["Amount"] * 1.1
print(data)
data["Risk_Level"] = data["Status"].apply(
    lambda x: "High" if x == "Failed" else "Low"
)

print(data)
import pandas as pd
data=pd.read_csv("data/transactions.csv")
data.to_csv("processed_transactions.csv", index=False)
print("File saved successfully")

total_transactions=len(data)
print("Total Transactions:", total_transactions)

total_amount=data["Amount"].sum()
print("Total Amount:", total_amount)
average_amount=data["Amount"].mean()
print("Average Amount:", average_amount)

print("\n===== FINANCIAL TRANSACTION REPORT =====")

print("Total Transactions:", total_transactions)
print("Total Amount:", total_amount)
print("Average Amount:", average_amount)
total_deposits = data[data["TransactionType"] == "Deposit"]["Amount"].sum()
total_withdrawals = data[data["TransactionType"] == "Withdrawal"]["Amount"].sum()

net_flow = total_deposits - total_withdrawals

print("\n===== NET FLOW ANALYSIS =====")
print("Net Flow:", net_flow)
failed_transactions = len(data[data["Status"] == "Failed"])

failed_rate = (failed_transactions / total_transactions) * 100

print("\n===== RISK ANALYSIS =====")
print("Failed Transactions:", failed_transactions)
print("Failed Rate:", failed_rate, "%")
status_summary = data["Status"].value_counts()

print("\n===== STATUS SUMMARY =====")
print(status_summary)
largest_transaction = data.loc[data["Amount"].idxmax()]

print("\n===== LARGEST TRANSACTION =====")
print(largest_transaction)
average_by_type = data.groupby("TransactionType")["Amount"].mean()

print("\n===== AVERAGE TRANSACTION BY TYPE =====")
print(average_by_type)
print("\n===== FINAL FINANCIAL SUMMARY =====")

print("\n===== FINANCIAL INSIGHTS =====")

print("Total Transactions:", total_transactions)
print("Total Amount:", total_amount)
print("Average Amount:", average_amount)
print("Net Flow:", net_flow)
print("Failed Rate:", failed_rate, "%")
print("Largest Transaction:", largest_transaction["Amount"])

print("\n===== FINANCIAL INSIGHTS =====")

if net_flow > 0:
    print("Insight: The financial flow is positive.")
else:
    print("Insight: The financial flow is negative.")

if failed_rate > 10:
    print("Risk Alert: High failed transaction rate.")
else:
    print("Risk Status: Failed transaction rate is under control.")

if total_deposits > total_withdrawals:
    print("Insight: Deposits are higher than withdrawals.")
else:
    print("Insight: Withdrawals are higher than deposits.")

data["RiskLevel"] = data["Status"].apply(
    lambda x: "High Risk" if x == "Failed" else "Low Risk"
)

print("\n===== RISK CLASSIFICATION =====")
print(data[["Status", "RiskLevel"]])

risk_summary = pd.pivot_table(
    data,
    index="TransactionType",
    columns="Status",
    values="Amount",
    aggfunc="count",
    fill_value=0
)

print("\n===== RISK SUMMARY BY TRANSACTION TYPE =====")
print(risk_summary)

sorted_data = data.sort_values(
    by="Amount",
    ascending=False
)

print("\n===== TRANSACTIONS SORTED BY AMOUNT =====")
print(sorted_data)

data["TransactionDate"] = pd.to_datetime(
    data["TransactionDate"]
)

print("\n===== TRANSACTION DATES =====")
print(data["TransactionDate"])

data["TransactionHour"] = data["TransactionDate"].dt.hour

print("\n===== TRANSACTION HOURS =====")
print(data[["TransactionDate", "TransactionHour"]])