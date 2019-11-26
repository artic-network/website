#!/usr/bin/env python3

"""
a hacky script to scrape all the protocols from the ARTIC group on protocols.io
"""

import json, requests, os, sys

url = 'https://www.protocols.io/api/v3/groups/artic/protocols'
headers = {'Authorization': 'Bearer 0beb1651aad1005a9369790220c29d2352ed2a47f34be1b8cc463c2ccd5a41da'}
outDir = '_protocols/'

data = requests.get(url, headers=headers)
numProtocols = 0
for item in data.json()['items']:
    with open(outDir + '2019-11-22-' + item['uri'] +'.md', 'w') as fh:
        fh.write('---')
        fh.write('\ntitle: ' + item['title'])
        fh.write('\nuri: ' + item['uri'])
        fh.write('\nnav_menu: false')
        fh.write('\nshow_tile: false')
        fh.write('\n---\n')
    fh.close()
    numProtocols+=1

if numProtocols == 0:
    print('no protocols found in the ARTIC group')
    sys.exit(1)

numFiles = len([f for f in os.listdir(outDir)if os.path.isfile(os.path.join(outDir, f))])
if numFiles != numProtocols:
    print('number of protocols written ({}) does not match number of protocols found ({})' .format(numFiles, numProtocols))
    sys.exit(1)

print('added {} protocols from the protocols.io ARTIC group' .format(numProtocols))