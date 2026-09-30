# Suricata IDS Lab

## Overview

This project documents a hands-on Suricata IDS lab in which I examined
custom Suricata rules, processed a PCAP file, triggered alerts, and
analyzed Suricata log output.

## Objectives

- Examine the structure of a Suricata rule
- Run Suricata against a packet capture
- Trigger a custom alert
- Examine fast.log
- Analyze eve.json
- Use jq to extract and correlate event data

## Tools Used

- Suricata
- Bash
- jq
- PCAP packet capture
- Linux

## Lab Workflow

### 1. Examine the custom rule

The custom rule used:

- `alert` action
- HTTP protocol
- `$HOME_NET` and `$EXTERNAL_NET`
- `flow:established,to_server`
- `content:"GET"`
- `sid:12345`
- `rev:3`

### 2. Process the PCAP

Command used:

```bash
sudo suricata -r sample.pcap -S custom.rules -k none
