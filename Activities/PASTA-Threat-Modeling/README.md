# PASTA Threat Modeling – Sneaker Marketplace App

## Overview

This project demonstrates a threat modeling exercise using the **Process of Attack Simulation and Threat Analysis (PASTA)** framework.

The scenario involves a mobile application that connects sneaker buyers and sellers and handles user accounts, messaging, product listings, seller ratings, and payment processing.

## Objectives

The threat model focuses on:

* Protecting user privacy and sensitive information
* Securing buyer and seller accounts
* Protecting payment-related information
* Identifying threats and vulnerabilities before application launch
* Recommending security controls to reduce risk

## PASTA Analysis

### Stage I – Business and Security Objectives

* Connect buyers and sellers through user accounts, messaging, and seller ratings.
* Protect user privacy and handle user information responsibly.
* Process sales efficiently while supporting secure payment handling and legal requirements.

### Stage II – Technical Scope

Technologies considered include:

* Application Programming Interface (API)
* Public Key Infrastructure (PKI)
* SHA-256
* Structured Query Language (SQL)

SQL was prioritized because the application uses a database for sneaker listings and seller information. SQL injection is also identified as an attack path in the provided attack tree.

### Stage III – Application Decomposition

The data-flow diagram represents a product-search process that interacts with the user database and returns current sneaker inventory listings.

### Stage IV – Threat Analysis

Identified threats:

1. SQL injection
2. Session hijacking

### Stage V – Vulnerability Analysis

Identified vulnerabilities:

1. Lack of prepared statements
2. Weak login credentials

### Stage VI – Attack Modeling

The attack paths examined include:

* User data → SQL injection → Lack of prepared statements
* User data → Session hijacking → Weak login credentials

### Stage VII – Security Controls

Recommended controls:

1. Prepared statements and input validation
2. Strong authentication and secure session management
3. PKI/TLS encryption for data in transit
4. Encryption and access controls for sensitive data

## Skills Demonstrated

* Threat modeling
* PASTA framework
* Attack-tree analysis
* Data-flow analysis
* Vulnerability identification
* Security controls
* Application security
* Risk analysis

## Project Artifact

The completed PASTA worksheet is available in this repository:

`PASTA Worksheet.pdf`

## Disclaimer

This project is an educational threat modeling exercise based on a fictional sneaker marketplace application. It is not a production security assessment.
