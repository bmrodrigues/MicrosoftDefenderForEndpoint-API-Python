import json
import urllib.request
import urllib.parse
import login

class List_Alerts:

    def __init__(self, tenantId, appId, appSecret):
        self.tenantId = tenantId
        self.appId = appId
        self.appSecret = appSecret
    
    def default(self):
        login_MDEcli = login.login(self.tenantId, self.appId, self.appSecret)
        aadToken = login_MDEcli.login()

        url = "https://api.securitycenter.microsoft.com/api/alerts"
        headers = { 
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : "Bearer " + aadToken
        }

        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        jsonResponse = json.loads(response.read())
        print(jsonResponse['value'][0])

    def latest_10(self):
        login_MDEcli = login.login(self.tenantId, self.appId, self.appSecret)
        aadToken = login_MDEcli.login()

        url = "https://api.securitycenter.microsoft.com/api/alerts?$top=10&$expand=evidence"
        headers = { 
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : "Bearer " + aadToken
        }

        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        jsonResponse = json.loads(response.read())
        print(jsonResponse['value'][0])