import requests,json
import sys
import re
import ssl
requests.packages.urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)

reqst = requests.Session()
reqst.mount('https://', MyAdapter())

url = "http://www.test.com"
#data = "username=admin&password=1234567!"
data = {
}
data["username"]="admin"
data["password"]="1234567!"
data = json.dumps(data)
# Build a request dictionary
preq = [re.findall("[^=]+", i) for i in re.findall("[^\&]+", data)]
dreq = {i[0]: i[1] if len(i) == 2 else "" for i in preq}

headers = {'Content-Type':'application/json','Accept':'application/json'}
username = "admin"
password = "1234567!"
url = "https://192.168.11.227/redfish/v1/SessionService/Sessions"
resp = reqst.post(url, verify=False, data=data, auth=(username, password), headers=headers)
print (resp)
output = resp.headers
#print(output["X-Auth-Token"])
print (output)
#print (resp.status)
#json_data = json.loads(output)
#print (json_data)