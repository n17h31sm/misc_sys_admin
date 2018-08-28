import json

output = "define service{{\n \tuse \t generic-service\n \thost_name \t  HOST\n\tservice_description\t Check domain expiry for {0}\n\tcheck_interval \t 1440\n\tcheck_command\t  check_domain!{0}\n}}\n"


blacklist = ["LIST OF DOMAINS WE SHOULD EXCLCUDE"]

#open the file with all domains and create domain expiry check service for all of them
domains = []
with open ('domains_monitor.json','r') as file:
    for line in file:
        domains = json.loads(line)

for dom in domains['data']['acct']:
    with open ('domains_expiry.cfg','a') as dom_file:
        if str(dom['domain']) not in blacklist:
            dom_file.write(output.format(str(dom['domain'])))
  
 # The reason for this script what that we have a lot of domains on WHM/Cpanel and wanted to automatically add expiry check for all of them in nagios
 # we move the domains_expiry.cfg to nagios .cfg files. Also we used the ssh execute on login, to get the list from WHM/Cpanel
