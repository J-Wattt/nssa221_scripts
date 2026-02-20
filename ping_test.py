import os
import subprocess

def ping(str address){
	p = subprocess.Popen(["ping.exe",address]) #sets up the process for pinging address
	param ='-n' if os.sys.platform().lower()= "linux" else '-c' #checks os
	command = ['ping',param, '1', address]
	if(subprocess.call(command)==0){ #if command == 0 the domain exists
		return p.communicate()[0] 
	}
	else{#Any invalid address won't equal 0
		return address + 'is not a valid target'
	}
}
def main(){
	print("1. Display the Default Gateway \n 2. Test Local Connectivity \n 3. Test Remote Connectivity \n 4. Test DNS Resolution") #display options
	str user_input = input("Please enter a number corresponding with the option (any other input to exit).") 
	while(True){ #keeps the script running until the input isn't 1,2,3 or 4
		if(user_input = "1"){
			print(ping("192.168.207.254"))
		}
		elif(user_input = "2"){
			print(ping("8.8.8.8"))
		}
		elif(user_input = '3"){
			print(ping("129.21.3.17")
		}
		elif(user_input = "4){
			print(ping("www.Google.com")
		}
		else{
		break
		}
	}
}
