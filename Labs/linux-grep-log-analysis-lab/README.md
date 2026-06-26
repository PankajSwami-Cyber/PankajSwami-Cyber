# Linux Log Analysis Using grep and Piping

## Overview

This project demonstrates the use of Linux command-line tools, specifically `grep` and piping (`|`), to search log files, locate specific information, and identify files based on naming patterns.

As a Security Analyst, efficiently searching logs and user records is an essential skill for investigating incidents, troubleshooting issues, and analyzing system activity.

---

## Scenario

In this lab, I worked with server log files and user report files to locate specific information.

The objectives were:

* Navigate through Linux directories
* Search for error messages in server logs
* Count occurrences of specific log entries
* Identify files matching specific naming conventions
* Search user data files for specific users and departments
* Use `grep` and piping to efficiently retrieve information

---

## Environment

* Operating System: Linux
* User Account: analyst
* Tools Used:

  * `pwd`
  * `ls`
  * `cd`
  * `grep`
  * Pipe Operator (`|`)

---

## Commands Performed

### Display Current Working Directory

```bash
pwd
```

### List Directory Contents

```bash
ls -la
```

### Navigate to the Logs Directory

```bash
cd logs
```

### View Files in the Logs Directory

```bash
ls -la
```

### Search for Error Messages in Server Logs

```bash
grep error server_logs.txt
```

### Count Error Messages

```bash
grep -c error server_logs.txt
```

**Result:**

```text
6
```

---

### Navigate to User Reports Directory

```bash
cd /home/analyst/reports/users
```

### Find Files Containing "Q1"

```bash
ls | grep Q1
```

**Output:**

```text
Q1_access.txt
Q1_added_users.txt
Q1_deleted_users.txt
```

### Count Q1 Files

```bash
ls | grep -c Q1
```

**Result:**

```text
3
```

---

### Find Access Report Files

```bash
ls | grep access
```

**Output:**

```text
Q1_access.txt
Q2_access.txt
Q3_access.txt
Q4_access.txt
```

### Count Access Report Files

```bash
ls | grep -c access
```

**Result:**

```text
4
```

---

### Search for User "jhill"

```bash
grep jhill Q2_deleted_users.txt
```

**Output:**

```text
1025    jhill    Sales
```

---

### Search for Human Resources Entries

```bash
grep "Human Resources" Q4_added_users.txt
```

**Output:**

```text
1151    sshah    Human Resources
1145    msosa    Human Resources
```

### Count Human Resources Entries

```bash
grep -c "Human Resources" Q4_added_users.txt
```

**Result:**

```text
2
```

---

## Skills Demonstrated

* Linux Command Line
* File System Navigation
* Log Analysis
* Data Searching with grep
* Pattern Matching
* Linux Pipelines
* Security Monitoring
* Security Operations Center (SOC) Fundamentals
* Incident Investigation Techniques

---

## Key Findings

* Located and reviewed error messages within server logs.
* Determined there were **6 error events** recorded.
* Identified **3 Q1 report files**.
* Identified **4 access report files**.
* Retrieved information for a specific deleted user account.
* Found and counted Human Resources users added during Q4.

---

## Screenshots

### Log Analysis and User Report Analysis


![screenshot20](https://github.com/PankajSwami-Cyber/PankajSwami-Cyber/blob/main/Labs/linux-grep-log-analysis/screenshots/20.png)

![secreenshot30](https://github.com/PankajSwami-Cyber/PankajSwami-Cyber/blob/main/Labs/linux-grep-log-analysis/screenshots/30.png)


## Lessons Learned

This lab reinforced the importance of command-line tools in cybersecurity operations. Using `grep` and piping enables analysts to quickly filter large amounts of data, identify relevant information, and investigate potential security events more efficiently.

---

## Author

**Pankaj Swami**

Aspiring Cybersecurity Analyst | Linux Enthusiast | SOC Analyst Learner

Connect with me on LinkedIn and GitHub to follow my cybersecurity learning journey.
