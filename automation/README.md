# Automation Scripts

## Overview
Python scripts for automating business analytics tasks.

## Scripts

### competitor_scraper.py
- Scrapes competitor websites for basic information
- Outputs data to CSV for analysis
- Requires: requests, beautifulsoup4

### lead_data_cleaner.py
- Cleans and standardizes lead data
- Removes duplicates and invalid entries
- Requires: pandas

## Usage
```bash
pip install requests beautifulsoup4 pandas
python competitor_scraper.py
python lead_data_cleaner.py
```