# Python — Auth Log Brute-Force Detector

A simple parser that scans Linux auth logs for repeated SSH failures within a time window and prints alerts.

## Usage

```bash
python scripts/auth_bruteforce_detector.py \
  --log-file ../siem-splunk-ssh-bruteforce/data/sample_logs/ssh_failed.log \
  --threshold 5 --window-min 10
```

- `--threshold` — number of failed attempts from the same IP to alert.
- `--window-min` — lookback window size in minutes.

## Notes
- Works best on `/var/log/auth.log` style lines.
- This is for learning; integrate with syslog or email for real alerts.
