import json
import urllib.request
import urllib.parse

class MDElogin:

    def __init__(self, tenantId, appId, appSecret):
        self.tenantId = tenantId
        self.appId = appId
        self.appSecret = appSecret

    def __repr__(self):
     
        url = "https://login.windows.net/%s/oauth2/token" % (self.tenantId)

        resourceAppIdUri = 'https://api.securitycenter.windows.com'

        body = {
            'resource' : resourceAppIdUri,
            'client_id' : self.appId,
            'client_secret' : self.appSecret,
            'grant_type' : 'client_credentials'
        }

        data = urllib.parse.urlencode(body).encode("utf-8")

        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        jsonResponse = json.loads(response.read())
        aadToken = jsonResponse["access_token"]

        return aadToken

logintoken = MDElogin('f22494a6-c485-4648-a3e6-4ed455ef0c4b', 'c3a5c924-da08-4df8-af03-a7df95bfdf99', 'Wld_U8hJQHLf-bg~84EUA.54pU_SlKO3qc')
