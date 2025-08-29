#!/usr/bin/env python3
"""
Auth Log Brute-Force Detector
Scans auth.log-like files for repeated "Failed password" events.
"""

import argparse
import re
from datetime import datetime, timedelta
from collections import defaultdict, deque

LOG_LINE = re.compile(
    r'^(?P<mon>\w{3})\s+(?P<day>\d{1,2})\s+(?P<time>\d{2}:\d{2}:\d{2}).*?Failed password.*?from\s+(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
)

MONTHS = {
    m: i
    for i, m in enumerate(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
         "Aug", "Sep", "Oct", "Nov", "Dec"],
        start=1
    )
}

)}

def parse_ts(mon: str, day: str, time_str: str, year: int) -> datetime:
    ts = datetime.strptime(f"{year}-{MONTHS[mon]:02d}-{int(day):02d} {time_str}", "%Y-%m-%d %H:%M:%S")
    return ts

def iter_events(path: str, year: int):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = LOG_LINE.search(line)
            if m:
                yield parse_ts(m.group("mon"), m.group("day"), m.group("time"), year), m.group("ip")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log-file", required=True, help="Path to auth.log-like file")
    ap.add_argument("--threshold", type=int, default=5, help="Failed attempts to trigger alert")
    ap.add_argument("--window-min", type=int, default=10, help="Sliding window in minutes")
    ap.add_argument("--year", type=int, default=datetime.utcnow().year, help="Year for parsing timestamps")
    args = ap.parse_args()

    window = timedelta(minutes=args.window_min)
    buckets = defaultdict(lambda: deque())

    alerts = []
    for ts, ip in iter_events(args.log_file, args.year):
        dq = buckets[ip]
        dq.append(ts)
        # Drop events outside the window
        while dq and (ts - dq[0]) > window:
            dq.popleft()
        if len(dq) >= args.threshold:
            alerts.append((ts.isoformat(), ip, len(dq)))

    if not alerts:
        print("No brute-force patterns detected.")
        return

    print("ALERTS: Failed SSH patterns detected")
    for when, ip, count in alerts:
        print(f"- {when} | {ip} | last-window-fails={count}")

if __name__ == "__main__":
    main()
