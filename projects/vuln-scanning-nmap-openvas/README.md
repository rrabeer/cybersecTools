# Vulnerability Scanning — Nmap & OpenVAS

Prioritize risks from discovery to remediation aligned with NIST principles.

## Steps
1. Scope targets in your lab (document in `docs/scope.md`).
2. Run baseline Nmap scans (examples in `scans/nmap/commands.sh`).
3. Run OpenVAS full and fast scans; export results (summarize in `scans/openvas/findings-summary.md`).
4. Prioritize and write `docs/remediation-report.md`.

## Deliverables
- `docs/remediation-report.md` (aligned to NIST risk concepts)
- `scans/nmap/*` commands and sample output
- `scans/openvas/findings-summary.md`
