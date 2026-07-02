# SQL Security Analysis Lab: Filtering Data with AND, OR, and NOT

## Overview

This project demonstrates the use of SQL filtering techniques to retrieve security-related information from a MariaDB database. The lab focuses on using the **AND**, **OR**, and **NOT** operators to analyze login activity and employee information for common cybersecurity tasks.

As a Security Analyst, I used SQL queries to investigate login attempts, identify employees in specific departments, and filter records based on multiple conditions. These techniques are essential for security monitoring, incident investigations, and system administration.

---

## Scenario

In this lab, I was responsible for retrieving specific information about employees, their machines, and the departments they belong to from a company database.

The security team required this data to investigate potential security issues and identify computers that needed updates. To support these tasks, I used SQL queries with logical operators to filter and retrieve only the relevant records.

---

## Objectives

* Filter login attempts that occurred after business hours.
* Retrieve login attempts on specific dates.
* Filter login attempts based on location.
* Retrieve information about employees in specific departments.
* Exclude employees from a specific department.
* Practice using SQL logical operators to build more complex queries.

---

## Environment

* **Database:** MariaDB
* **Language:** SQL
* **Platform:** Linux Terminal (MariaDB Shell)

---

## SQL Skills Demonstrated

* SELECT
* FROM
* WHERE
* AND
* OR
* NOT
* LIKE
* LIMIT

---

## SQL Queries

### 1. Filter failed login attempts after business hours

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00'
AND success = FALSE;
```

---

### 2. Retrieve login attempts on specific dates

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
OR login_date = '2022-05-08';
```

---

### 3. Retrieve login attempts that did not originate in Mexico

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

---

### 4. View all employee records

```sql
SELECT *
FROM employees;
```

---

### 5. Retrieve Marketing employees located in the East office

```sql
SELECT *
FROM employees
WHERE department = 'Marketing'
AND office LIKE 'East%';
```

---

### 6. Retrieve employees in the Finance or Sales departments

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
OR department = 'Sales';
```

---

### 7. Retrieve a Sales employee username

```sql
SELECT username
FROM employees
WHERE department = 'Sales'
LIMIT 1;
```

---

### 8. Retrieve employees who are not in the Information Technology department

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

---

## Key Concepts Practiced

* Combining multiple conditions with **AND**
* Returning results that satisfy either of multiple conditions using **OR**
* Excluding records with **NOT**
* Pattern matching with **LIKE**
* Limiting query results with **LIMIT**
* Filtering database records for cybersecurity investigations

---

## What I Learned

Through this lab, I strengthened my understanding of SQL filtering techniques used in cybersecurity. I learned how logical operators can narrow search results, making it easier to analyze authentication logs and employee data efficiently.

These skills are valuable for:

* Security Operations Center (SOC) investigations
* Log analysis
* Incident response
* User activity monitoring
* Database querying
* Security auditing

---

## Repository Contents

```
sql-security-analysis-lab/
│
├── README.md
└── screenshots.pdf
```

---

## Technologies Used

* SQL
* MariaDB
* Linux
* Git
* GitHub

---

## Skills

* SQL
* Database Querying
* MariaDB
* Cybersecurity
* Security Analysis
* Log Analysis
* Data Filtering
* Linux
* GitHub

---

## Acknowledgment

This project was completed as part of a hands-on SQL lab focused on applying logical operators to solve real-world cybersecurity scenarios and strengthen database querying skills.

---

## Connect With Me

If you'd like to connect or view more of my cybersecurity projects, feel free to visit my GitHub profile and connect with me on LinkedIn.

**GitHub:** https://github.com/PankajSwami-Cyber/PankajSwami-Cyber/tree/main/Labs/sql-and-or-not-filtering-lab

**LinkedIn:** https://www.linkedin.com/in/pankajswamicyber/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BDKhjL3DlQYWNC9z6ELu38Q%3D%3D
