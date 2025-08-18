# Incident Response Report — SSH Brute-Force (Simulated)

- **Incident ID:** IR-2025-SSH-001
- **Date/Time (UTC):** 2025-08-01 14:12
- **SOC Analyst:** Rabbani Rasha
- **Summary:** Multiple failed SSH login attempts indicate a possible brute-force from a single external IP.

## 1. Detection
- **Alert:** Saved search threshold (>=5 fails in 10m).
- **Indicators:** 203.0.113.45 (example), user: `root`, `admin`.
- **Timeline:** Spikes at 14:02–14:10 UTC.

## 2. Analysis
- Pattern consistent with credential stuffing. No successful logins observed.

## 3. Containment/Eradication/Recovery
- Containment: Block IP at perimeter; enable fail2ban.
- Eradication: N/A (no compromise).
- Recovery: Verify SSHD config; enforce key-based auth.

## 4. Lessons Learned
- Add MFA for bastion; shorten lockout window.
