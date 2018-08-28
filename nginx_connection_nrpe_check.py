import urllib.request

contents = str(urllib.request.urlopen("Endpoint that shows conections").read())

pos_a = contents.find(':')
pos_b = contents.rfind('server')

new_contents = int(contents[(pos_a + 1):(pos_b-2)]) # the number is between : and server


if new_contents <= 150:
    print("OK - connections = " + str(new_contents))
    exit(0)
elif 150 < new_contents < 200:
    print("WARNING - connections = " + str(new_contents))
    exit(1)
elif new_contents >= 200:
    print("CRITICAL - connections = " + str(new_contents))
    exit(2)
else:
    print("UNKNOWN - " + str(new_contents))
    exit(3)
