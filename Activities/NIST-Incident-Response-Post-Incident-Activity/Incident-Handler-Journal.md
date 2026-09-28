# Incident Handler's Journal

## Incident

Unauthorized access to customer PII and financial information.

## Date

September 22, 2026

## Detection / Initial Notification

At approximately 3:13 a.m. PT, an employee received an email claiming that customer data had been stolen. A second email later included sample stolen data and increased the payment demand.

The employee subsequently notified the security team.

## Investigation

The security team investigated the incident between September 22 and September 27, 2026.

The investigation identified a vulnerability in the e-commerce web application.

The attacker used a forced browsing technique by modifying the order number in a URL to access other customers' purchase confirmation pages.

## Evidence

Web application and web server logs showed a high volume of sequentially listed customer orders and access to thousands of purchase confirmation pages.

## Impact

Approximately 60,000 customer records were affected.

## Response

* Security investigation
* Web/application log analysis
* Breach disclosure to customers
* Free identity protection services for affected customers

## Recommendations

* Routine vulnerability scanning
* Penetration testing
* URL allowlisting
* Blocking unauthorized URL requests
* Authentication requirements for protected content

## Lessons Learned

Strong authorization controls, authentication, application security testing, and effective log monitoring are important defenses against unauthorized access to customer data.
