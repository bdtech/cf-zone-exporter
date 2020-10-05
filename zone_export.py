import os
import requests
import json
import argparse
from time import sleep

if not os.path.exists('zone_files'):
    os.makedirs('zone_files')

if not os.path.exists('error_files'):
    os.makedirs('error_files')


def create_file(filepath, contents):
    f = open('{filepath}'.format(filepath=filepath), "w")
    f.write(contents)
    f.close()
    print('Exported {filepath} to {filepath}'.format(filepath = filepath))

def send_request(apiToken):
    # Export DNS Records
    # GET https://api.cloudflare.com/client/v4/zones//dns_records/export

    try:
      with open('./zoneids.json') as f:
        zones = json.load(f)
        for zone in zones:
            output = None
            filepath = None
            zid = zone['zone_tag']
            name = zone['zone_name']
            response = requests.get(
                url='https://api.cloudflare.com/client/v4/zones/{zid}/dns_records/export'.format(zid = zid),
                headers={
                    'Authorization': 'Bearer {token}'.format(token=apiToken),
                    'Content-Type': 'application/json'
                }
            )
            print('zid,' '', name, 'Status Code: {status_code}'.format(
                status_code=response.status_code))
            if response.status_code != 200:
              print('Status Code: {status_code}'.format(
                status_code=response.status_code))
              output = json.dumps(response.json(), indent=4, sort_keys=True)
              filepath = 'error_files/{domain}'.format(domain = name)
            else:
              filepath = 'zone_files/{domain}'.format(domain = name)
              output = response.text
            create_file(filepath=filepath, contents=output)
            sleep(0.33)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

parser = argparse.ArgumentParser()
parser.add_argument('--api_token', required=True)
args = parser.parse_args()
send_request(apiToken = args.api_token)