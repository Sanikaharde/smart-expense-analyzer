import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/transactions.csv")

# -----------------------------
# PAGE TITLE
# -----------------------------
st.set_page_config(
    page_title="Smart Expense Analyzer",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Smart Expense Analyzer")
st.markdown("AI & ML Powered FinTech Analytics Dashboard")

# -----------------------------
# KPI SECTION
# -----------------------------
st.header("📊 Financial Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Spending",
        f"₹{df['amount'].sum():,.0f}"
    )

with col2:
    st.metric(
        "Average Transaction",
        f"₹{df['amount'].mean():,.0f}"
    )

# -----------------------------
# CATEGORY ANALYSIS
# -----------------------------
category_df = (
    df.groupby("category")["amount"]
    .sum()
    .reset_index()
)

st.header("🍕 Spending by Category")

fig1 = px.pie(
    category_df,
    names="category",
    values="amount",
    title="Expense Distribution by Category"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# USER ANALYSIS
# -----------------------------
user_df = (
    df.groupby("user_id")["amount"]
    .sum()
    .reset_index()
)

st.header("👤 Spending by User")

fig2 = px.bar(
    user_df,
    x="user_id",
    y="amount",
    title="Top Spenders",
    color="amount"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# MONTHLY TREND
# -----------------------------
st.header("📈 Monthly Spending Trend")

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

monthly_df = (
    df.groupby(
        df["transaction_date"].dt.to_period("M")
    )["amount"]
    .sum()
    .reset_index()
)

monthly_df["transaction_date"] = (
    monthly_df["transaction_date"]
    .astype(str)
)

fig3 = px.line(
    monthly_df,
    x="transaction_date",
    y="amount",
    markers=True,
    title="Monthly Spending Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# EXTRA KPI SECTION
# -----------------------------
top_category = category_df.loc[
    category_df["amount"].idxmax()
]

top_user = user_df.loc[
    user_df["amount"].idxmax()
]

st.header("🏆 Highlights")

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "Highest Spending Category",
        top_category["category"]
    )

with col4:
    st.metric(
        "Top Spender",
        f"User {int(top_user['user_id'])}"
    )

# -----------------------------
# MACHINE LEARNING
# -----------------------------
st.header("🚨 ML Anomaly Detection")

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

df["anomaly"] = model.fit_predict(
    df[["amount"]]
)

anomalies = df[
    df["anomaly"] == -1
]

st.metric(
    "Total Anomalies Detected",
    len(anomalies)
)

st.dataframe(
    anomalies[
        [
            "user_id",
            "category",
            "amount",
            "description"
        ]
    ],
    use_container_width=True
)

# -----------------------------
# ML INSIGHTS
# -----------------------------
st.subheader("🤖 ML Insights")

for _, row in anomalies.iterrows():

    st.warning(
        f"User {row['user_id']} made an unusual "
        f"{row['category']} transaction of "
        f"₹{row['amount']:,} "
        f"({row['description']})"
    )

# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------
st.header("💡 Business Insights")

st.success(
    f"""
    ✅ Total spending across all users is ₹{df['amount'].sum():,}

    ✅ Highest spending category: {top_category['category']}

    ✅ Top spender: User {int(top_user['user_id'])}

    ✅ {len(anomalies)} unusual transactions detected

    ✅ Travel and Shopping contribute the highest-value transactions
    """
)


  # -----------------------------
# AI ASSISTANT
# -----------------------------



st.header("🤖 AI Assistant")

question = st.text_input(
    "Ask a question about your spending"
)

if question:

    question = question.lower()

    if "top spender" in question or "who spent the most" in question:

        st.success(
            f"User {int(top_user['user_id'])} is the top spender with ₹{int(top_user['amount']):,}."
        )

    elif "highest category" in question or "highest spending category" in question:

        st.success(
            f"{top_category['category']} is the highest spending category with ₹{int(top_category['amount']):,} spent."
        )

    elif "total spending" in question:

        st.success(
            f"Total spending across all users is ₹{int(df['amount'].sum()):,}."
        )

    elif "average transaction" in question:

        st.success(
            f"The average transaction amount is ₹{df['amount'].mean():.2f}."
        )

    elif "anomalies" in question or "suspicious transactions" in question:

        st.success(
            f"{len(anomalies)} unusual transactions were detected."
        )

    elif "top category" in question:

        st.success(
            f"{top_category['category']} is the top spending category."
        )

    elif "top transaction" in question:

        highest = df.loc[df["amount"].idxmax()]

        st.success(
            f"The largest transaction is ₹{highest['amount']:,} for {highest['description']}."
        )

    elif "how many users" in question:

        st.success(
            f"There are {df['user_id'].nunique()} users in the dataset."
        )

    else:

        st.warning(
            "Sorry, I don't know how to answer that yet. Try asking about top spender, highest category, total spending, top transaction, anomalies or how many users."
        )