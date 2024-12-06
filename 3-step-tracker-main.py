import json
import pyperclip

datas = {}

with open('hopp-report.json', 'r') as f:
    datas = json.load(f)

data_str = ""

for data in datas["session_recording"]["rec"] :
    data_str += json.dumps(data)
    data_str += "\n--------------------------------\n"

pyperclip.copy(datas["session_recording"]["rec"] )
