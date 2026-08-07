# Risk Assessment & Risk Register

## Project Overview

This project demonstrates the process of performing a qualitative cybersecurity risk assessment using a **risk register**. The assessment was conducted for a fictional commercial bank to identify potential security risks, evaluate their likelihood and impact, calculate risk scores, and prioritize remediation efforts.

This project was completed as part of the **Google Cybersecurity Professional Certificate** and follows the risk assessment process used in the **NIST Cybersecurity Framework (CSF)**.

---

## Scenario

As a member of a newly formed cybersecurity team at a commercial bank, I was tasked with evaluating the organization's operational environment and identifying the most significant cybersecurity risks.

The bank's environment includes:

- 100 on-premise employees
- 20 remote employees
- 2,000 individual customer accounts
- 200 commercial customer accounts
- Strict financial regulations requiring protection of customer data and financial assets

The objective was to assess each identified risk, determine its likelihood and severity, calculate a risk score, and prioritize risks for mitigation.

---

## Objectives

- Identify organizational assets and potential threats
- Evaluate vulnerabilities affecting business operations
- Assign likelihood and severity ratings
- Calculate overall risk scores
- Prioritize risks based on business impact
- Document findings using a professional risk register

---

## Risk Assessment Methodology

Each identified risk was evaluated using the following criteria:

- **Likelihood (1–3):** Probability that the risk will occur.
- **Severity (1–3):** Potential business impact if the risk occurs.
- **Risk Score:** Calculated using:

```
Risk Score = Likelihood × Severity
```

Higher scores indicate higher priority for mitigation.

---

## Risk Register Summary

| Asset | Risk | Likelihood | Severity | Risk Score | Priority |
|------|------|:----------:|:--------:|:----------:|----------|
| Funds | Business Email Compromise | 2 | 2 | 4 | Medium |
| Customer Database | Compromised User Database | 2 | 3 | 6 | High |
| Financial Records | Public Backup Database Exposure | 3 | 3 | 9 | Critical |
| Bank Safe | Theft | 1 | 3 | 3 | Low |
| Supply Chain | Natural Disaster Delays | 1 | 2 | 2 | Low |

The **Financial Records Leak** received the highest risk score due to the exposure of a publicly accessible backup database, making it the highest-priority risk for remediation.

---

## Key Findings

- Sensitive financial data requires strong protection because of regulatory requirements.
- Publicly accessible systems significantly increase organizational risk.
- Customer databases should be protected using strong encryption.
- Business email compromise remains a common threat that can expose confidential information.
- Risk prioritization helps security teams allocate resources effectively and address the most critical vulnerabilities first.

---

## Skills Demonstrated

- Cybersecurity Risk Assessment
- Risk Management
- Risk Register Development
- Vulnerability Assessment
- Threat Analysis
- Asset Identification
- Risk Prioritization
- Security Planning
- Information Security
- NIST Cybersecurity Framework (CSF)

---

## Tools & Frameworks

- Risk Register
- Risk Matrix
- NIST Cybersecurity Framework (CSF)
- Google Workspace

---

## Repository Structure

```
risk-assessment-risk-register/
│
├── README.md
├── Risk register.pdf
```

---

## Key Takeaways

This project strengthened my understanding of how cybersecurity professionals perform qualitative risk assessments by evaluating vulnerabilities, calculating risk scores, and prioritizing mitigation efforts. It also reinforced the importance of structured risk management in protecting organizational assets and supporting informed security decisions.

---

## References

- Google Cybersecurity Professional Certificate
- NIST Cybersecurity Framework (CSF)

---

## Author

**Pankaj Swami**

Aspiring Cybersecurity Analyst

- GitHub: https://github.com/PankajSwami-Cyber/PankajSwami-Cyber/tree/main
- LinkedIn: www.linkedin.com/in/pankajswamicyber
