# Linux File Navigation and Log Analysis Lab

## Overview

This lab demonstrates fundamental Linux command-line skills used in cybersecurity and system administration. The objective was to navigate a Linux file system, locate specific files, and analyze their contents using common shell commands.

As a security analyst, the ability to work efficiently in a Linux environment without a graphical user interface (GUI) is essential for investigating systems, reviewing logs, and managing files remotely.

---

## Scenario

In this lab, I explored the `/home/analyst` directory structure and gathered information from various files.

The tasks completed included:

1. Identifying the current working directory.
2. Listing files and directories with detailed permissions.
3. Navigating through subdirectories.
4. Viewing user-related records stored in a text file.
5. Accessing server log files and reviewing log entries.

---

## Commands Used

```bash
pwd
ls -la
cd reports
ls -la
cd users
ls -la
cat Q1_added_users.txt
cd /home/analyst/logs
ls -la
head server_logs.txt
```

---

## Directory Navigation

### Display Current Directory

```bash
pwd
```

Output:

```text
/home/analyst
```

### List Files and Directories

```bash
ls -la
```

This command displayed all files and directories, including hidden files, along with permissions, ownership, and timestamps.

---

## User Records Analysis

### Navigate to User Reports

```bash
cd reports
cd users
```

### View Added Users

```bash
cat Q1_added_users.txt
```

The file contained the following user records:

| Employee ID | Username | Department             |
| ----------- | -------- | ---------------------- |
| 1001        | bmoreno  | Marketing              |
| 1026        | apatel   | Human Resources        |
| 1041        | cgriffin | Sales                  |
| 1104        | mreed    | Information Technology |
| 1177        | aezra    | Human Resources        |
| 1188        | noshiro  | Finance                |

---

## Log Analysis

### Navigate to Logs Directory

```bash
cd /home/analyst/logs
```

### View the First 10 Log Entries

```bash
head server_logs.txt
```

Sample log events included:

* Successful user logins
* Incorrect username attempts
* Incorrect password attempts
* File storage utilization warnings
* Password expiration notifications

Examples:

```text
info     User logged on successfully
error    The password is incorrect
warning  The file storage is 75% full
warning  The current user's password expires in 15 days
```

---

## Skills Demonstrated

* Linux Command Line Interface (CLI)
* File System Navigation
* Directory Management
* User Record Analysis
* Log File Investigation
* Cybersecurity Fundamentals
* Security Operations Center (SOC) Concepts

---

## Key Takeaways

This lab reinforced the importance of Linux navigation and log analysis skills in cybersecurity. By using basic shell commands, I was able to locate files, review user information, and analyze system log data efficiently in a command-line environment.

---

## Tools Used

* Linux Shell (Bash)
* Command-Line Utilities

  * `pwd`
  * `ls`
  * `cd`
  * `cat`
  * `head`

---

## Author

**[Pankaj Swami]**

Aspiring Cybersecurity Analyst | Linux Enthusiast | SOC Analyst Learner
