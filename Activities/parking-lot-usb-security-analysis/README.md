# Parking Lot USB Security Analysis

## Overview

This project analyzes a simulated USB baiting scenario from both the attacker and defender perspectives.

The exercise examines how an unknown USB device can create security risks even when no obvious malicious files are opened. The analysis focuses on information exposure, social engineering opportunities, malware risks, and controls that organizations can use to reduce USB-related attacks.

## Scenario

A USB drive is discovered in a hospital parking lot with the organization's logo printed on it. The drive contains a mixture of personal and work-related files.

The device is investigated in an isolated virtual environment rather than being opened directly on a production workstation.

## Key Findings

### Contents

The USB drive contains personal information such as family and pet photos, as well as work-related documents including hiring, scheduling, resume, budget, and other organizational information.

### Attacker Mindset

An attacker could use personal information for social engineering, phishing, or targeted impersonation. Work-related information could help identify employees, understand organizational processes, and support attempts to gain unauthorized access.

### Risk Analysis

USB baiting can expose organizations to malware such as credential stealers, remote-access malware, ransomware, or other malicious code.

Recommended controls include:

- Restricting unauthorized USB devices
- Endpoint protection and removable-media scanning
- Security awareness training
- Policies requiring employees to report unknown USB devices
- Separating personal and business data
- Investigating suspicious removable media in isolated environments

## Security Concepts Demonstrated

- USB baiting
- Social engineering
- Personally identifiable information (PII)
- Malware delivery
- Attack surface analysis
- Security awareness
- Removable-media controls
- Defense in depth

## Lessons Learned

This exercise reinforced that a USB drive does not need to contain obvious malware to create a security risk. Information stored on removable media can itself become valuable intelligence for an attacker.

A strong security program therefore needs both technical controls and user awareness.

## Disclaimer

This repository contains a cybersecurity training exercise and does not contain real patient information, credentials, or confidential organizational data.
