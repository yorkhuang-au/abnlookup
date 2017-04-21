
import urllib.request as req
#from xml.etree import ElementTree
from xml.etree.ElementTree import XML
import threading
import datetime
from multiprocessing import Pool

#from twisted.internet import reactor, protocol

class ABNLookUpThread(threading.Thread):
	def __init__(self, counter):
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self):
		name = 'coles'
		postcode = '2250'
		legalName = ''
		tradingName = ''
		NSW = ''
		SA = ''
		ACT = ''
		VIC = ''
		WA = ''
		NT = ''
		QLD = ''
		TAS = ''
		authenticationGuid = 'f65308c5-30a5-4a5f-8fd7-29b997325deb'		#Your GUID should go here

		proxy = req.ProxyHandler({'http': r'http://operyhg:Qyy2003Hyf@10.150.17.10:3128'})
		auth = req.HTTPBasicAuthHandler()
		opener = req.build_opener(proxy, auth, req.HTTPHandler)
		req.install_opener(opener)
		for j in range(10):
			conn = req.urlopen('http://abr.business.gov.au/abrxmlsearchRPC/AbrXmlSearch.asmx/' +
								'ABRSearchByNameSimpleProtocol?name=' + name +
								'&postcode=' + postcode + '&legalName=' + legalName +
								'&tradingName=' + tradingName + '&NSW=' + NSW +
								'&SA=' + SA + '&ACT=' + ACT + '&VIC=' +  VIC +
								'&WA=' + WA + '&NT=' + NT + '&QLD=' + QLD +
								'&TAS=' + TAS + '&authenticationGuid=' + authenticationGuid)

			#XML is returned by the webservice
			#Put returned xml into variable 'returnedXML'
			#Output xml string to file 'output.xml' and print to console
			returnedXML = conn.read()
			ele = XML(returnedXML)
			print(self.counter)
			print(j)
			print(ele)

def lookup(c):
	name = 'coles'
	postcode = '2250'
	legalName = ''
	tradingName = ''
	NSW = ''
	SA = ''
	ACT = ''
	VIC = ''
	WA = ''
	NT = ''
	QLD = ''
	TAS = ''
	authenticationGuid = 'f65308c5-30a5-4a5f-8fd7-29b997325deb'		#Your GUID should go here

	proxy = req.ProxyHandler({'http': r'http://operyhg:Qyy2003Hyf@10.150.17.10:3128'})
	auth = req.HTTPBasicAuthHandler()
	opener = req.build_opener(proxy, auth, req.HTTPHandler)
	req.install_opener(opener)
	for j in range(10):
		conn = req.urlopen('http://abr.business.gov.au/abrxmlsearchRPC/AbrXmlSearch.asmx/' +
							'ABRSearchByNameSimpleProtocol?name=' + name +
							'&postcode=' + postcode + '&legalName=' + legalName +
							'&tradingName=' + tradingName + '&NSW=' + NSW +
							'&SA=' + SA + '&ACT=' + ACT + '&VIC=' +  VIC +
							'&WA=' + WA + '&NT=' + NT + '&QLD=' + QLD +
							'&TAS=' + TAS + '&authenticationGuid=' + authenticationGuid)

		#XML is returned by the webservice
		#Put returned xml into variable 'returnedXML'
		#Output xml string to file 'output.xml' and print to console
		returnedXML = conn.read()
		ele = XML(returnedXML)
		print(c)
		print(j)
		print(ele)

print(datetime.datetime.now())
ths = []
for i in range(100):
	t = ABNLookUpThread(i)
	t.start()
	ths.append(t)

for th in ths:
	th.join()
print(datetime.datetime.now())

#if __name__ == '__main__':
#	print(datetime.datetime.now())
#	pool = Pool( processes=100)
#	pool.map(lookup, range(100))
#	print(datetime.datetime.now())