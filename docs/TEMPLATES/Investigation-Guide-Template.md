# Packet Analysis Investigation Guide (Template)

## Goal
Walk through identifying suspicious DNS or beaconing traffic from PCAPs.

## Steps
1. Capture or import PCAP.
2. Apply baseline filters (see `filters.txt`).
3. Identify outliers (rare domains, high NXDOMAIN rate, unusual TTLs).
4. Pivot into WHOIS/OSINT (do not include secrets in the repo).
5. Document findings with timestamps and screenshots.

## Evidence Checklist
- PCAP location
- Filter(s) used
- Screenshots of streams/queries
- Domain/IP reputation notes
