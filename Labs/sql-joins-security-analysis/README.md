# SQL Joins Security Investigation

## Overview

This project demonstrates how SQL JOIN statements can be used to retrieve and correlate information stored across multiple relational database tables during a cybersecurity investigation.

Using the MariaDB shell, I analyzed relationships between **employees, machines, and login attempts** to gather information relevant to a simulated security incident involving compromised machines.

## Scenario

As a security analyst, I needed to investigate a recent security incident and retrieve information from multiple database tables.

Because the required information was stored separately, I used SQL JOINs to connect related records through shared columns.

The investigation focused on:

* Identifying which employees are assigned to specific machines
* Identifying machines that do not have an assigned employee
* Identifying employees who do not have an assigned machine
* Connecting employees with their login attempts

## Objectives

The main objectives of this lab were to:

1. Use an **INNER JOIN** to find information about employees and their machines.
2. Use a **LEFT JOIN** to identify machines without an assigned employee.
3. Use a **RIGHT JOIN** to identify employees without an assigned machine.
4. Use an **INNER JOIN** to identify login attempts associated with employees.

## Database Tables

The investigation used three relational database tables:

| Table             | Description                                           |
| ----------------- | ----------------------------------------------------- |
| `machines`        | Contains information about organizational machines    |
| `employees`       | Contains employee information and machine assignments |
| `log_in_attempts` | Contains information about login attempts             |

### Shared Columns

The tables were connected using shared fields:

* `machines.device_id` ↔ `employees.device_id`
* `employees.username` ↔ `log_in_attempts.username`

These shared columns allowed me to correlate information across the different tables.

---

## SQL Queries

### 1. View the Machines Table

Before performing the joins, I reviewed the contents of the `machines` table.

```sql
SELECT *
FROM machines;
```

This provided an overview of the available machine records and helped identify the fields that could be used to connect the table with employee information.

---

### 2. INNER JOIN — Employees and Machines

I used an INNER JOIN to identify employees associated with specific machines.

```sql
SELECT *
FROM machines
INNER JOIN employees
    ON machines.device_id = employees.device_id;
```

An **INNER JOIN** returns only records where a matching value exists in both tables.

In this investigation, the query connects machine records with employee records using the `device_id` column.

This helps determine **which employees are using which machines**.

---

### 3. LEFT JOIN — Machines and Employees

I used a LEFT JOIN to return all machines and any matching employee information.

```sql
SELECT *
FROM machines
LEFT JOIN employees
    ON machines.device_id = employees.device_id;
```

A **LEFT JOIN** returns every record from the left table (`machines`) and matching records from the right table (`employees`).

This is useful for identifying **machines that do not have a corresponding employee assignment**.

---

### 4. RIGHT JOIN — Employees and Machines

I used a RIGHT JOIN to return all employees and any matching machine information.

```sql
SELECT *
FROM machines
RIGHT JOIN employees
    ON machines.device_id = employees.device_id;
```

A **RIGHT JOIN** returns every record from the right table (`employees`) and matching records from the left table (`machines`).

This helps identify **employees who do not have a corresponding machine assignment**.

---

### 5. INNER JOIN — Employees and Login Attempts

Finally, I used an INNER JOIN to connect employees with their login attempts.

```sql
SELECT *
FROM employees
INNER JOIN log_in_attempts
    ON employees.username = log_in_attempts.username;
```

This query connects employee records with login attempt records using the `username` column.

The resulting information can help a security analyst associate **login activity with specific employee accounts** during an investigation.

---

## Security Investigation Relevance

SQL JOINs are useful for security analysts because important investigation data is often distributed across multiple database tables.

For example, during an incident investigation, an analyst may need to determine:

* Which employee was assigned to a potentially compromised machine
* Which machines do not have an assigned user
* Which employees do not have an assigned machine
* Which login attempts are associated with employee accounts
* How different pieces of information relate to one another

By joining related tables, an analyst can build a more complete picture of activity within an organization's environment.

---

## Key Takeaways

Through this lab, I practiced:

* Writing SQL queries in MariaDB
* Using `INNER JOIN`
* Using `LEFT JOIN`
* Using `RIGHT JOIN`
* Identifying shared columns between relational tables
* Combining information from multiple database tables
* Analyzing employee-to-machine relationships
* Connecting employees to login activity
* Applying SQL to a simulated cybersecurity investigation

## Tools & Technologies

* **MariaDB**
* **SQL**
* **Relational Databases**
* **SQL JOINs**
* **GitHub**

## Project Structure

```text
sql-joins-security-analysis/
│
├── README.md
└── screenshots.pdf
```

## Conclusion

This lab strengthened my understanding of how SQL JOINs can be used to correlate information across relational database tables.

From a cybersecurity perspective, the ability to connect machine, employee, and login information is valuable when investigating security incidents and analyzing potentially suspicious activity.

This project is part of my ongoing cybersecurity learning and portfolio development.
