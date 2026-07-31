import matplotlib.pyplot as plt
days=["Mon", "Tue", "Wed", "Thu", "Fri"]
sales=[1200,1500,1300,1800,2000]
plt.figure(figsize=(8,5))
plt.plot(days, sales, color="green", marker="o", linewidth=2)
plt.title("Daily Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("daily_sales.png")
plt.show()