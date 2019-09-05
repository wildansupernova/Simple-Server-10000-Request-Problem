import tornado.ioloop
import tornado.web
from tornado import gen
import json
from file_server import CachedFileServer


file_server_ins = CachedFileServer()

with open('resource/config.json') as f:
  config = json.load(f)



class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        # f = open(config['FILE_20_KB'], "r")
        yield self.write(file_server_ins.read(config['FILE_20_KB']))
        # f.close()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(config['PORT_APP'])
    print("Check di localhost:" + str(config['PORT_APP']))
    tornado.ioloop.IOLoop.current().start()