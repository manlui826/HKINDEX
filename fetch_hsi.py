name: HSI Daily Auto Fetcher

on:
  schedule:
    - cron: '15 9 * * 1-5'
  workflow_dispatch:

jobs:
  run-script:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
    - name: Check out repo code
      uses: actions/checkout@v4.2.2

    - name: Set up Python
      uses: actions/setup-python@v5.4.0
      with:
        python-version: '3.11'

    - name: Install Dependencies
      run: pip install yfinance pandas openpyxl

    - name: Fetch HSI Data
      run: python fetch_hsi.py

    - name: Save Excel back to Repository
      run: |
        git config --global user.name "github-actions[bot]"
        git config --global user.email "github-actions[bot]@users.noreply.github.com"
        git add hsi_historical_data.xlsx
        git commit -m "Automated HSI Data Sync (Excel format)" || exit 0
        
        # FIX: Pull down any web changes first to prevent push rejection
        git pull --rebase origin main
        
        git push origin main
