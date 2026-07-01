# Linux User Management Lab

## Overview

This lab demonstrates fundamental Linux user and group management using Bash commands. The objective was to create and manage a user account, assign group memberships, modify file ownership, and safely remove the user from the system.

## Objectives

* Create a new user account
* Change the user's primary group
* Change ownership of a project file
* Add the user to a supplementary group
* Delete the user account
* Remove the unused user group

## Commands Used

```bash
# Create a new user
sudo useradd researcher9

# Change the user's primary group
sudo usermod -g research_team researcher9

# Change ownership of the project file
sudo chown researcher9 /home/researcher2/projects/project_r.txt

# Add the user to a supplementary group
sudo usermod -a -G sales_team researcher9

# Delete the user account
sudo userdel researcher9

# Remove the unused user group
sudo groupdel researcher9
```

## Verification

The commands completed the following tasks successfully:

* Created the user **researcher9**
* Assigned **research_team** as the primary group
* Changed ownership of **project_r.txt**
* Added the user to the **sales_team** supplementary group
* Deleted the user account
* Removed the leftover user group

> **Note:** During user deletion, the following message appeared:

```text
userdel: group researcher9 not removed because it is not the primary group of user researcher9.
```

This behavior is expected because the user's primary group had already been changed to **research_team**. The remaining **researcher9** group was removed afterward using:

```bash
sudo groupdel researcher9
```

## Skills Demonstrated

* Linux Administration
* Bash Shell
* User Management
* Group Management
* File Ownership
* Access Control
* Authentication Fundamentals
* Command-Line Operations

## Repository Structure

```
linux-user-management-lab/
│── README.md
└── screenshots.pdf
```

## Author

**Pankaj Swami**

Learning Linux system administration and cybersecurity through hands-on labs and practical exercises.
