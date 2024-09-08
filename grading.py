import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

# Function to test HW3
def grading_learning_bridge():
    # run mininet test
    process = subprocess.Popen(
        ['sudo', '/usr/local/bin/mn', '--controller=remote,127.0.0.1:6653', 
        '--topo=tree,depth=1', 
        '--switch=ovs,protocols=OpenFlow14', 
        '--test=pingall'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    
    # Capture stderr output due to the use of sudo
    _, stderr = process.communicate()
    
    output_lines = stderr.decode('utf-8')
    # Successful if there is 0% packet loss or failure.
    return True if re.search(r'Results: 0% dropped', output_lines) else False
    
        


def grading_proxyarp():
    # run mininet test
    process = subprocess.Popen(
        ['sudo', '/usr/local/bin/mn', '--controller=remote,127.0.0.1:6653', 
        '--topo=tree,depth=1', 
        '--switch=ovs,protocols=OpenFlow14', 
        '--custom',
        'mn_test.py',
        '--test=arpingall'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    # Capture stderr output due to the use of sudo
    _, stderr = process.communicate()
    
    output_lines = stderr.decode('utf-8').splitlines()
    results_lines = [ line for line in output_lines if 'unanswered' in line]
    drop_lines = [line for line in results_lines if re.search(r'^(?!.*0%)',line)]
    
    # Success if there are no dropped packets; otherwise, it fails.
    return True if not drop_lines else False
def request_flow_rule():
    tmp = 0
    url = 'http://localhost:8181/onos/v1/flows/of:0000000000000001'
    auth = HTTPBasicAuth('onos', 'rocks')
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url=url, auth=auth, headers=headers)
    if response.status_code == 200:
        flows = response.json().get('flows', [])
        for flow in flows:
            treatment = flow.get('treatment', {}).get('instructions', [{}])
            criteria = flow.get('selector', {}).get('criteria', [{}])

            if (flow.get('appId') == 'nctu.winlab.bridge' and
                flow.get('timeout') == flow.get('priority') == 30 and
                treatment[0].get('type') == 'OUTPUT' and
                {'ETH_DST', 'ETH_SRC'}.issubset({criteria[0].get('type'), criteria[1].get('type')})):
                tmp += 1
        print(tmp)
    else : 
        print(f"Failed to retrieve data: {response.status_code}")

        
    

if grading_learning_bridge():
    print("success")
else:
    print("fail")
request_flow_rule()
if grading_proxyarp():
    print("success")
else:
    print("fail")
    

