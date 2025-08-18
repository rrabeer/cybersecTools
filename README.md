# Cybersecurity Homelab Portfolio

This repo showcases hands-on security projects by **Rabbani Rasha**. It's designed as a clear, recruiter-friendly portfolio with reproducible steps, screenshots, and reports.

## Projects

- **SIEM (Splunk) – SSH Brute-Force Detection** (`projects/siem-splunk-ssh-bruteforce/`)
- **Vulnerability Scanning – Nmap & OpenVAS** (`projects/vuln-scanning-nmap-openvas/`)
- **Packet Analysis – Suspicious DNS with Wireshark** (`projects/wireshark-dns-analysis/`)
- **Python – Auth Log Brute-Force Detector** (`projects/python-authlog-bruteforce-detector/`)

> Tip: Put all screenshots in each project's `assets/` folder to keep things organized.

## Quick Start

```bash
# 1) Clone after you publish your repo on GitHub
git clone https://github.com/<YOUR_GITHUB_USERNAME>/cybersec-portfolio.git
cd cybersec-portfolio

# 2) (Optional) Create a virtualenv for Python project
python3 -m venv .venv && source .venv/bin/activate
pip install -r projects/python-authlog-bruteforce-detector/requirements.txt

# 3) Run the Python detector (sample usage)
python projects/python-authlog-bruteforce-detector/scripts/auth_bruteforce_detector.py \
  --log-file projects/siem-splunk-ssh-bruteforce/data/sample_logs/ssh_failed.log \
  --threshold 5 --window-min 10
```

## How to Publish This Repo to GitHub

1. Create a **new empty repo** on GitHub named `cybersec-portfolio` (no README).
2. On your machine:

```bash
cd /path/to/cybersec-portfolio   # the folder that contains this README
git init
git add .
git commit -m "Initial commit: cybersecurity homelab portfolio"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/cybersec-portfolio.git
# or SSH: git@github.com:<YOUR_GITHUB_USERNAME>/cybersec-portfolio.git
git push -u origin main
```

## Repo Layout

```
cybersec-portfolio/
├─ projects/
│  ├─ siem-splunk-ssh-bruteforce/
│  ├─ vuln-scanning-nmap-openvas/
│  ├─ wireshark-dns-analysis/
│  └─ python-authlog-bruteforce-detector/
├─ docs/
│  └─ TEMPLATES/
├─ .github/workflows/
├─ .gitignore
├─ LICENSE
└─ README.md
```

## License
MIT — see `LICENSE` for details.
