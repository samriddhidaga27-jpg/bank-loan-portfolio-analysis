# Bank Loan Portfolio Analysis

## Overview

This project analyzes a bank loan dataset to understand loan applications, portfolio performance, and credit risk.

I worked with 38,576 loan records using SQL, Python, and Power BI. The analysis looks at loan amounts, loan status, interest rates, loan grades, DTI, and charge-offs.

The project also identifies a high-risk loan segment and compares its charge-off rate with the overall portfolio.

## Project Objectives

- Understand the overall loan portfolio
- Analyze loan applications by purpose and status
- Study charge-off patterns across different loan characteristics
- Compare risk across loan grades, DTI bands, and interest-rate bands
- Identify a high-risk group of loans
- Build a Power BI dashboard to present the findings

## Dataset

The dataset contains 38,576 loan records and 24 variables.

Some of the main variables used in the analysis are:

- Loan amount
- Loan status
- Loan grade and sub-grade
- Interest rate
- DTI
- Annual income
- Loan purpose
- Employment length
- Home ownership
- Issue date
- Payment information

The cleaned dataset used in the project is:

`financial_loan_clean.csv`

## Tools Used

**SQL**  
Used for data exploration, portfolio analysis, loan status analysis, charge-off analysis, and monthly trends.

**Python**  
Used for risk analysis and visualizations using Pandas and Matplotlib.

**Power BI**  
Used to create the final interactive dashboard.

## SQL Analysis

The SQL analysis includes:

- Basic data checks
- Loan status distribution
- Loan purpose analysis
- Loan grade analysis
- Interest-rate analysis
- Charge-off analysis
- Monthly loan trends
- Grade and purpose based analysis

SQL file:

`sql/bank_loan_analysis.sql`

## Python Analysis

Python was used to study charge-off rates across different loan characteristics, including:

- Loan grade
- DTI
- Annual income
- Sub-grade
- Interest rate
- Employment length
- Home ownership

A high-risk segment was also created by combining multiple risk indicators.

Python file:

`bank_loan_risk_analysis.py`

## Power BI Dashboard

The Power BI dashboard has two pages.

### Bank Loan Portfolio Analysis

- Total Applications
- Total Loan Amount
- Total Interest Amount
- Average Interest Rate
- Loan Applications by Purpose
- Loan Amount by Purpose
- Loan Status Distribution
- Loan Applications Over Time

### Bank Loan Risk Analysis

- Total Loans
- Charged-Off Loans
- Overall Charge-Off Rate
- High-Risk Loans
- High-Risk Charge-Off Rate
- High-Risk Loan Exposure
- Charge-Off Rate by Loan Grade
- Charge-Off Rate by DTI Band
- Charge-Off Rate by Interest Rate
- Overall vs High-Risk Charge-Off Rate

Power BI file:

`Bank_Loan_Analysis_Dashboard.pbix`

## Key Results

- Total loans analyzed: **38,576**
- Total loan amount: approximately **436M**
- Total interest amount: approximately **37M**
- Average interest rate: **12.05%**
- Charged-off loans: **5,330**
- Overall charge-off rate: **14.23%**
- High-risk loans: **748**
- High-risk loan exposure: approximately **13.32M**
- High-risk charge-off rate: **28.61%**

## Main Observations

Charge-off rates increased across the loan grades, with the higher-risk grades showing much higher charge-off rates.

Higher DTI bands also showed higher charge-off rates.

The analysis showed higher charge-off rates in the higher interest-rate bands.

The identified high-risk segment had a charge-off rate of **28.61%**, compared with **14.23%** for the overall portfolio.

## Project Structure

```text
bank-loan-portfolio-analysis/

├── Bank_Loan_Analysis_Dashboard.pbix
├── bank_loan_risk_analysis.py
├── financial_loan_clean.csv
├── README.md
│
└── sql/
    └── bank_loan_analysis.sql
