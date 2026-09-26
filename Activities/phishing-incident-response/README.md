# Phishing Incident Response – SOC Investigation

## Overview

This project documents a simulated phishing incident investigation completed as part of a Security Operations Center (SOC) training activity.

The alert involved a suspected phishing email containing a password-protected executable attachment. The attachment's SHA-256 hash had previously been verified as malicious, so the incident required escalation according to the phishing response playbook.

## Incident Summary

* **Alert ID:** A-2703
* **Alert type:** Phishing attempt / possible malware download
* **Severity:** Medium
* **Attachment:** `bfsvc.exe`
* **Disposition:** Escalated
* **Escalation:** Level-2 SOC analyst

## Investigation Process

The investigation followed a phishing-response workflow:

1. Reviewed the alert severity and email details.
2. Examined the sender, recipient, subject, message body, and attachment.
3. Identified inconsistencies in the sender information and grammatical errors in the message.
4. Confirmed that an attachment was present.
5. Used the previously investigated file hash to establish that the attachment was malicious.
6. Determined that the alert required escalation.
7. Updated the alert disposition to Escalated and documented the investigation findings.

## Indicators of Phishing

Several characteristics supported the phishing assessment:

* Inconsistent sender identity and email information.
* Grammatical errors in the subject and message body.
* A password-protected executable attachment.
* The attachment was confirmed to be malicious by its SHA-256 hash.
* The alert was classified as Medium severity.

## Response

The alert was escalated to a Level-2 SOC analyst for further investigation and response.

## Skills Demonstrated

* Phishing analysis
* Security alert triage
* Incident response
* Threat intelligence
* IOC/hash analysis
* SOC documentation
* Escalation procedures

## Note

This repository contains sanitized educational material. Sensitive information, credentials, identifying email/IP information, course-restricted materials, and executable malware samples are intentionally excluded.
