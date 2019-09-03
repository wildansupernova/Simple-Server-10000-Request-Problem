import signal
import pyuv
import json
import sys
import chardet

from file_server import CachedFileServer

file_server = CachedFileServer()

with open('resource/config.json') as f:
    config = json.load(f)

if (len(sys.argv) < 2):
    print("Specify file type")
    sys.exit()
    
file_type = sys.argv[1]

def on_read(client, data, error):
    content = file_server.read(config[file_type])
    response = "HTTP/1.1 200 OK\n" \
        + "Date: Thu, 19 Feb 2009 12:27:04 GMT\n" \
        + "Server: Apache/2.2.3\n" \
        + "Last-Modified: Wed, 18 Jun 2003 16:05:58 GMT\n" \
        + "Content-Type: text/html\n" \
        + f"Content-Length: {len(content)}\n" \
        + "Connection: close\n" \
        + "\n"
    response = str.encode(response) + content

    client.write(response)
    client.close()
    clients.remove(client)
    return

def on_connection(server, error):
    client = pyuv.TCP(server.loop)
    server.accept(client)
    clients.append(client)
    client.start_read(on_read)
    ip, port = client.getpeername()


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
