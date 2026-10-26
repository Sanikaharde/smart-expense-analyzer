import pandas as pd

df = pd.read_csv("data/transactions.csv")

print("\n===== TOTAL SPENDING =====")
print(df["amount"].sum())

print("\n===== AVERAGE TRANSACTION =====")
print(df["amount"].mean())

print("\n===== SPENDING BY CATEGORY =====")
print(df.groupby("category")["amount"].sum())

print("\n===== TOP SPENDERS =====")
print(
    df.groupby("user_id")["amount"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== HIGHEST TRANSACTION =====")
print(df.loc[df["amount"].idxmax()])