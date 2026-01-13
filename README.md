# 🔐 Automated Brute-Force Detection & Response Engine

## Overview
This project demonstrates a basic security engineering control designed to detect and respond to brute-force login attempts.

It analyzes authentication logs, groups failed login attempts by source IP address, applies a threshold to identify suspicious behavior, and simulates automated defensive actions such as IP blocking and account lockout.

## Security Engineering Concepts
- System hardening
- Defense in depth
- Detection and response
- Security automation

## How It Works
1. Parses authentication log entries
2. Counts failed login attempts per IP
3. Applies a configurable threshold
4. Flags brute-force behavior
5. Triggers simulated response actions

## Technologies Used
- Python
- Log parsing
- Security automation logic

## Future Improvements
- Time-based detection windows
- Integration with real log files
- Firewall rule automation
- Account management integration
