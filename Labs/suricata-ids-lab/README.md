# Suricata IDS Lab – Custom Rules, Alerts & Log Analysis

## Overview

This project documents a hands-on **Suricata Intrusion Detection System (IDS)** lab completed in a controlled environment.

The lab focused on understanding the components of Suricata rules, creating and testing custom rules against a packet capture, triggering alerts, and analyzing Suricata's `fast.log` and `eve.json` outputs.

The activity provided practical experience with **Suricata, Bash, packet capture analysis, IDS signatures, alert investigation, JSON processing, and network-flow correlation**.

---

## Objectives

* Examine the structure and components of a Suricata rule
* Understand Suricata rule actions, headers, and options
* Run Suricata against a sample PCAP file
* Trigger a custom IDS alert
* Examine alerts generated in `fast.log`
* Analyze detailed event data in `eve.json`
* Use `jq` to format and extract JSON fields
* Use `flow_id` to correlate events belonging to the same network flow

---

## Tools & Technologies

* **Suricata**
* **Linux / Bash shell**
* **jq**
* **PCAP packet capture**
* **Suricata IDS rules**
* **JSON log analysis**

---

## Lab Environment

The lab supplied the following files in the `/home/analyst` directory:

```text
custom.rules
sample.pcap
```

### File Purpose

**`sample.pcap`**
A packet capture containing example network traffic used to test Suricata rules.

**`custom.rules`**
A custom Suricata rule file used to define the traffic conditions that should generate alerts.

**`fast.log`**
A Suricata alert log containing a quick text-based representation of triggered alerts.

**`eve.json`**
Suricata's standard event log containing detailed event and alert information in JSON format.

---

# Task 1 – Examine a Custom Suricata Rule

The custom rule was examined using:

```bash
cat custom.rules
```

The rule uses the following structure:

```text
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"GET on wire"; flow:established,to_server; content:"GET"; sid:12345; rev:3;)
```

## Rule Components

### Action

The first component is:

```text
alert
```

The `alert` action instructs Suricata to generate an alert when the rule conditions are met.

Other Suricata actions discussed in the lab include:

```text
alert
drop
pass
reject
```

A `drop` action can also generate an alert while dropping the matching traffic when Suricata is running in IPS mode.

---

### Protocol

The rule uses:

```text
http
```

This means the rule applies to HTTP traffic.

---

### Source and Destination

```text
$HOME_NET any -> $EXTERNAL_NET any
```

The arrow indicates the direction of traffic:

```text
$HOME_NET  →  $EXTERNAL_NET
```

In this lab:

```text
$HOME_NET = 172.21.224.0/20
```

The `any` keyword means that traffic from any port in the specified network can be matched.

---

## Rule Options

### Message

```text
msg:"GET on wire"
```

The `msg` option specifies the alert message that appears when the rule triggers.

---

### Flow

```text
flow:established,to_server
```

This limits matching to established traffic traveling from the client toward the server.

---

### Content

```text
content:"GET"
```

The rule looks for the text:

```text
GET
```

in the HTTP method portion of the packet.

---

### Signature ID

```text
sid:12345
```

The `sid` identifies the rule with a unique numerical signature ID.

---

### Revision

```text
rev:3
```

The `rev` value identifies the revision of the rule.

---

## Rule Summary

The rule is designed to trigger an alert when Suricata observes an HTTP `GET` request traveling from the home network to the external network while the connection is established.

---

# Task 2 – Trigger the Custom Rule

The Suricata log directory was first examined using:

```bash
ls -l /var/log/suricata
```

Suricata was then run against the supplied PCAP using the custom rule file:

```bash
sudo suricata -r sample.pcap -S custom.rules -k none
```

### Command Options

| Option            | Purpose                                    |
| ----------------- | ------------------------------------------ |
| `-r sample.pcap`  | Processes the supplied packet capture file |
| `-S custom.rules` | Loads the custom Suricata rules            |
| `-k none`         | Disables checksum validation               |

After processing the PCAP, Suricata generated log files in:

```text
/var/log/suricata/
```

The generated files included:

```text
fast.log
eve.json
```

---

# Task 3 – Examine `fast.log`

The alert log was displayed using:

```bash
cat /var/log/suricata/fast.log
```

Each entry in `fast.log` represents an alert generated when the conditions of an alert rule were met.

The alert output includes information such as:

* Alert message
* Source information
* Destination information
* Traffic direction

The lab also notes that `fast.log` is considered a **deprecated format** and is not recommended for incident response or threat hunting, although it can still be useful for quick checks and quality-assurance tasks.

---

# Task 4 – Examine `eve.json`

Suricata's primary event log was examined using:

```bash
cat /var/log/suricata/eve.json
```

The raw JSON output contains significantly more information than `fast.log`.

Because raw JSON can be difficult to read, it was formatted with:

```bash
jq . /var/log/suricata/eve.json | less
```

This made the event information easier to inspect.

---

## Extract Specific Event Fields

The following command was used to extract selected fields:

```bash
jq -c "[.timestamp,.flow_id,.alert.signature,.proto,.dest_ip]" /var/log/suricata/eve.json
```

The selected fields were:

```text
timestamp
flow_id
alert.signature
proto
dest_ip
```

This provided a more focused view of the Suricata event data.

---

## Correlate Events Using `flow_id`

Suricata assigns a unique `flow_id` to each network flow.

Events belonging to the same flow share the same `flow_id`, making the field useful for correlating related network activity.

A specific flow can be selected with:

```bash
jq "select(.flow_id==X)" /var/log/suricata/eve.json
```

Replace `X` with the desired `flow_id` obtained from the previous query.

---

# Key Skills Practiced

This lab provided hands-on practice with:

```text
Suricata IDS rule analysis
Custom signature testing
PCAP-based traffic inspection
Network alert generation
fast.log analysis
eve.json analysis
jq JSON filtering
flow_id-based event correlation
Linux/Bash commands
```

---

# Investigation Workflow

The overall workflow used in this lab was:

```text
Sample PCAP
     │
     ▼
Custom Suricata Rule
     │
     ▼
Suricata Processing
     │
     ├──────────────► fast.log
     │
     └──────────────► eve.json
                           │
                           ▼
                         jq
                           │
                           ▼
                  Event Extraction
                           │
                           ▼
                   flow_id Correlation
```

---

# Evidence

Screenshots and supporting evidence from the lab are available.

Example project structure:

```text
suricata-ids-lab/
├── README.md
├── custom.rules
├── .gitignore
└── suricata-lab-evidence.pdf
```

---

# What I Learned

Through this exercise, I gained practical experience in understanding how an IDS rule is structured and how Suricata applies rules to network traffic.

I also practiced moving from **rule creation and testing** to **alert investigation and event correlation**, using both `fast.log` and the more detailed `eve.json` format.

The lab strengthened my familiarity with:

* Network security monitoring
* IDS signatures and rules
* Suricata alert analysis
* Linux command-line investigation
* JSON log analysis
* Network-flow correlation

---

## Disclaimer

This project was completed in a **controlled lab environment** using supplied sample data for educational purposes.

No production network traffic or confidential organizational data is intentionally included in this repository.
