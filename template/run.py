import tornado.ioloop as ioloop
import tornado.web as web
import logging
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
        logging.basicConfig(level=logging.DEBUG)
    else:
        # running at localhost and different ports to use nginx for load balancing
        address = '127.0.0.1'

        """
            better to log into sys.stdout,
            and use `supervisor` or some other tools to redirect to safe file
        """
        logging.basicConfig(level=logging.WARNING)

    print("app runs&reload at http://{}:{}".format(address, port))
    app.listen(port, address=address)
    ioloop.IOLoop.current().start()
