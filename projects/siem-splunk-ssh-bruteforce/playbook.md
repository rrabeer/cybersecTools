# SOC Playbook — SSH Brute-Force

1. Validate alert fidelity and source (asset, log integrity).
2. Check for **successful** logins from same IP/user.
3. Geolocate IP; check threat intel.
4. Contain (block IP/range, enable jail).
5. Harden: key-only auth, disable root SSH, rate-limit.
6. Document and close with evidence.
