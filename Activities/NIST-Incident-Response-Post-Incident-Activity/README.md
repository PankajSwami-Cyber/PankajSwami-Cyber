# NIST Incident Response – Post-Incident Activity

## Overview

This project documents my review of an incident final report as part of cybersecurity and Security Operations Center (SOC) training.

The purpose of this activity was to understand the post-incident phase of the NIST Incident Response Lifecycle and identify:

1. What happened
2. When it happened
3. What response actions were taken
4. What recommendations were made to prevent recurrence

## Incident Summary

According to the final report, the organization experienced a security incident on September 22, 2026. An attacker gained unauthorized access to customer personally identifiable information (PII) and financial information.

Approximately 60,000 customer records were affected.

The root cause was a vulnerability in the organization's e-commerce web application. The attacker was able to perform a forced browsing attack by modifying the order number contained in a purchase confirmation URL. This allowed access to other customers' purchase confirmation pages and exposed customer transaction data.

## Timeline

| Date / Time                       | Event                                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------- |
| September 22, 2026 – 3:13 a.m. PT | Employee received an email claiming customer data had been stolen.                 |
| September 22, 2026                | A second email included sample stolen data and increased the payment demand.       |
| September 22, 2026                | Employee notified the security team.                                               |
| September 22–27, 2026             | Security team investigated the attack and determined the extent of the data theft. |

## Root Cause

The root cause was an e-commerce web application vulnerability that allowed an attacker to access customer transaction information by changing order numbers in URLs.

Web server and application logs showed an exceptionally high volume of sequential customer orders and access to thousands of purchase confirmation pages.

## Response Actions

The organization:

* Investigated the incident.
* Reviewed web application and web server logs.
* Determined how the data was accessed and exfiltrated.
* Worked with the public relations department to disclose the breach to customers.
* Offered free identity protection services to affected customers.

## Recommendations

The final report recommended:

* Routine vulnerability scanning.
* Penetration testing.
* URL allowlisting.
* Blocking requests outside approved URL ranges.
* Requiring authentication before users can access protected content.

## Key Lessons Learned

This incident demonstrates the importance of:

* Secure authorization controls in web applications.
* Proper authentication and access controls.
* Routine vulnerability assessments and penetration testing.
* Effective log monitoring and anomaly detection.
* Thorough post-incident documentation.
* Reviewing application behavior for unauthorized sequential access.

## Skills Demonstrated

* Incident analysis
* Incident timeline development
* Root-cause analysis
* Log analysis concepts
* Vulnerability identification
* Incident response documentation
* NIST Incident Response Lifecycle concepts
* Security recommendations

## Disclaimer

This repository contains my educational analysis of an incident final report. It does not contain confidential company information or credentials.
