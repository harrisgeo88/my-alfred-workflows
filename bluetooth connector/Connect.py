import json
import sys
import os

with open('devices.json') as json_file:
    data = json.load(json_file)
    device = data[sys.argv[1]]

    if device:
        action = 'connect' if sys.argv[2] == 'c' else 'disconnect'
        os.system(
            '/usr/local/bin/BluetoothConnector {} --{}'.format(device, action))

        result = {"items": [
            {
                "type": "file",
                "title": "Connected to device" if action == 'connect' else 'Disconnected from device',
                "subtitle": "Success!",
                "arg": "arg1"
            }
        ]}

        finalResult = json.dumps(result)

        print(finalResult)
