import tornado.ioloop as ioloop
import tornado.web as web
import sys
from project.service import routes
from project.config import settings, DEBUG

# print routes
app = web.Application(handlers=routes, **settings)

if __name__ == '__main__':
    port = 5000
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    if DEBUG:
        address = '0.0.0.0'
    else:
        address = '127.0.0.1'
    app.listen(port, address=address)
    ioloop.IOLoop.current().start()
