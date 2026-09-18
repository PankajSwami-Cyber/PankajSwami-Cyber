# Phishing Email Analysis – ExecuTalk

## Overview

This project documents a phishing email investigation performed as a security analyst for a fictional investment firm, Imaginary Bank.

The simulated attack uses spear phishing and social engineering techniques to convince an executive to install collaboration software called ExecuTalk.

## Objectives

- Analyze the suspicious email
- Examine the sender and email header
- Identify social engineering and phishing indicators
- Investigate the software download links
- Determine whether the message should be allowed or quarantined

## Phishing Indicators Identified

### 1. Suspicious sender domain

The email claims to represent Imaginary Bank but was sent from:

`imaginarybank@gmail.org`

The organization's legitimate domain is:

`imaginarybank.com`

### 2. Spelling and grammar mistakes

Examples include:

- "Conglaturations"
- "Downlode"
- "You're team"
- "You are been added"
- "ecsecutiv's groups"

These errors are common indicators of suspicious messages.

### 3. Urgency

The message states that the invitation will expire in 48 hours and tells the recipient to act quickly.

### 4. Unexpected software installation

The executive was instructed to download ExecuTalk even though the software had not been discussed during the previous board meeting.

### 5. Suspicious download destination

The download links lead to:

`my.site.net/pwnexecs/`

The page requests a username and password and includes a "Continue with Google" option.

This behavior is consistent with a credential-phishing page.

## Investigation Result

**Disposition: QUARANTINE**

The email contains multiple indicators of spear phishing and should not be trusted.

## Skills Demonstrated

- Phishing analysis
- Email header analysis
- Social engineering identification
- Malicious URL investigation
- Credential-phishing detection
- Incident triage
- Security awareness

## Disclaimer

This is a simulated cybersecurity training scenario created for educational purposes.
