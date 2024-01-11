Dictionaries :--------(eg)----------------
ec2_instance_list = [
    {
        "id":"In-01",
        "type":"Micro"

    },
    {"id":"In-02",
        "type":"Micro"
        },
    {"id":"In-03",
        "type":"Micro"
        }
]

print (ec2_instance_list [2]["id"])

------------------------------------------------------------------------------------------------------
eg: 
import requests

re = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print (re)

[ o/p:PS C:\Users\YASH\videos> python test.py
<Response [200]> ] (we getting this as an ouput) here basicaaly we gat an ouput as class/object : so, if we want Json fomart) then samll change in code.


import requests

re = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print (re.json())
