# Domain Availability Checker

This script generates domain name combinations from a list of keywords and checks their availability using the WHOIS service. It supports multithreading to speed up the (potentially I/O heavy) process.

## Features

- Generates domain name combinations from provided keywords
- Limits combinations to a specified maximum length
- Checks domain availability using the WHOIS service
- Supports multithreading for faster execution

## Requirements

- Python 3.x
- `python-whois` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/quartzinquartz/domain_availability_checker.git
   cd domain_availability_checker

2. Install required libray:
   ```sh
   pip install python-whois

## Usage

1. Edit the `find_available_domains.py` script to update the `domain_keywords` and `tlds` lists as needed.
2. Run the script:
   ```sh
   python3 find_available_domains.py
