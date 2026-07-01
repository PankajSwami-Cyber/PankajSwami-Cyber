# Linux File Management Lab

## Overview

This project demonstrates fundamental Linux file and directory management skills using the Bash shell. The objective was to organize the `/home/analyst` directory by creating, removing, moving, and editing files while maintaining proper directory structure and documenting completed tasks.

## Scenario

In this lab, I was responsible for ensuring that the `/home/analyst` directory was properly organized. To accomplish this, I performed several file management operations and documented the updates made to the directory structure.

## Objectives

* Create a new directory
* Remove an existing directory
* Move files between directories
* Delete unnecessary files
* Create and edit files using the Nano text editor
* Verify changes using Linux commands

---

## Tasks Completed

### 1. Created a New Directory

Created a directory named `logs` inside the `/home/analyst` directory.

```bash
mkdir logs
```

### 2. Removed an Unnecessary Directory

Removed the `temp` directory.

```bash
rmdir temp
```

### 3. Moved a File

Moved `Q3patches.txt` from the `notes` directory to the `reports` directory.

```bash
mv Q3patches.txt /home/analyst/reports/
```

### 4. Deleted a File

Removed the obsolete file `tempnotes.txt`.

```bash
rm tempnotes.txt
```

### 5. Created a New File

Created a task tracking file named `tasks.txt`.

```bash
touch tasks.txt
```

### 6. Edited a File Using Nano

Used the Nano text editor to add documentation to the file.

```bash
nano tasks.txt
```

### 7. Verified File Contents

Displayed the contents of the file to confirm the changes.

```bash
cat tasks.txt
```

Output:

```text
Completed tasks

1. Managed file structure in /home/analyst
```

---

## Commands Used

```bash
pwd
mkdir logs
ls
rmdir temp
ls
cd notes
ls
mv Q3patches.txt /home/analyst/reports/
ls /home/analyst/reports
rm tempnotes.txt
ls
touch tasks.txt
ls
nano tasks.txt
clear
cat tasks.txt
```

---

## Skills Demonstrated

* Linux Command Line Interface (CLI)
* Linux File Management
* Directory Management
* Bash Shell Navigation
* Nano Text Editor
* System Administration Fundamentals
* File Organization and Maintenance

---

## Learning Outcomes

Through this lab, I learned how to:

* Navigate Linux directories efficiently
* Create and remove directories
* Move and delete files safely
* Create and edit text files using Nano
* Verify file contents using command-line tools
* Maintain an organized Linux file structure
* Apply basic Linux administration practices

---

## Author

**Pankaj Swami**

<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="pankaj-swami-726806416" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/pankaj-swami-726806416?trk=profile-badge">Pankaj Swami</a></div>
              

Aspiring Cybersecurity Professional | Linux Learner | SOC Analyst Enthusiast

### Connect With Me

* LinkedIn: [ www.linkedin.com/in/pankajswamicyber ]
* GitHub: [ https://github.com/PankajSwami-Cyber/PankajSwami-Cyber/tree/main ]
