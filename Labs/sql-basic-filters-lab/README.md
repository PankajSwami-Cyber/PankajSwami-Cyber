# SQL Basic Filters Lab (MariaDB)

## Overview

This project demonstrates the use of basic SQL filtering techniques in MariaDB to retrieve security-related information from a relational database. The lab simulates common tasks performed by cybersecurity professionals, such as identifying machines by operating system, locating employees within specific departments, and filtering records based on office locations.

By applying SQL filters, security analysts can efficiently retrieve relevant information needed for system updates, security investigations, compliance activities, and incident response.

---

## Scenario

As a security analyst, I was responsible for querying a MariaDB database to retrieve specific information about employees, their assigned machines, and their departments. My team required this information to support several operational tasks, including:

- Identifying organization machines and their operating systems
- Finding machines running a specific operating system
- Locating employees in the Finance and Sales departments
- Retrieving employees based on office locations
- Supporting security-related investigations with targeted database queries

---

## Objectives

- Retrieve machine information from the database
- Filter machines by operating system
- Retrieve employees by department
- Filter employees by office location
- Apply SQL filtering techniques using `WHERE`
- Use pattern matching with `LIKE`
- Limit query results using `LIMIT`

---

## Technologies Used

- MariaDB
- SQL
- GitHub

---

## SQL Concepts Demonstrated

- `SELECT`
- `FROM`
- `WHERE`
- `LIKE`
- `LIMIT`

---

## SQL Queries

### 1. Return all machines and their operating systems

```sql
SELECT device_id, operating_system
FROM machines;
```

### 2. Return machines running OS 2

```sql
SELECT device_id, operating_system
FROM machines
WHERE operating_system = 'OS 2';
```

### 3. Return employees in the Finance department

```sql
SELECT *
FROM employees
WHERE department = 'Finance';
```

### 4. Return one employee from the Finance department

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
LIMIT 1;
```

### 5. Return employees in the Sales department

```sql
SELECT *
FROM employees
WHERE department = 'Sales';
```

### 6. Return employees located in office South-109

```sql
SELECT *
FROM employees
WHERE office = 'South-109';
```

### 7. Return employees whose office starts with "South"

```sql
SELECT *
FROM employees
WHERE office LIKE 'South%';
```

### 8. Return one employee whose office starts with "South"

```sql
SELECT *
FROM employees
WHERE office LIKE 'South%'
LIMIT 1;
```

---

## Skills Demonstrated

- SQL Query Development
- Database Filtering
- MariaDB
- Data Retrieval
- Relational Database Concepts
- Pattern Matching with SQL
- Cybersecurity Data Analysis
- Technical Documentation

---

## Key Takeaways

This lab strengthened my understanding of SQL filtering techniques and how they can be applied to retrieve targeted information from relational databases. Efficient querying is an essential skill for cybersecurity professionals, enabling faster analysis of employee and system data during investigations, vulnerability management, and routine security operations.

---

## Repository Structure

```
sql-basic-filters-lab/
│
├── README.md
└── screenshots.pdf
```

---

## Author

**Pankaj Swami**

Aspiring Cybersecurity Professional | SQL | MariaDB | Linux | Network Security

---

## License

This project is shared for educational and portfolio purposes.
