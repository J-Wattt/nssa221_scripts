#Jacob Watson March 27, 2026
#!/env/bin/python3
from geoip import geolite2
import subprocess
import os
import pathlib
import re


pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

DATABASE_PATH = "/home/student/GeoLite2-City/GeoLite2-City.mmdb"

def main():
	os.system("clear")
	ip_addresses = {}
	syslog = "/home/student/syslog.log"
	try:
		with open(syslog,"r") as f:
			for line in f:
				match = re.search(pattern, line)
				if match:
					ip = match.group().strip()
					if ip in ip_addresses:
						ip_addresses[ip]["Count"] += 1
		                    
					else:
						try:
							response = geolite2.lookup(ip) 
							if response:
								country = response.country
							else:
								continue
							ip_addresses[ip] = {"Count" : 1, "Country": country}


						except Exception as e:
							print("Something went wrong", e)
				else:
					continue
	except FileNotFoundError:
		print(f"File not found")
    
	sorted_report = sorted(ip_addresses.items(),key=lambda x:[1]["Count"], reverse = True)
	
	print(f"{'Count':<6} {'IP Address':<15} {'Country'}")
	print("-" * 40)

	print(subprocess.run(["date"],capture_output=True, text=True))
	for ip, data in sorted_report:
		print(f"{data['Count']} {ip:<15} {data['Country']}")

main()
