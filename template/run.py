from tornado.options import options, define, parse_command_line
import tornado.ioloop as ioloop
import tornado.web as web
import logging
import sys

from project.service import routes
from project.config import settings, DEBUG

define('port', default=5000, help="Running port")

# print routes
app = web.Application(handlers=routes, **settings)

if __name__ == '__main__':
    parse_command_line()
    if DEBUG:
        # ip = 0.0.0.0, so other devices can access
        address = '0.0.0.0'
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        # running at localhost and different ports to use nginx for load balancing
        address = '127.0.0.1'

        """
            better to log into sys.stdout,
            and use `supervisor` or some other tools to redirect to safe file
        """
        logging.getLogger().setLevel(logging.WARNING)

    logging.info("app runs at http://{}:{}".format(address, options.port))
    app.listen(options.port, address=address)
    ioloop.IOLoop.current().start()
