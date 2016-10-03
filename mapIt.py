import webbrowser,sys,urllib2

def getAddress(address):
	webbrowser.open('https://google.com/maps/place/' + address + '/')
	print address

def getRoute(origin,destination):
	webbrowser.open('https://google.com/maps/dir/' + origin + '/' + destination + '/')
	print origin + destination

def getCoordinates(address):
	response = urllib2.urlopen('https://google.com/maps/place/' + address + '/')
	html = response.read()
	for line in html:
		if 'markers' in line:
			coordinates = line[line.find('markers')+1:]
			print coordinates
			break

hola = ['hola','que','tal']

if len(sys.argv)> 1:
	argvString = ''.join(sys.argv[1:])
	argvString = argvString.replace(' ','+')
	if ':' in argvString:
		argvString = argvString.split(':')
		getRoute(argvString[0],argvString[1])
	else:
#		getAddress(argvString)
		getCoordinates(argvString)
else:
	print "please write an address"
	exit()

