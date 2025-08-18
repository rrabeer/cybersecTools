# SIEM (Splunk) — SSH Brute-Force Detection

Detect repeated failed SSH login attempts and simulate SOC response.

## Lab Summary
- **Goal:** Detect brute-force attempts via Splunk, build dashboards, and complete an IR report.
- **Data:** Linux `/var/log/auth.log` (sample provided).
- **Deliverables:** Saved searches, dashboard XML/JSON, incident report, playbook.

## Reproduce

1) **Ingest logs** into Splunk (forward sample in `data/sample_logs/ssh_failed.log`).
2) **Create a search** using SPL (see `splunk/saved_searches.spl`).
3) **Build a dashboard** from the search (see `splunk/dashboard_simple.xml`).
4) **Trigger a notable** (threshold-based) and complete `docs/incident-report.md`.

## Artifacts
- `splunk/saved_searches.spl`
- `splunk/dashboard_simple.xml`
- `docs/incident-report.md`
- `playbook.md`
- `data/sample_logs/ssh_failed.log`

> Replace sample logs with sanitized real lab data as you iterate.
