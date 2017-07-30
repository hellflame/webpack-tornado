import tornado.ioloop as ioloop
import tornado.web as web
import sys
from project.service import routes
from project.config import settings

# print routes
app = web.Application(handlers=routes, **settings)

if __name__ == '__main__':
    port = 5000
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    app.listen(port)
    ioloop.IOLoop.current().start()
