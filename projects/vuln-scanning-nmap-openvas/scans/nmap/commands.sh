#!/usr/bin/env bash
set -euo pipefail

# Quick host discovery
nmap -sn 192.168.56.0/24 -oA scans/nmap/host-discovery

# Top ports + service/version detection
nmap -sS -sV --top-ports 100 192.168.56.101 -oA scans/nmap/top100

# Full TCP with scripts (be patient)
nmap -p- -sS -sV -sC 192.168.56.101 -oA scans/nmap/full_tcp

# Vulnerability NSE examples
nmap --script vuln -sV 192.168.56.101 -oA scans/nmap/vuln
