"""Script Cataloging Information
:Product Info:Nexus::9000::9516::NX-OS Release 6.2
:Category:Cleanup
:Box Type:Off-Box
:Title:Nexus Configuration Cleanup
:Short Description:To clean up the switch configurations
:Long Description:Cleanup the switch configurations
:Input:command to disable the configurations
:Output:Nexus switch is cleaned up
"""

import os
import requests
import json
import ConfigParser
import datetime
import time
import ast

#read the nexus configuration file
config=ConfigParser.ConfigParser()
config.read('nexus_cleanup.cfg')

def CheckConfig(host, ipaddress, username, password):
	
	#check the configuration details
	if (ipaddress == ''):
		print "Please update the configuration file with Switch IPAddress for Host"+str(host)
		exit(1)

	if ((username and password) == ''):
		print "Please update the configuration file with Switch User Credentials for Host"+str(host)
		exit(1)
	elif (username == ''):
		print "Please update the configuration file with Switch User Credentials for Host"+str(host)
		exit(1)
	elif (password == ''):
		print "Please update the configuration file with Switch User Credentials for Host"+str(host)
		exit(1)
	print "-- Host"+str(host)+" configuration is valid" 
	return 


"""

Class to cleanup the required nexus switch
"""

class Nexus_Clean:

    myheaders = {'content-type':'application/json-rpc'}
    headers = {'content-type':'application/json'}    

    def nexus_clean(self, host, ipaddress, username, password):
        url = "http://"+ipaddress+"/ins"
        print "-- Trying "+url
       

        #execute the commands
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"conf t","version":1},"id":1},
            {"jsonrpc":"2.0","method":"cli","params":{"cmd":"no feature bash-shell","version":1},"id":2},
            {"jsonrpc":"2.0","method":"cli","params":{"cmd":"terminal dont-ask","version":1},"id":3},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no feature scheduler","version":1},"id":4},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no int loo 5","version":1},"id":5},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no int loo 100","version":1},"id":6},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()     
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"defa int e 1/2 -3","version":1},"id":7},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"int e 1/2 -3","version":1},"id":8},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"shutdown","version":1},"id":9},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"exit","version":1},"id":10},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass

#####################################################
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no onep","version":1},"id":1},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"chef","version":1},"id":2},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [
            {"jsonrpc":"2.0","method":"cli","params":{"cmd":"no server https://chef-server.onecloudinc.com:443","version":1},"id":3},
            ]
 
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no vrf management","version":1},"id":4},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no validation-client-name chef-validator","version":1},"id":5},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no interval 60","version":1},"id":6},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            cmd = "no node-name" + '' + ipaddress
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":cmd,"version":1},"id":7},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no domain-name onecloudinc.com","version":1},"id":8},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no name-server 10.1.150.254","version":1},"id":9},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass


#####################################################################################
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"conf t","version":1},"id":1},
             {"jsonrpc":"2.0","method":"cli","params":{"cmd":"virtual-service chef","version":1},"id":2},
              {"jsonrpc":"2.0","method":"cli","params":{"cmd":"no activate","version":1},"id":3},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
            time.sleep(60)
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"exit","version":1},"id":4},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no virtual-service chef","version":1},"id":5},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
            time.sleep(60)
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no chef","version":1},"id":6},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass

        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no scheduler job name helloworld","version":1},"id":7},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no scheduler name helloworld","version":1},"id":8},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
    
###########################################################################################################
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"puppet","version":1},"id":1},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no master puppet-master.sakommu-lab.com","version":1},"id":2},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no vrf management","version":1},"id":3},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no run-interval 60","version":1},"id":4},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no name-server 10.1.150.254","version":1},"id":5},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no activate","version":1},"id":6},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"exit","version":1},"id":7},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
############################################################
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"conf t","version":1},"id":1},
            {"jsonrpc":"2.0","method":"cli","params":{"cmd":"virtual-service puppet","version":1},"id":2},
            {"jsonrpc":"2.0","method":"cli","params":{"cmd":"no activate","version":1},"id":3},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
            time.sleep(60)
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"exit","version":1},"id":4},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no virtual-service puppet","version":1},"id":5},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
            time.sleep(60)
        except Exception as e:
            pass

        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no puppet","version":1},"id":6},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no event manager applet foo","version":1},"id":7},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"virtual-service uninstall name chef","version":1},"id":8},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
            time.sleep(60)
        except Exception as e:
            pass
###############################################
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no vlan 500 - 555","version":1},"id":1},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no ip prefix-list puppet-list seq 5 permit 192.168.0.0/16","version":1},"id":2},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no inter port 10","version":1},"id":3},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no ip access-list puppet-command-config","version":1},"id":4},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no ntp server 10.1.150.51 use-vrf management","version":1},"id":5},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no ntp server 10.1.150.52 use-vrf management","version":1},"id":6},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"virtual-service uninstall name puppet","version":1},"id":7},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
            time.sleep(60)
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"virtual-service uninstall name chef","version":1},"id":8},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
            time.sleep(60)
        except Exception as e:
            pass
################################
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"guestshell destroy","version":1},"id":1},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no virtual-service destroy","version":1},"id":2},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"defa int e 1/10","version":1},"id":3},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"defa int e 2/1","version":1},"id":4},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no int loo 99","version":1},"id":5},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"copy r s","version":1},"id":6},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"exit","version":1},"id":7},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"conf t","version":1},"id":8},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass

        
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"do delete bootflash:interface_rate.py","version":1},"id":9},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"do del bootflash:pingrange.py","version":1},"id":10},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"do del bootflash:scripts/helloworld.py","version":1},"id":11},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"do del bootflash:int_change.py","version":1},"id":12},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"do del bootflash:Int_Change.py","version":1},"id":13},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass

        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"no terminal dont-ask","version":1},"id":14},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass


#####################################
#                                   #
#        Validation Commands        #
#                                   #
#####################################

        try:
            payload={"ins_api":{"version": "1.0","type":"cli_show_ascii","chunk": "0","sid": "1","input": "sh run | inc chef","output_format": "json"}}
	    response = requests.post(url,data=json.dumps(payload), headers=Nexus_Clean.headers,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload={"ins_api":{"version": "1.0","type":"cli_show_ascii","chunk": "0","sid": "1","input": "sh run | inc puppet","output_format": "json"}}
            response = requests.post(url,data=json.dumps(payload), headers=Nexus_Clean.headers,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload={"ins_api":{"version": "1.0","type":"cli_show_ascii","chunk": "0","sid": "1","input": "sh run | inc ntp","output_format": "json"}}
            response = requests.post(url,data=json.dumps(payload), headers=Nexus_Clean.headers,auth=(username,password)).json()
        except Exception as e:
            pass
        try:
            payload = [{"jsonrpc":"2.0","method":"cli","params":{"cmd":"sh virtual-service list","version":1},"id":4},]
            response = requests.post(url,data=json.dumps(payload),headers=Nexus_Clean.myheaders,auth=(username,password)).json()
        except Exception as e:
            pass

        print "Host"+str(host)+" is cleaned up!!!\n"



if __name__ == '__main__':
    Hostdetails = ast.literal_eval(config.get('BulkHostDetails', 'HostDetails'))
    
    print "*"*50
    print "   Intilizing Configuration check"
    print "*"*50+"\n"
    
    for host in Hostdetails:
		ipaddress = Hostdetails[host]['ipaddress']
		username = Hostdetails[host]['username']
		password = Hostdetails[host]['password']
		CheckConfig(host, ipaddress, username, password)
    
    print "\n   Finished Configuration check\n"
    
    print "*"*50
    print "   Intilizing Host clean up"
    print "*"*50+"\n"
    
    for host in Hostdetails:
		ipaddress = Hostdetails[host]['ipaddress']
		username = Hostdetails[host]['username']
		password = Hostdetails[host]['password']
		ob = Nexus_Clean() 
		ob.nexus_clean(host, ipaddress, username, password)  
		print "Host"+str(host)+" is cleaned up!!!\n" 
