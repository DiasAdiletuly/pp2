import json
import requests

response = requests.get("https://raw.githubusercontent.com/erlanurbergen/pp2/master/week5/Lab4/json/sample-data.json")
data = json.loads(response.text)
    # print(data)
print("""Interface Status================================================================================""")
print("""DN                                             Description          Speed                      MTU """)
for imdata in data["imdata"]:
    for i, k in imdata['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="                          ")
        if i == "speed":
            print(k, end="                                         ")
        if i == "mtu":
            print(k, end="                   ")
    print()