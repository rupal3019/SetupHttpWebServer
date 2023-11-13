import tornado.web
import tornado.ioloop


class basicRequesthandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hey!! its me")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequesthandler)
    ])

    port = 8082
    app.listen(port)
    print(f'application is listening on port {port}')
    tornado.ioloop.IOLoop.current().start()