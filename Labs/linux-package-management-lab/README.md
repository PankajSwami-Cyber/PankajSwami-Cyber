# Linux Package Management Lab Using APT

## Overview

This project demonstrates the use of the Advanced Package Tool (APT) to manage software packages in a Linux environment. The lab was completed in a Qwiklabs environment using the Bash shell and focused on installing, uninstalling, verifying, and reinstalling network security applications commonly used by security analysts.

---

## Scenario

As a security analyst, it is important to understand how to install and manage security tools on Linux systems. In this lab, I used APT to install, remove, and verify the status of two network security applications: **Suricata** and **tcpdump**.

---

## Objectives

* Confirm APT is installed
* Install Suricata using APT
* Verify Suricata installation
* Uninstall Suricata
* Verify Suricata removal
* Install tcpdump using APT
* List installed packages
* Reinstall Suricata
* Verify both applications are installed

---

## Environment

* Platform: Qwiklabs
* Operating System: Linux
* Shell: Bash
* Package Manager: APT (Advanced Package Tool)

---

## Commands Used

### Confirm APT Installation

```bash
apt
```

### Install Suricata

```bash
sudo apt install suricata
```

### Verify Suricata Installation

```bash
suricata
```

### Remove Suricata

```bash
sudo apt remove suricata
```

### Verify Suricata Removal

```bash
suricata
```

### Install tcpdump

```bash
sudo apt install tcpdump
```

### List Installed Packages

```bash
apt list --installed
```

### Reinstall Suricata

```bash
sudo apt install suricata
```

### Final Verification

```bash
apt list --installed
```

---

## Results

### Task 1: Confirmed APT Installation

Verified that the APT package manager was installed and functioning correctly.

### Task 2: Installed Suricata

Successfully installed Suricata and its dependencies using APT.

### Task 3: Verified Installation

Confirmed that Suricata was available and operational.

### Task 4: Removed Suricata

Successfully removed Suricata from the system.

### Task 5: Verified Removal

Confirmed that Suricata was no longer available after uninstallation.

### Task 6: Installed tcpdump

Successfully installed tcpdump for packet capture and network traffic analysis.

### Task 7: Listed Installed Packages

Viewed installed packages using APT.

### Task 8: Reinstalled Suricata

Successfully reinstalled Suricata using APT.

### Task 9: Final Verification

Verified that both Suricata and tcpdump were installed on the system.

---

## Skills Demonstrated

* Linux Administration
* Bash Shell Operations
* Package Management with APT
* Software Installation and Removal
* System Verification
* Network Security Fundamentals
* Security Tool Deployment

---

## Tools Used

* Linux Bash
* APT (Advanced Package Tool)
* Suricata
* tcpdump
* Qwiklabs

---

## Screenshots

```markdown
![APT Installed](Labs/linux-package-management-lab/screenshots/2-APT-Installed.png)

![Installing Suricata](screenshots/02-install-suricata.png)

![Verifying Suricata](screenshots/03-verify-suricata.png)

![Installing tcpdump](screenshots/04-install-tcpdump.png)

![Final Verification](screenshots/05-final-verification.png)
```

---

## Key Takeaways

* Learned how to manage software packages using APT.
* Practiced installing and removing security applications in Linux.
* Verified application installation and removal through the command line.
* Gained hands-on experience with Suricata and tcpdump.
* Strengthened foundational Linux administration skills relevant to cybersecurity roles.

---

## Conclusion

This lab provided practical experience using APT to manage software packages in Linux. I successfully installed, removed, and reinstalled Suricata, installed tcpdump, and verified package status throughout the process. The exercise reinforced essential Linux administration and cybersecurity skills used by security analysts.

**Status: Completed Successfully ✅**
