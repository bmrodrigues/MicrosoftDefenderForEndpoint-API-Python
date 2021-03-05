import getpass
import argparse
import MDElogin
import listalerts

# Menu
parser = argparse.ArgumentParser()
parser.add_argument('-login', help='Tests app Login and prints out token for debug', action='store_true')
parser.add_argument('-listalerts', help='Retrieves a collection of Alerts', action='store_true')
parser.add_argument('-last10alerts', help='Get 10 latest Alerts with related Evidence', action='store_true')

args = parser.parse_args()

# Authentication
tenantId = input('Enter your Tenant ID: ')
appId = input('Enter your application ID: ')
appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')

# Menu options

if args.login:
    logintoken = MDElogin.MDElogin(tenantId, appId, appSecret)
    print('\n')
    print(logintoken)
    print('\n')

if args.listalerts:
    alerts = listalerts.List_Alerts(tenantId, appId, appSecret)
    alerts.default()

if args.last10alerts:
    alerts = listalerts.List_Alerts(tenantId, appId, appSecret)
    alerts.latest_10()