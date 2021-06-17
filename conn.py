from json import decoder
import socket
import http.client as http
import json

class Conn():
    HOST = ""
    PORT = ""
    URL = ""
    HEADERS = {"Content-Type": "application/json", "X-GATE-KEY": "Gll123mlPOIn1$@!@#94NBizE98121547f79123*7123^sm"}

    def __init__(self, host, port, url):
        self.HOST = host
        self.PORT = port
        self.URL = url

    def isConnect(self, timeout = 3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.HOST, self.PORT))
            return True
        except:
            return False
    
    def checkData(self, idcard, fungsi):
        try:
            data = '{"id_card": "' + idcard + '", "fungsi": "' + fungsi + '"}'
            con = http.HTTPConnection(self.HOST)
            con.request('POST', self.URL, data, self.HEADERS)
            response = con.getresponse()
            result = response.read().decode()
            respond = json.loads(result)
            con.close()
            return respond
        except Exception as e:
            print(e)
            return False



    
