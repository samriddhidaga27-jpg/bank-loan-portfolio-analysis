import pandas as pd

df = pd.read_csv("financial_loan_clean.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- LOAN STATUS ---")
print(df["loan_status"].value_counts())

# --------------------------------------------------
# RISK ANALYSIS
# --------------------------------------------------

# Loans with a final outcome
completed_loans = df[
    df["loan_status"].isin(["Fully Paid", "Charged Off"])
]

# Overall charge-off rate
charge_off_rate = (
    (completed_loans["loan_status"] == "Charged Off").mean() * 100
)

print("\n--- OVERALL RISK ---")
print(f"Charge-Off Rate: {charge_off_rate:.2f}%")

# Average loan characteristics by loan status
print("\n--- LOAN CHARACTERISTICS BY STATUS ---")

status_analysis = completed_loans.groupby("loan_status").agg(
    Average_Loan_Amount=("loan_amount", "mean"),
    Average_Interest_Rate=("int_rate", "mean"),
    Average_Annual_Income=("annual_income", "mean"),
    Average_DTI=("dti", "mean"),
    Number_of_Loans=("id", "count")
)

print(status_analysis)

# --------------------------------------------------
# RISK BY LOAN GRADE
# --------------------------------------------------

grade_risk = completed_loans.groupby("grade").agg(
    Total_Loans=("id", "count"),
    Charged_Off=("loan_status", lambda x: (x == "Charged Off").sum()),
    Average_Interest_Rate=("int_rate", "mean"),
    Average_DTI=("dti", "mean")
)

grade_risk["Charge_Off_Rate"] = (
    grade_risk["Charged_Off"] / grade_risk["Total_Loans"] * 100
)

grade_risk = grade_risk.sort_index()

print("\n--- RISK BY LOAN GRADE ---")
print(grade_risk)

# --------------------------------------------------
# RISK BY LOAN PURPOSE
# --------------------------------------------------

purpose_risk = completed_loans.groupby("purpose").agg(
    Total_Loans=("id", "count"),
    Charged_Off=("loan_status", lambda x: (x == "Charged Off").sum()),
    Average_Loan_Amount=("loan_amount", "mean"),
    Average_Interest_Rate=("int_rate", "mean")
)

purpose_risk["Charge_Off_Rate"] = (
    purpose_risk["Charged_Off"] / purpose_risk["Total_Loans"] * 100
)

purpose_risk = purpose_risk.sort_values(
    "Charge_Off_Rate",
    ascending=False
)

print("\n--- RISK BY LOAN PURPOSE ---")
print(purpose_risk)

# --------------------------------------------------
# RISK BY DEBT-TO-INCOME (DTI)
# --------------------------------------------------

completed_loans["DTI_Band"] = pd.cut(
    completed_loans["dti"],
   bins=[-float("inf"), 0.10, 0.20, 0.30, 0.40, float("inf")],
    labels=["<10", "10-20", "20-30", "30-40", "40+"]
)

dti_risk = completed_loans.groupby(
    "DTI_Band",
    observed=False
).agg(
    Total_Loans=("id", "count"),
    Charged_Off=("loan_status", lambda x: (x == "Charged Off").sum()),
    Average_Loan_Amount=("loan_amount", "mean"),
    Average_Interest_Rate=("int_rate", "mean")
)

dti_risk["Charge_Off_Rate"] = (
    dti_risk["Charged_Off"] /
    dti_risk["Total_Loans"] * 100
)

print("\n--- RISK BY DTI ---")
print(dti_risk)

# --------------------------------------------------
# RISK BY ANNUAL INCOME
# --------------------------------------------------

completed_loans["Income_Band"] = pd.cut(
    completed_loans["annual_income"],
    bins=[0, 30000, 50000, 75000, 100000, 150000, float("inf")],
    labels=[
        "<30K",
        "30K-50K",
        "50K-75K",
        "75K-100K",
        "100K-150K",
        "150K+"
    ],
    include_lowest=True
)

income_risk = completed_loans.groupby(
    "Income_Band",
    observed=False
).agg(
    Total_Loans=("id", "count"),
    Charged_Off=("loan_status", lambda x: (x == "Charged Off").sum()),
    Average_Loan_Amount=("loan_amount", "mean"),
    Average_Interest_Rate=("int_rate", "mean")
)

income_risk["Charge_Off_Rate"] = (
    income_risk["Charged_Off"] /
    income_risk["Total_Loans"] * 100
)

print("\n--- RISK BY ANNUAL INCOME ---")
print(income_risk)

# --------------------------------------------------
# RISK BY LOAN SUB-GRADE
# --------------------------------------------------

subgrade_risk = completed_loans.groupby("sub_grade").agg(
    Total_Loans=("id", "count"),
    Charged_Off=("loan_status", lambda x: (x == "Charged Off").sum()),
    Average_Interest_Rate=("int_rate", "mean"),
    Average_DTI=("dti", "mean")
)

subgrade_risk["Charge_Off_Rate"] = (
    subgrade_risk["Charged_Off"] /
    subgrade_risk["Total_Loans"] * 100
)

subgrade_risk = subgrade_risk.sort_values(
    "Charge_Off_Rate",
    ascending=False
)

print("\n--- RISK BY LOAN SUB-GRADE ---")
print(subgrade_risk)

# --------------------------------------------------
# RISK BY INTEREST RATE
# --------------------------------------------------

completed_loans["Interest_Rate_Band"] = pd.cut(
    completed_loans["int_rate"] * 100,
    bins=[0, 8, 12, 16, 20, float("inf")],
    labels=["<8%", "8-12%", "12-16%", "16-20%", "20%+"],
    include_lowest=True
)

interest_rate_risk = completed_loans.groupby(
    "Interest_Rate_Band",
    observed=False
).agg(
    Total_Loans=("id", "count"),
    Charged_Off=("loan_status", lambda x: (x == "Charged Off").sum()),
    Average_Loan_Amount=("loan_amount", "mean"),
    Average_DTI=("dti", "mean")
)

interest_rate_risk["Charge_Off_Rate"] = (
    interest_rate_risk["Charged_Off"] /
    interest_rate_risk["Total_Loans"] * 100
)

print("\n--- RISK BY INTEREST RATE ---")
print(interest_rate_risk)

# --------------------------------------------------
# RISK BY EMPLOYMENT LENGTH
# --------------------------------------------------

employment_risk = completed_loans.groupby("emp_length").agg(
    Total_Loans=("id", "count"),
    Charged_Off=("loan_status", lambda x: (x == "Charged Off").sum()),
    Average_Loan_Amount=("loan_amount", "mean"),
    Average_Interest_Rate=("int_rate", "mean")
)

employment_risk["Charge_Off_Rate"] = (
    employment_risk["Charged_Off"] /
    employment_risk["Total_Loans"] * 100
)

print("\n--- RISK BY EMPLOYMENT LENGTH ---")
print(employment_risk)

# --------------------------------------------------
# RISK BY HOME OWNERSHIP
# --------------------------------------------------

home_ownership_risk = completed_loans.groupby("home_ownership").agg(
    Total_Loans=("id", "count"),
    Charged_Off=("loan_status", lambda x: (x == "Charged Off").sum()),
    Average_Loan_Amount=("loan_amount", "mean"),
    Average_Interest_Rate=("int_rate", "mean"),
    Average_DTI=("dti", "mean")
)

home_ownership_risk["Charge_Off_Rate"] = (
    home_ownership_risk["Charged_Off"] /
    home_ownership_risk["Total_Loans"] * 100
)

home_ownership_risk = home_ownership_risk.sort_values(
    "Charge_Off_Rate",
    ascending=False
)

print("\n--- RISK BY HOME OWNERSHIP ---")
print(home_ownership_risk)

high_risk = completed_loans[
    (completed_loans["grade"].isin(["E", "F", "G"])) &
    (completed_loans["dti"] > 0.20) &
    (completed_loans["int_rate"] > 0.16)
].copy()

high_risk_charge_off_rate = (
    (high_risk["loan_status"] == "Charged Off").mean() * 100
)

print("\n--- COMBINED HIGH-RISK SEGMENT ---")
print("Number of high-risk loans:", len(high_risk))
print(f"Charge-Off Rate: {high_risk_charge_off_rate:.2f}%")
print(
    "Total Loan Amount:",
    f"${high_risk['loan_amount'].sum():,.0f}"
)

# --------------------------------------------------
# RISK SUMMARY
# --------------------------------------------------

risk_summary = pd.DataFrame({
    "Metric": [
        "Total Loans",
        "Completed Loans",
        "Charged-Off Loans",
        "Overall Charge-Off Rate",
        "High-Risk Segment Loans",
        "High-Risk Segment Charge-Off Rate",
        "High-Risk Segment Loan Amount"
    ],
    "Value": [
        len(df),
        len(completed_loans),
        (completed_loans["loan_status"] == "Charged Off").sum(),
        charge_off_rate,
        len(high_risk),
        high_risk_charge_off_rate,
        high_risk["loan_amount"].sum()
    ]
})

print("\n--- RISK SUMMARY ---")
print(risk_summary)

# --------------------------------------------------
# VISUALIZATION: CHARGE-OFF RATE BY LOAN GRADE
# --------------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.bar(
    grade_risk.index,
    grade_risk["Charge_Off_Rate"]
)

plt.xlabel("Loan Grade")
plt.ylabel("Charge-Off Rate (%)")
plt.title("Historical Charge-Off Rate by Loan Grade")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# CHECK HIGH-RISK CONDITIONS
# --------------------------------------------------

print("\n--- HIGH-RISK CONDITION CHECK ---")

print(
    "Grade E/F/G:",
    len(completed_loans[
        completed_loans["grade"].isin(["E", "F", "G"])
    ])
)

print(
    "DTI > 20%:",
    len(completed_loans[
        completed_loans["dti"] > 0.20
    ])
)

print(
    "Interest Rate > 16%:",
    len(completed_loans[
        completed_loans["int_rate"] > 0.16
    ])
)

print(
    "Grade E/F/G + DTI > 20%:",
    len(completed_loans[
        (completed_loans["grade"].isin(["E", "F", "G"])) &
        (completed_loans["dti"] > 0.20)
    ])
)

print(
    "All 3 conditions:",
    len(completed_loans[
        (completed_loans["grade"].isin(["E", "F", "G"])) &
        (completed_loans["dti"] > 0.20) &
        (completed_loans["int_rate"] > 0.16)
    ])
)

# --------------------------------------------------
# VISUALIZATION: CHARGE-OFF RATE BY DTI BAND
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    dti_risk.index.astype(str),
    dti_risk["Charge_Off_Rate"]
)

plt.xlabel("Debt-to-Income (DTI) Band")
plt.ylabel("Charge-Off Rate (%)")
plt.title("Historical Charge-Off Rate by DTI Band")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# VISUALIZATION: CHARGE-OFF RATE BY INTEREST RATE
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    interest_rate_risk.index.astype(str),
    interest_rate_risk["Charge_Off_Rate"]
)

plt.xlabel("Interest Rate Band")
plt.ylabel("Charge-Off Rate (%)")
plt.title("Historical Charge-Off Rate by Interest Rate")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# VISUALIZATION: OVERALL VS HIGH-RISK CHARGE-OFF RATE
# --------------------------------------------------

comparison_labels = [
    "Overall Portfolio",
    "High-Risk Segment"
]

comparison_rates = [
    charge_off_rate,
    high_risk_charge_off_rate
]

plt.figure(figsize=(7, 5))

plt.bar(
    comparison_labels,
    comparison_rates
)

plt.ylabel("Charge-Off Rate (%)")
plt.title("Overall vs High-Risk Charge-Off Rate")

plt.tight_layout()
plt.show()