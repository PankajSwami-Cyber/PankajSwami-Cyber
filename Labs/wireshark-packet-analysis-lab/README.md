# Wireshark Packet Capture Analysis Lab

Hands-on Wireshark lab focused on packet inspection, display filtering, DNS analysis, and TCP/web traffic investigation.

## Overview

This project documents a Wireshark packet-analysis exercise using a sample `.pcap` capture from a web-browsing session. The lab demonstrates how a security analyst can move from a high-level packet list to detailed protocol fields and then use display filters to isolate traffic of interest.

## Objectives

* Open and review a packet capture in Wireshark
* Understand the main packet-list fields: No., Time, Source, Destination, Protocol, Length, and Info
* Inspect packet data across multiple protocol layers
* Filter traffic by IPv4 address and Ethernet MAC address
* Analyze UDP DNS queries and responses
* Filter TCP web traffic and search packet payloads for text

## Lab Tasks

### 1. Explore packet data

The capture was opened in Wireshark and reviewed at a high level. The packet list was used to identify different types of traffic, including DNS, TCP, HTTP, and ICMP packets.

### 2. Inspect a packet and its protocol layers

Traffic associated with the following IP address was filtered:

```text
ip.addr == 142.250.1.139
```

A TCP packet was then opened and examined through these protocol layers:

1. **Frame** — overall packet information such as frame length and arrival time
2. **Ethernet II** — source and destination MAC addresses and encapsulated protocol
3. **Internet Protocol Version 4** — source and destination IP addresses, Time to Live, and protocol
4. **Transmission Control Protocol** — source and destination ports, sequence information, and TCP flags

The TCP **Flags** section was also expanded for closer inspection.

## Display Filters Used

### IP address filters

```text
ip.addr == 142.250.1.139
ip.src == 142.250.1.139
ip.dst == 142.250.1.139
```

* `ip.addr` selects packets where the address is either the source or destination.
* `ip.src` selects packets originating from the specified address.
* `ip.dst` selects packets sent to the specified address.

### Ethernet MAC address filter

```text
eth.addr == 42:01:ac:15:e0:02
```

This filter selects traffic where the specified MAC address appears as the source or destination Ethernet address.

### DNS filter

```text
udp.port == 53
```

This filter isolates UDP traffic associated with DNS.

The lab inspected a DNS query for:

```text
opensource.google.com
```

The DNS response was then examined in the **Answers** section to view the addresses associated with the queried hostname.

### TCP/web traffic filter

```text
tcp.port == 80
```

This filter isolates TCP traffic associated with port 80, the default port used for HTTP web traffic.

The lab noted that the first packet in the filtered list had destination IP address:

```text
169.254.169.254
```

### TCP payload text search

```text
tcp contains "curl"
```

This filter searches TCP packet data for the text `curl` and was used to locate packets containing web requests made with the `curl` command in the sample capture.

## Key Findings from the Lab

* The capture contains multiple protocol types, including DNS, ICMP, TCP, and HTTP-related traffic.
* IP filtering can quickly reduce a large packet capture to traffic associated with a specific host.
* Ethernet, IPv4, and TCP fields provide different levels of detail for the same packet.
* DNS traffic can reveal both the hostname being queried and the addresses returned by the DNS response.
* TCP payload searches can help identify packets containing specific application-level text.

## Skills Demonstrated

* Wireshark packet capture analysis
* Network protocol inspection
* IPv4 and Ethernet analysis
* TCP and UDP display filtering
* DNS query/response analysis
* TCP payload text searching
* Basic network-investigation workflow

## Evidence

The screenshots and lab evidence are included in:

wireshark-lab-evidence.pdf

## Repository Structure

```text
wireshark-packet-analysis-lab/
├── README.md
└── wireshark-lab-evidence.pdf
```

## Lab Takeaway

This exercise provided practical experience using Wireshark to open saved packet captures, inspect protocol layers, apply targeted display filters, analyze DNS traffic, and search TCP payload data for relevant text. These are foundational packet-analysis skills for network monitoring and security investigations.
