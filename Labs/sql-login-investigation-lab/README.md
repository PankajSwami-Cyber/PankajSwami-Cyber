# SQL Login Investigation Lab

## Overview

This project demonstrates the use of SQL queries to investigate login activity as part of a cybersecurity incident investigation. Using MariaDB, I filtered authentication records based on dates, times, and event IDs to identify relevant login attempts during a simulated security incident.

The lab showcases practical SQL skills commonly used by Security Analysts and SOC Analysts when investigating authentication logs and security events.

---

## Scenario

A recent security incident required an investigation into user login activity. The objective was to retrieve specific login events by filtering records using SQL queries.

During this investigation, I:

- Retrieved login attempts made after a specific date.
- Filtered login attempts within a defined date range.
- Investigated login attempts that occurred during specific time periods.
- Filtered login attempts using Event IDs.
- Applied SQL comparison operators to retrieve accurate results.

---

## Objectives

- Filter login attempts made after a certain date.
- Filter login attempts within a date range.
- Filter login attempts before a specified time.
- Filter login attempts by Event ID.
- Practice using SQL comparison and filtering operators.
- Strengthen SQL skills for cybersecurity investigations.

---

## Technologies Used

- SQL
- MariaDB
- Linux Terminal
- Git
- GitHub

---

## SQL Concepts Covered

- SELECT
- WHERE
- BETWEEN
- ORDER BY
- LIMIT
- OFFSET
- Comparison Operators
- Date Filtering
- Time Filtering
- Numeric Filtering

---

## SQL Operators Used

| Operator | Description |
|----------|-------------|
| = | Equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |
| <> | Not equal to |
| BETWEEN | Filters values within a specified range |

---

## SQL Queries

### 1. Filter login attempts after a specific date

```sql
SELECT *
FROM log_in_attempts
WHERE login_date > '2022-05-09';
```

---

### 2. Filter login attempts on or after a specific date

```sql
SELECT *
FROM log_in_attempts
WHERE login_date >= '2022-05-09';
```

---

### 3. Filter login attempts within a date range

```sql
SELECT *
FROM log_in_attempts
WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11';
```

---

### 4. Filter login attempts before 7:00 AM

```sql
SELECT *
FROM log_in_attempts
WHERE login_time < '07:00:00';
```

---

### 5. Retrieve a limited number of login attempts before 7:00 AM

```sql
SELECT *
FROM log_in_attempts
WHERE login_time < '07:00:00'
LIMIT 1,4;
```

---

### 6. Filter login attempts between 6:00 AM and 7:00 AM

```sql
SELECT *
FROM log_in_attempts
WHERE login_time BETWEEN '06:00:00' AND '07:00:00';
```

---

### 7. Retrieve the earliest login attempt within the time range

```sql
SELECT *
FROM log_in_attempts
WHERE login_time BETWEEN '06:00:00' AND '07:00:00'
ORDER BY login_time
LIMIT 1;
```

---

### 8. Filter login attempts with Event ID greater than or equal to 100

```sql
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id >= 100;
```

---

### 9. Retrieve the first three matching Event IDs

```sql
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id >= 100
LIMIT 3;
```

---

### 10. Filter Event IDs within a specific range

```sql
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id BETWEEN 100 AND 150;
```

---

### 11. Retrieve records using LIMIT and OFFSET

```sql
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id BETWEEN 100 AND 150
LIMIT 1 OFFSET 6;
```

---

## Skills Demonstrated

- Writing SQL queries for cybersecurity investigations
- Filtering authentication logs using SQL
- Querying data using date and time conditions
- Working with numeric filters
- Using comparison operators effectively
- Applying LIMIT and OFFSET for result pagination
- Organizing and analyzing security event data
- Using MariaDB in a Linux environment

---

## Learning Outcomes

After completing this lab, I gained practical experience in:

- Investigating login events using SQL.
- Filtering records using dates, times, and numeric values.
- Applying SQL comparison operators to retrieve precise results.
- Using MariaDB to analyze authentication logs.
- Performing basic security log analysis to support incident investigations.

---

## Project Structure

```
sql-login-investigation-lab/
│
├── README.md
├── screenshots.pdf
```

---

## Future Improvements

- Perform more advanced SQL investigations using JOIN operations.
- Analyze multiple security-related tables.
- Create aggregate reports using GROUP BY.
- Build SQL queries for detecting suspicious login behavior.
- Explore SQL optimization techniques for large datasets.

---

## Acknowledgements

This project was completed as part of my cybersecurity learning journey to strengthen SQL skills used in Security Operations Center (SOC) investigations and incident response.

---

## Author

**Pankaj Swami**

Aspiring Cybersecurity Analyst

- GitHub: https://github.com/PankajSwami-Cyber/PankajSwami-Cyber
- LinkedIn: https://www.linkedin.com/in/pankajswamicyber/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2B45pB77MSRC1CyMu%2BBzVpw%3D%3D
