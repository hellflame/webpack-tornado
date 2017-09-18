# coding=utf8
import os
import sys
import mimetypes

from . import base, route
from ..config import DEBUG
import tornado.httpclient as httpClient
from tornado import gen

reload(sys)
sys.setdefaultencoding('utf8')


@route(r'/(static|public)/(.+?)')
class StaticService(base.NormalBase):
    @gen.coroutine
    def get(self, dirs, path):
        if dirs == 'public':
            target = os.path.join(self.settings['public'], path)
            if not os.path.exists(target) or os.path.isdir(target):
                self.send_error(404)
            else:
                self.set_header("Content-Type", mimetypes.guess_type(target)[0] or
                                'application/octet-stream')

                handle = base.web.StaticFileHandler.get_content(target)
                for i in handle:
                    self.write(i)
                    yield self.flush()

        elif dirs == 'static':
            if self.settings['debug']:
                client = httpClient.HTTPClient()
                try:
                    response = client.fetch("http://{}:8080/static/{}".format(self.request.host.split(":")[0], path))
                    self.write(response.body)
                except Exception as e:
                    self.write("")
                client.close()
            else:
                """
                # Restrict the Referer Hosts
                if not self.request.host == self.settings['domain']:
                    return self.send_error(404)
                """

                target = os.path.join(self.settings['static'], path)
                if not os.path.exists(target) or os.path.isdir(target):
                    self.send_error(404)
                else:
                    self.set_header("Content-Type", mimetypes.guess_type(target)[0] or
                                    'application/octet-stream')

                    handle = base.web.StaticFileHandler.get_content(target)
                    for i in handle:
                        self.write(i)
                        yield self.flush()
        else:
            self.send_error(404)


if DEBUG:
    @route(r'/__webpack_hmr')
    class WebpackHMR(base.NormalBase):
        def get(self):
            # event stream redirect
            return self.redirect("http://{}:8080/__webpack_hmr".format(self.request.host.split(":")[0]))


