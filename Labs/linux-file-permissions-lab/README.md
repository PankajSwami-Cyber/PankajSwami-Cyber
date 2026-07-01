# Linux File Permission Management Lab

## Overview

This lab demonstrates how Linux file and directory permissions are used to enforce authorization and protect sensitive information.

Authorization is the process of granting users access only to the resources they are permitted to use. Without proper authorization controls, users could access, modify, or delete files that belong to other users or the system, creating significant security risks.

In this lab, I examined and modified permissions for files and directories located in:

```bash
/home/researcher2/projects
```

The user `researcher2` belongs to the `research_team` group.

As a security analyst, configuring and maintaining proper access permissions is essential for protecting sensitive information and maintaining the security of a system.

---

## Lab Objectives

* Examine file and directory permissions
* Identify incorrect permissions
* Modify permissions using Linux commands
* Restrict unauthorized access
* Verify permission changes
* Apply the principle of least privilege

---

## Environment

* Operating System: Linux
* Shell: Bash
* User: `researcher2`
* Group: `research_team`

---

## Tasks Performed

### 1. Check Permissions for Files in a Directory

First, I navigated to the projects directory and reviewed the permissions assigned to files.

#### Commands

```bash
pwd
ls
cd projects
ls -l
ls -la
```

---

### 2. Remove Unauthorized Write Access

The file `project_k.txt` allowed write access to others, which was not authorized.

#### Command

```bash
chmod o-w project_k.txt
```

#### Result

Write permission for others was removed, reducing the risk of unauthorized modification.

---

### 3. Remove Unauthorized Group Read Access

The file `project_m.txt` allowed group members to read the file when they should not have access.

#### Command

```bash
chmod g-r project_m.txt
```

#### Result

Group read access was removed, ensuring only authorized users could access the file.

---

### 4. Correct Permissions on a Hidden File

The hidden file `.project_x.txt` had incorrect permissions that did not align with the required authorization settings.

#### Command

```bash
chmod u-w,g-w,g+r .project_x.txt
```

#### Result

The file permissions were adjusted to prevent unauthorized modifications while maintaining appropriate access.

---

### 5. Remove Unauthorized Directory Access

The `drafts` directory granted execute permissions to the group, allowing access that was not authorized.

#### Command

```bash
chmod g-x drafts
```

#### Result

Group execute permission was removed, preventing unauthorized access to the directory.

---

## Complete Command List

```bash
pwd
ls
cd projects

ls -l
ls -la

chmod o-w project_k.txt
ls -l

chmod g-r project_m.txt
ls -l

chmod u-w,g-w,g+r .project_x.txt
ls -la

chmod g-x drafts
ls -l
```

---

## Security Concepts Demonstrated

### Authorization

Authorization determines which users are permitted to access specific resources within a system.

### File Permissions

Linux permissions control who can:

* Read files (`r`)
* Write to files (`w`)
* Execute files or access directories (`x`)

### Principle of Least Privilege

Users should be granted only the minimum permissions necessary to perform their tasks.

### Access Control

Proper permission management helps prevent unauthorized access, modification, and disclosure of sensitive information.

---

## Skills Demonstrated

* Linux Administration
* Bash Shell Commands
* File Permission Management
* Access Control
* Authorization
* Cybersecurity Fundamentals
* Security Operations
* Least Privilege Implementation
* Linux Security

---

## Key Takeaways

This lab provided hands-on experience with Linux authorization and permission management. By examining and modifying file and directory permissions, I reinforced the importance of access control and the principle of least privilege in maintaining system security.

Proper permission management is a fundamental cybersecurity skill that helps protect sensitive information from unauthorized access and modification.

---

## Author

**Pankaj Swami**

Cybersecurity Learner | Linux Administration | Security Operations
