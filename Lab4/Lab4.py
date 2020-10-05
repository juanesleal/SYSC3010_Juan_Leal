import http.client
import urllib.parse

key = '54CDA6FJF4RCJ92C'
# Put your API Key here IIUQ8XBFN7K9WG2A
#54CDA6FJF4RCJ92C
def lab4():
        field1 = 'juanleal@cmail.carleton.ca'
        field2 = 'L2-M-7'
        field3 = 'c'
        param = urllib.parse.urlencode({'field1': field1, 'field2': field2,'field3': field3,'key':key }) 
        header= {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        
        try:
            conn.request("POST", "/update", param, header)
            response = conn.getresponse()
            print(field1)
            print(field2)
            print(field3)
            data = response.read()
            conn.close()
        except:
            print("connection failed")

lab4()