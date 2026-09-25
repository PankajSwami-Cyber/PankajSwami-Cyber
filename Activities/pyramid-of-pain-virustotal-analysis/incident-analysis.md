# Incident Analysis

## Alert Summary

A suspicious spreadsheet attachment was delivered to an employee through email. The employee downloaded and opened the password-protected file, after which unauthorized executable files were created on the system.

An intrusion detection system subsequently generated an alert.

## Timeline

| Time      | Event                                               |
| --------- | --------------------------------------------------- |
| 1:11 p.m. | Employee received an email containing an attachment |
| 1:13 p.m. | Employee downloaded and opened the file             |
| 1:15 p.m. | Unauthorized executable files were created          |
| 1:20 p.m. | Intrusion detection system generated an alert       |

## File Indicator

SHA256:

`54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b`

## VirusTotal Analysis

### Detection

The VirusTotal detection results were reviewed to determine whether security vendors identified the file as malicious.

### Details

Additional file hashes and metadata were examined to identify other indicators associated with the artifact.

### Relations

Network relationships were examined to identify contacted domains and IP addresses.

### Behavior

Sandbox behavior was reviewed to identify file-system activity, processes, network activity, and MITRE ATT&CK techniques.

## Pyramid of Pain

The investigation identified three IoC categories:

| Pyramid of Pain Category | Indicator                          |
| ------------------------ | ---------------------------------- |
| Hash Value               | `287d612e29b71c90aa54947313810a25` |
| Domain Name              | `org.misecure.com`                 |
| IP Address               | `207.148.109.242`                  |

## Conclusion

The investigation demonstrated the process of using a file hash as a starting point for malware triage and then expanding the investigation to related indicators of compromise.

The findings were organized using the Pyramid of Pain framework to illustrate the different types of indicators that can be used for detection and response.
