import tornado.web
import tornado.ioloop


class basicRequesthandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hey!! its me")

class skillsRequesthandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num)%2!=0 else "even"
            self.write(f"the integer {num} is {r}")
        else:
            self.write(f"the num {num} is not a valid integer")
 

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self,studentName,courseID):
        self.write(f"welcome {studentName}, the course you are viewing is {courseID}") 

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequesthandler),
        (r"/skills",skillsRequesthandler),
        (r"/checkNumber",queryParamRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)",resourceParamRequestHandler)
    ])

    port = 8082
    app.listen(port)
    print(f'application is listening on port {port}')
    tornado.ioloop.IOLoop.current().start()