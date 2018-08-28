
import pypd
pypd.api_key = "SECRET"

# We wanted to get alerted in pagerduty when geoip update fails, but it can fail in may ways so I checked all error texts, 
# and send it to pagerduty integration so first we run goeipupdate > geoipstatus.txt in cron then this script

list_of_errors = ["Unable", "Unknown", "Can't", "must be", "Error", "unexpectedly", "invalid", "unexpected", "failed"]
string_message = ""

with open('geoipstatus.txt','r') as status:
        for line in status:
            string_message += line


for error in list_of_errors:
    if error in string_message:
        #Send the mail
        msg = "\n" + string_message # The /n separates the message from the headers
        pypd.EventV2.create(data={
            'routing_key': 'SECRET',
            'event_action': 'trigger',
            'payload': {
                'summary': "You can check the error at /root/geoipupdate_check/geoipstatus.txt on HOST",
                'severity': 'error',
                'source': 'INTEGRATION',
            }
        })
        break
