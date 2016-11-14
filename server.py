import BaseHTTPServer
import json
from ocr import OCRNeuralNetwork
import numpy as np
import random

HOST_NAME = 8000
HIDDEN_NODE_COUNT = 15

data_matrix = np.loadtxt(open('data.csv', 'rb'), delimiter = ',')
data_labels = np.loadtxt(open('dataLabels.csv', 'rb'))

data_matrix = data_matrix.tolist()
data_labels = data_labesl.tolist()

train_indice = range(5000)

random.shuffle(train_indice)

nn = OCRNeuralNetwork(HIDDEN_NODE_COUNT, data_matrix, data_labels, train_indice)

class JSONHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
	response_code = 200
	response = ""
	var_len = int(self.header.get('Content-Length'))
	content = self.rfile.read(var_len)
	payload = json.loads(content)

	if payload.get('train'):
	    nn.train(payload['trainArray'])
	    nn.save()
	elif payload.get('predict'):
	    try:
		print(nn.predict(data_matrix[0])
		response = {"type":"test", "result":str(nn.predict(payload['image']))}
	    except:
		response_code = 500
	else:
	    response_code = 400
	
	self.send_response(response_code)
	self.send_header("Content-type", "application/json")
	self.send_header("Access-Control-Allow-Origin","*")
	self.end_headers()
	if response:
	    self.wfile.write(json.dumps(response))
	return


if __name__='__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), JSONHandler)

    try:
	httpd.server_forever()
    except KeyboardInterrupt:
	pass
    else:
	print("Unexpected server exception occurred.")
    finally:
	httpd.server_close()





