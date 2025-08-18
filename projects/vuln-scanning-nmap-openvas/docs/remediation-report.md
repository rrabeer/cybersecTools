# Remediation Report (Aligned to NIST)

## Executive Summary
This report prioritizes remediation based on likelihood and impact.

## Prioritized Findings
1. **SMB Signing Not Required** — *High*
   - **Risk:** MITM/relay risk on SMB.
   - **Recommendation:** Enforce SMB signing; disable NTLMv1.
   - **Validation:** Re-scan confirms policy in effect.

2. **Outdated OpenSSH** — *Medium*
   - **Risk:** Potential RCE/DoS vulnerabilities.
   - **Recommendation:** Upgrade to latest LTS; enforce key-only auth.

## Methodology
- Nmap discovery + service versioning
- OpenVAS authenticated scan where possible
