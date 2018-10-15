import requests,json
import sys
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

#GET Method: Definition for GET Method, Returns output data in json format
def restapi_get_method(uri, usrname, passwd):
    headers = {'Content-Type':'application/json','Accept':'application/json'}
    username = usrname
    password = passwd
    url = uri
    ucpAuth = requests.auth.HTTPBasicAuth(username,password)
    get_reqst = requests.get(url,verify=False,auth=ucpAuth)
    output = get_reqst.content
    json_data = json.loads(output)
    
    return json_data

#POST Method: Definition for POST Method, Returns output data
def restapi_post_method(uri, usrname, passwd, data):
    headers = {'Content-Type':'application/json','Accept':'application/json'}
    username = usrname
    password = passwd
    url = uri
    ucpAuth = requests.auth.HTTPBasicAuth(username, password)
    #resp = requests.post(url, verify=False, data=data, auth=(username, password), headers=headers)
    resp = reqst.post(url, verify=False, data=data, auth=(username, password), headers=headers)
    response = resp.headers
    #json_data = json.loads(response)
    print (response)
    print (response.headers)
    return response

#Comment following lines to run from RobotFramework

#Running scripts directly from python
success_response = "Redfish Root Service"
result = restapi_get_method(sys.argv[1], sys.argv[2], sys.argv[3])
#print (result)
#print (result.content)
data = result
print (data)
name = data.get("Name")
#print (name)
print (data.get("Respose code"))


if name == success_response:
	print ("RESTAPI URI Success")
else: 
	print ("RESTAPI Not Enabled")


#  Build a request Body for Session Creation
session_data = {
}
session_data["username"]="sys.argv[2]"
session_data["password"]="sys.argv[3]"
session_data = json.dumps(session_data)

#post_session = restapi_post_method(sys.argv[1], sys.argv[2], sys.argv[3], session_data)
#print (post_session)

