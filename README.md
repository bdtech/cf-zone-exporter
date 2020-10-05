# cf-zone-exporter
Export all the DNS zone files across all your Cloudflare accounts.

Requires Python 3.7.x

## Download
```sh
# Clone using git
git clone https://github.com/shagamemnon/cf-zone-exporter.git
```
Alternative, download and unzip:
https://github.com/shagamemnon/cf-zone-exporter/zipball/main

## Install
```
cd C:\users\frank\Downloads\cf-zone-exporter
pip install -r requirements.txt
pip3 install -r requirements.txt
```
## Usage
```
cd C:\users\frank\Downloads\cf-zone-exporter
# Do NOT add the Bearer prefix. Just the token
python3 zone_export.py --api_token '12345myCLOUDFLAREAPITOKEN'
```

This script throttles itself at 3 requests / second in accordance with the Cloudflare API v4 rate limits. For example, downloading 3700 zone files will take ~1233 seconds (~20.6 minutes).
