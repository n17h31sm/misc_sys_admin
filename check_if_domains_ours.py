import CloudFlare
import csv
import http.client 
import requests

#This script uses CloudFlare's API to check if a list of domains is there, therfore is ours.
# First it check if the domain works, then check if it is in this cloudflare account, and remove them from the list if they are found
# Finally create a new file with the remaining domains

domains = []
with open ('remaining_domains.csv','r') as csvfile:
    _domains = csv.reader(csvfile)
    for domain in _domains:
        domains.append(domain)
#for dom in domains:
 #   print(dom)

cf = CloudFlare.CloudFlare(email='', token='')
try:
    zones = cf.zones.get()
except CloudFlare.exceptions.CloudFlareAPIError as e:
    exit('/zones.get %d %s - api call failed' % (e, e))
except Exception as e:
    exit('/zones.get - %s - api call failed' % (e))

if len(zones) == 0:
   exit('No zones found')

zone_ids = []
for zone in zones:
    zone_ids.append(zone['id'])

print(len(zone_ids))
#active_domains = []

for zid in zone_ids:
    print("\n" + zid)
    try:
        dns_records = cf.zones.dns_records.get(zid,params={'type':'A'})
        print("--------------------------------")
        print(len(dns_records))
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones/dns_records.get %d %s - api call failed' % (e, e))
    for dom in domains:
        print(dom)
        try:
            status = requests.get("http://"+ dom[0]).status_code
        except requests.exceptions.ConnectionError:
            status  = 430
        print("-------" + str(status) + "\n")
        if status < 400:
            for record in dns_records:
                print(dom[0] + " ?==? " + record['name'] + '\n')
                if dom[0] in record['name']:
                    print(record['content'] + '\n')
                    if dom[1] == record['content']:
                       #print(domain[0] + '\n') 
                       #print(record['name'] + '\n')
                       #active_domains.append(domain[0])
                       if dom in domains:
                          domains.remove(dom)

for dom in domains:

    
    
    #exist = 0
    #for ac in active_domains:
     #   if ac == dom[0]:
      #      exist = 1
    #if exist == 0:
   with open ('remaining_domains1.csv','a') as remaining:
        writer = csv.writer(remaining, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(dom) 
