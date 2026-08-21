# Data Leak Analysis Using NIST SP 800-53 AC-6

## 📌 Project Overview

This project analyzes a simulated data leak at an educational technology company that develops an application to help teachers automatically grade assignments.

The application handles information collected from academic institutions, instructors, parents, and students. The analysis focuses on protecting **information privacy** and applying the **principle of least privilege** to reduce the risk of unauthorized data exposure.

---

## 🔎 Incident Summary

A customer success representative received access to a folder of internal documents from a manager. The folder contained files related to a new product offering, including customer analytics and marketing materials.

The manager forgot to revoke access to the internal folder. Later, during a sales call, the representative intended to share a link to marketing materials with an external business partner but accidentally shared a link to the entire internal folder.

The business partner subsequently posted the link on social media, exposing internal business information.

---

## ⚠️ Issues Identified

The incident was caused by several weaknesses in data handling:

* Access to the internal folder was broader than necessary.
* The manager did not revoke access after the folder was no longer needed.
* The representative accidentally shared the entire folder instead of the intended marketing materials.
* An external business partner received access to internal documents.
* Sensitive information was not sufficiently protected through least-privilege controls.

---

## 🛡️ Security Framework

The company used the **NIST Cybersecurity Framework (CSF)** to address information security and data privacy concerns.

The relevant area of the security plan is:

**Function:** Protect
**Category:** PR.DS — Data Security
**Subcategory:** PR.DS-5 — Protections Against Data Leaks
**Reference:** NIST SP 800-53 AC-6

The worksheet identifies NIST SP 800-53 as the guideline used for the controls protecting against data leaks.

---

## 🔐 NIST SP 800-53 AC-6 — Least Privilege

NIST SP 800-53 AC-6 focuses on **Least Privilege**.

The control states that users should receive only the minimum access and authorization required to complete a task or function.

Processes, user accounts, and roles should be enforced to prevent users from operating at privilege levels greater than those necessary to accomplish business objectives.

### Control Enhancements

The AC-6 resource identifies several enhancements that can strengthen least privilege:

* Restrict access to sensitive resources based on user role.
* Automatically revoke access to information after a period of time.
* Keep activity logs of provisioned user accounts.
* Regularly audit user privileges.

---

## ✅ Recommended Improvements

### 1. Restrict Access Based on User Role

Sensitive resources should only be accessible to users whose roles require that information.

This would reduce the number of employees who can access confidential internal documents and help prevent unnecessary exposure.

### 2. Automatically Revoke Access After a Period of Time

Temporary access to sensitive information should automatically expire after it is no longer required.

This would reduce the risk of forgotten permissions remaining active after meetings, projects, or other business activities.

---

## 🎯 Expected Security Benefits

Implementing these enhancements would strengthen the company's least-privilege approach.

Role-based restrictions can reduce unnecessary access to sensitive information, while automatic access revocation can prevent outdated permissions from remaining active. Together, these controls can reduce the likelihood of accidental data exposure and similar data leaks.

---

## 🧠 Skills Demonstrated

* Cybersecurity
* Information Security
* Information Privacy
* Access Control
* Least Privilege
* Risk Assessment
* Data Leak Analysis
* Security Controls
* NIST Cybersecurity Framework
* NIST SP 800-53
* Data Loss Prevention

---

## 📚 References

* **NIST SP 800-53 — AC-6: Least Privilege**
* **NIST Cybersecurity Framework (CSF)**
* **PR.DS-5: Protections Against Data Leaks**

---

## 📁 Project Files

```text
data-leak-analysis-nist-ac6/
│
├── README.md
└── data-leak-worksheet.pdf
```

---

## ⚠️ Disclaimer

This project is based on a simulated educational cybersecurity scenario. It does not contain confidential company information, real customer data, credentials, or proprietary business information.

---

## 📈 Project Outcome

This project demonstrates how a data leak can result from excessive access, failure to revoke permissions, and accidental sharing of sensitive resources.

Applying the principle of least privilege through appropriate access restrictions and timely access revocation can help organizations strengthen information privacy and reduce the risk of future data leaks.

Github - 

Linkedin - 
