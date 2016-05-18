import tornado.web
import tornado.httpserver

class MyStaticFileHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        # Disable cache
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')

application = tornado.web.Application([(r"/(.*)", \
                                   MyStaticFileHandler, \
                                   {"path":r"./output/", "default_filename": "index.html"})])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(80)

tornado.ioloop.IOLoop.current().start()
