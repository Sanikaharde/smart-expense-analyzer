import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/transactions.csv")

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

df["anomaly"] = model.fit_predict(df[["amount"]])

anomalies = df[df["anomaly"] == -1]

print("\n===== FRAUD / UNUSUAL TRANSACTIONS =====")

for _, row in anomalies.iterrows():

    print(
        f"""
User ID      : {row['user_id']}
Category     : {row['category']}
Amount       : ₹{row['amount']}
Description  : {row['description']}
---------------------------------------------------
"""
    )