# Apply Filters to SQL Queries

## Project Overview

This project demonstrates how SQL filtering techniques can be used to investigate potential security incidents and identify employee devices that require security updates. Using the `log_in_attempts` and `employees` tables, I wrote SQL queries to retrieve specific records based on login times, dates, locations, and departments. This project was completed as part of the **Google Cybersecurity Professional Certificate**.

---

## Objectives

- Investigate failed login attempts after business hours.
- Analyze login activity on specific dates related to a security incident.
- Identify login attempts originating outside of Mexico.
- Locate employee devices that require security updates.
- Practice applying SQL filtering techniques for cybersecurity investigations.

---

## Skills Demonstrated

- SQL
- Database Querying
- Cybersecurity Log Analysis
- Security Investigation
- Data Filtering
- Pattern Matching
- Logical Operators

---

## SQL Concepts Used

- `SELECT`
- `FROM`
- `WHERE`
- `AND`
- `OR`
- `NOT`
- `LIKE`
- Wildcards (`%`)
- Date Filtering
- Time Filtering

---

## Project Tasks

### 1. Retrieve After-Hours Failed Login Attempts

Filtered failed login attempts that occurred after **18:00** using the `AND` operator.

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00'
AND success = FALSE;
```

---

### 2. Retrieve Login Attempts on Specific Dates

Retrieved login attempts that occurred on **2022-05-08** and **2022-05-09** using the `OR` operator.

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
OR login_date = '2022-05-08';
```

---

### 3. Retrieve Login Attempts Outside of Mexico

Used `NOT` with `LIKE` to exclude records from Mexico. The wildcard `%` matches both `MEX` and `MEXICO`.

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

---

### 4. Retrieve Marketing Employees in the East Building

Used `AND` and `LIKE` to identify Marketing employees whose office locations begin with "East".

```sql
SELECT *
FROM employees
WHERE department = 'Marketing'
AND office LIKE 'East%';
```

---

### 5. Retrieve Employees in Finance or Sales

Used the `OR` operator to return employees from either department.

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
OR department = 'Sales';
```

---

### 6. Retrieve Employees Not in Information Technology

Used the `NOT` operator to identify employees outside the Information Technology department.

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

---

## Files Included

- `README.md` – Project overview and documentation
- `sql_queries.sql` – SQL queries used in the project
- `apply_filters_to_sql_queries.pdf` – Completed project report

---

## Key Takeaways

Through this project, I strengthened my ability to use SQL to support cybersecurity investigations. I practiced filtering records using logical operators (`AND`, `OR`, `NOT`), pattern matching with `LIKE` and the `%` wildcard, and filtering data by dates and times. These techniques are essential for analyzing security logs, investigating suspicious activity, and identifying systems that require security updates.

---

## Technologies Used

- SQL
- MariaDB
- Git
- GitHub

---

## Author

**Pankaj Swami**

Google Cybersecurity Professional Certificate
