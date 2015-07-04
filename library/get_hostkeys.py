#!/usr/bin/env python

DOCUMENTATION = '''
---
module: get_hostkeys
short_description: workaround for the limitations of I(ansible_ssh_host_key_*)
'''

import json
import glob
import re

hostkeys = dict()
for f in glob.glob('/etc/ssh/ssh_host_*_key.pub'):
    hostkey_raw = open(f).read().strip()
    hostkeys[f] = re.sub(r'([a-z0-9-]+ [a-zA-Z0-9+/-]+=*?) .*', r'\1', hostkey_raw)

print json.dumps({
    'ansible_facts': {
        'ssh_hostkeys': hostkeys
    }
})
