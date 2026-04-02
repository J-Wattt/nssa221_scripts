#Jacob Watson March 27, 2026
#!/env/bin/python3
from geoip import geolite2 # type: ignore
import subprocess
import os
import pathlib
import re

pattern = r"[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}]"

    

def main():
    ip_addresses = dict("Count","IP address", "Country")
    syslog = "/home/student/syslog.log"
    try:
        with open(syslog,"r") as f:
            for line in f:
                match = pattern.search(line)
                if match in ip_addresses:
                    for address in ip_addresses:
                        if(ip_addresses['IP address'] == match):
                            address["Count"] +=1
                            
                else:
                    try:
                        with geoip2.database.Reader(DATABASE_PATH) as reader:
                            response = reader.city(match) 
                            country = response.country.name
                            ip_address = dict("Count" | 0, "IP address" | match, "Country"|country)
                            ip_addresses = ip_address | ip_addresses


                    except geoip2.errors.AddressNotFound:
                        print("Error: Location for IP")
                    except Exception as e:
                        print("Something went wrong", e)

    except FileNotFoundError:
        print(f"File not found")
    
    sorted_report = dict(sorted(ip_address.items()))

    print(subprocess.run(["date"],capture_output=True, stdout=True))
    for entries in sorted_report:
        print(entries)

main()
