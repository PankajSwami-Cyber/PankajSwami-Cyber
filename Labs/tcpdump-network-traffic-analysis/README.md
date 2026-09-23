# TCPDump Network Traffic Capture and Analysis

## Overview

This project documents a hands-on Linux networking lab focused on capturing and analyzing network traffic using `tcpdump`.

The objective was to identify available network interfaces, capture live traffic, save traffic to a packet capture file, and filter packet data for analysis.

## Skills Demonstrated

* Linux command-line usage
* Network interface identification
* `tcpdump`
* Packet capture and filtering
* TCP/IP traffic analysis
* PCAP file analysis
* Hexadecimal and ASCII packet inspection
* HTTP traffic capture
* Basic network security analysis

## Lab Tasks

### 1. Identify Network Interfaces

Used:

```bash
sudo ifconfig
```

and:

```bash
sudo tcpdump -D
```

The available interfaces were reviewed to identify the interface used for packet capture.

## 2. Inspect Live Network Traffic

Used:

```bash
sudo tcpdump -i eth0 -v -c5
```

This captured five packets from the `eth0` interface and displayed detailed packet information.

The output included information such as:

* Packet timestamps
* IP information
* TCP information
* Source and destination systems
* Source and destination ports
* TCP flags
* Sequence and acknowledgment information
* Packet length

## 3. Capture Network Traffic to a PCAP File

Used:

```bash
sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &
```

HTTP traffic was generated with:

```bash
curl opensource.google.com
```

The resulting capture file was verified with:

```bash
ls -l capture.pcap
```

The `-nn` option was used to prevent address and port name resolution.

## 4. Analyze the Captured Traffic

Packet headers were examined with:

```bash
sudo tcpdump -nn -r capture.pcap -v
```

Extended packet information was examined with:

```bash
sudo tcpdump -nn -r capture.pcap -X
```

The `-X` option displayed packet contents in hexadecimal and ASCII formats.

## Key Takeaways

This lab provided practical experience with:

1. Identifying Linux network interfaces.
2. Capturing live network traffic with `tcpdump`.
3. Filtering traffic by network port.
4. Saving traffic to a PCAP file.
5. Reading packet captures for later analysis.
6. Examining hexadecimal and ASCII packet data.
7. Applying basic packet-analysis techniques used in security operations.

## Tools

* Linux
* Bash
* tcpdump
* curl
* PCAP

## Evidence

Screenshots showing the commands and analysis performed during the lab are included in the `screenshots.pdf` file.

> Note: Raw packet captures are intentionally excluded from this public repository to avoid unnecessarily exposing network information.
