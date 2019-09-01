import signal
import pyuv
import json
import sys

with open('resource/config.json') as f:
    config = json.load(f)

if (len(sys.argv) < 2):
    print("Specify file type")
    sys.exit()
    
file_type = sys.argv[1]

def on_read(client, data, error):
    f = open(config[file_type], "r")
    content = str.encode(f.read())
    client.write(content)
    client.close()
    clients.remove(client)
    return

def on_connection(server, error):
    client = pyuv.TCP(server.loop)
    server.accept(client)
    clients.append(client)
    client.start_read(on_read)
    ip, port = client.getpeername()
    print("{}:{} connected".format(ip,port))


def signal_cb(handle, signum):
    [c.close() for c in clients]
    signal_h.close()
    server.close()

print("PyUV version %s" % pyuv.__version__)

loop = pyuv.Loop.default_loop()
clients = []

server = pyuv.TCP(loop)
server.bind(("0.0.0.0", config['PORT_APP']))
server.listen(on_connection)

signal_h = pyuv.Signal(loop)
signal_h.start(signal_cb, signal.SIGINT)

loop.run()
print("Stopped!")
