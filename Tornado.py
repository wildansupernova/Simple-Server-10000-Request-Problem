import tornado.ioloop
import tornado.web
import json

with open('resource/config.json') as f:
  config = json.load(f)



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        f = open(config['FILE_20_KB'], "r")
        self.write(f.read())
        f.close()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(config['PORT_APP'])
    print("Check di localhost:" + str(config['PORT_APP']))
    tornado.ioloop.IOLoop.current().start()