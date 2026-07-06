-- ============================================================
-- SQL Queries for Security Investigation
-- ============================================================

-- 1. Retrieve failed login attempts after business hours (after 18:00)

SELECT *
FROM log_in_attempts
WHERE login_time > '18:00'
  AND success = FALSE;


-- 2. Retrieve login attempts on May 8, 2022, and May 9, 2022

SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
   OR login_date = '2022-05-08';


-- 3. Retrieve login attempts outside of Mexico

SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';


-- 4. Retrieve employees in the Marketing department located in the East building

SELECT *
FROM employees
WHERE department = 'Marketing'
  AND office LIKE 'East%';


-- 5. Retrieve employees in the Finance or Sales departments

SELECT *
FROM employees
WHERE department = 'Finance'
   OR department = 'Sales';


-- 6. Retrieve employees not in the Information Technology department

SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
