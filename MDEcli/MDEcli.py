import getpass
import argparse
import login

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--login', help='Tests app Login and prints out token for debug',
                    action='store_true' )

args = parser.parse_args()
if args.login:
    arg_tenantId = input('Enter your Tenant ID: ')
    arg_appId = input('Enter your application ID: ')
    arg_appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
    logintoken = login.MDElogin(arg_tenantId, arg_appId, arg_appSecret)
    print('\n')
    print(logintoken)
    print('\n')