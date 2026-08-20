CREATE DATABASE bank_loan_analysis;
USE bank_loan_analysis;
CREATE TABLE loans (
    id INT PRIMARY KEY,
    address_state VARCHAR(10),
    application_type VARCHAR(50),
    emp_length VARCHAR(50),
    emp_title VARCHAR(255),
    grade VARCHAR(5),
    home_ownership VARCHAR(30),
    issue_date DATE,
    last_credit_pull_date DATE,
    last_payment_date DATE,
    loan_status VARCHAR(50),
    next_payment_date DATE,
    member_id BIGINT,
    purpose VARCHAR(100),
    sub_grade VARCHAR(10),
    term VARCHAR(30),
    verification_status VARCHAR(50),
    annual_income DECIMAL(15,2),
    dti DECIMAL(10,4),
    installment DECIMAL(12,2),
    int_rate DECIMAL(10,4),
    loan_amount INT,
    total_acc INT,
    total_payment INT
);

SELECT COUNT(*) AS total_records
FROM loans;
SELECT COUNT(DISTINCT id) AS unique_ids
FROM loans;

SELECT SUM(loan_amount) AS total_loan_amount
FROM loans;

SELECT COUNT(*) AS total_applications
FROM loans;

SELECT ROUND(AVG(loan_amount), 2) AS avg_loan_amount
FROM loans;

SELECT ROUND(AVG(int_rate) * 100, 2) AS avg_interest_rate_pct
FROM loans;

SELECT ROUND(AVG(annual_income), 2) AS avg_annual_income
FROM loans;

SELECT
    loan_status,
    COUNT(*) AS number_of_loans,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM loans), 2) AS percentage
FROM loans
GROUP BY loan_status
ORDER BY number_of_loans DESC;

SELECT
    purpose,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY purpose
ORDER BY total_loan_amount DESC;

SELECT
    address_state,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY address_state
ORDER BY total_loan_amount DESC;

SELECT
    home_ownership,
    COUNT(*) AS number_of_loans,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY home_ownership
ORDER BY total_loan_amount DESC;

SELECT
    emp_length,
    COUNT(*) AS number_of_loans,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY emp_length
ORDER BY total_loan_amount DESC;

SELECT
    grade,
    COUNT(*) AS number_of_loans,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY grade
ORDER BY grade;

SELECT
    grade,
    ROUND(AVG(int_rate) * 100, 2) AS avg_interest_rate_pct
FROM loans
GROUP BY grade
ORDER BY grade;

SELECT
    grade,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS charged_off,
    ROUND(
        SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS default_rate_pct
FROM loans
GROUP BY grade
ORDER BY default_rate_pct DESC;

SELECT
    purpose,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS charged_off,
    ROUND(
        SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS default_rate_pct
FROM loans
GROUP BY purpose
ORDER BY default_rate_pct DESC;

SELECT
    address_state,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS charged_off,
    ROUND(
        SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS default_rate_pct
FROM loans
GROUP BY address_state
ORDER BY default_rate_pct DESC;

SELECT
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS charged_off_loans,
    ROUND(
        SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS default_rate_pct
FROM loans;

SELECT
    DATE_FORMAT(issue_date, '%Y-%m') AS loan_month,
    COUNT(*) AS number_of_loans,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY DATE_FORMAT(issue_date, '%Y-%m')
ORDER BY loan_month;

SELECT
    home_ownership,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS charged_off,
    ROUND(
        SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS default_rate_pct
FROM loans
GROUP BY home_ownership
ORDER BY default_rate_pct DESC;

SELECT
    emp_length,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS charged_off,
    ROUND(
        SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS default_rate_pct
FROM loans
GROUP BY emp_length
ORDER BY default_rate_pct DESC;

SELECT
    grade,
    purpose,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS charged_off,
    ROUND(
        SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS default_rate_pct,
    ROUND(AVG(int_rate) * 100, 2) AS avg_interest_rate_pct
FROM loans
GROUP BY grade, purpose
HAVING COUNT(*) >= 100
ORDER BY default_rate_pct DESC;
