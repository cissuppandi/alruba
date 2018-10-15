import requests,json
import sys
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
def restapi_post_method(uri, usrname, passwd, session_data):
    headers = {'Content-Type':'application/json','Accept':'application/json'}
    username = usrname
    password = passwd
    url = uri
    ucpAuth = requests.auth.HTTPBasicAuth(username, password)
    #resp = requests.post(url, verify=False, data=data, auth=(username, password), headers=headers)
    resp = reqst.post(url, verify=False, data=session_data, auth=(username, password), headers=headers)
    response = resp.headers
    #json_data = json.loads(response)
    print (response)
    return response

#Comment following lines to run from RobotFramework

#  Build a request Body for Session Creation
session_data = {
}
session_data["username"]=sys.argv[2]
session_data["password"]=sys.argv[3]
session_data = json.dumps(session_data)

post_session = restapi_post_method(sys.argv[1], sys.argv[2], sys.argv[3], session_data)
print (post_session)
print (post_session.get("X-Auth-Token"))
session_id = post_session.get("X-Auth-Token")

if (session_id):
	print ("Session Created Successfully")
else:
	print("Verify session data for creating correct session id")


