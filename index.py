import tornado.web
import tornado.ioloop
import json

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

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fl = open('names.txt','r')
        skills = fl.read().splitlines()
        fl.close()
        self.write(json.dumps(skills))

    def post(self):
        skill = self.get_argument("skill")
        fl = open('names.txt','a')
        fl.write(f"{skill}\n")
        fl.close()
        self.write(json.dumps({"message":"skill added successfully"}))

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequesthandler),
        (r"/skills",skillsRequesthandler),
        (r"/checkNumber",queryParamRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)",resourceParamRequestHandler),
        (r"/list",listRequestHandler)

    ])

    port = 8082
    app.listen(port)
    print(f'application is listening on port {port}')
    tornado.ioloop.IOLoop.current().start()