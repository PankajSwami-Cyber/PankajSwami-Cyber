# SQL Database Query Lab

## Overview

This project demonstrates the use of SQL queries in MariaDB to retrieve, filter, and sort information from an organization's database. The lab focuses on querying employee device information and investigating login activity, tasks commonly performed by security analysts to support system maintenance and security monitoring.

---

## Scenario

In this lab, I worked with the `machines` and `log_in_attempts` tables in an organization database to complete the following tasks:

- Retrieve information about employee devices that require updates.
- Examine user login attempts for potential unusual activity.
- Sort query results using the `ORDER BY` clause.

---

## Objectives

- Retrieve data using the `SELECT` and `FROM` statements.
- Filter records using the `WHERE` clause.
- Limit returned results using the `LIMIT` clause.
- Sort data using `ORDER BY`.
- Practice SQL queries in the MariaDB shell.

---

## Tools & Technologies

- SQL
- MariaDB
- Linux Terminal
- Git & GitHub

---

## SQL Queries

### Retrieve all employee devices

```sql
SELECT *
FROM machines;
```

### Retrieve device IDs and email clients

```sql
SELECT device_id, email_client
FROM machines;
```

### Retrieve a specific email client

```sql
SELECT email_client
FROM machines
LIMIT 2,1;
```

### Retrieve operating system information

```sql
SELECT device_id, operating_system, OS_patch_date
FROM machines;
```

### Retrieve an operating system patch date

```sql
SELECT OS_patch_date
FROM machines
LIMIT 1;
```

### Retrieve login event IDs and countries

```sql
SELECT event_id, country
FROM log_in_attempts;
```

### Retrieve login attempts from Australia

```sql
SELECT country
FROM log_in_attempts
WHERE country = 'AUS';
```

### Retrieve usernames with login dates and times

```sql
SELECT username, login_date, login_time
FROM log_in_attempts;
```

### Retrieve a specific username

```sql
SELECT username
FROM log_in_attempts
LIMIT 4,1;
```

### Retrieve all login attempts

```sql
SELECT *
FROM log_in_attempts;
```

### Sort login attempts by date

```sql
SELECT *
FROM log_in_attempts
ORDER BY login_date;
```

### Sort login attempts by date and time

```sql
SELECT *
FROM log_in_attempts
ORDER BY login_date, login_time;
```

### Retrieve the earliest login attempt

```sql
SELECT username, login_date, login_time
FROM log_in_attempts
ORDER BY login_date, login_time
LIMIT 1;
```

---

## Skills Demonstrated

- SQL querying
- Database exploration
- Data retrieval
- Data filtering
- Data sorting
- MariaDB
- Security log analysis
- Investigating login activity
- Cybersecurity fundamentals

---

## Key Takeaways

Through this lab, I gained practical experience using SQL to query and analyze organizational data. I learned how to retrieve specific information from database tables, filter records, limit query results, and sort data efficiently. These are essential skills for security analysts who need to investigate system activity, identify devices requiring updates, and review authentication logs during security investigations.

---

## Repository Structure

```text
sql-database-query-lab/
│
├── README.md
└── screenshots.pdf
```

---

## Author

**Pankaj Swami**

GitHub: https://github.com/PankajSwami-Cyber/PankajSwami-Cyber

LinkedIn: https://www.linkedin.com/in/pankajswamicyber/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BmL6F16RqQrKaRIqWsek4Xw%3D%3D

Email Address: pankaj.swami.cyber@gmail.com
