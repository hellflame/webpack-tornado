# coding=utf8
import os
import sys
import mimetypes

from . import base, routes
from ..config import DEBUG
import tornado.httpclient as httpClient

reload(sys)
sys.setdefaultencoding('utf8')


class StaticService(base.NormalBase):
    def get(self, dirs, path):
        if dirs == 'public':
            target = os.path.join(self.settings['public'], path)
            if not os.path.exists(target) or os.path.isdir(target):
                return self.send_error(404)

            self.set_header("Content-Type", mimetypes.guess_type(target)[0] or
                            'application/octet-stream')

            handle = base.web.StaticFileHandler.get_content(target)
            for i in handle:
                self.write(i)
            return
        elif dirs == 'static':
            if self.settings['debug']:
                try:
                    response = httpClient.HTTPClient().fetch("http://127.0.0.1:8080/static/{}".format(path))
                    self.write(response.body)
                except Exception as e:
                    return self.write("")
            else:
                """
                if not self.request.host == self.settings['domain']:
                    return self.send_error(404)
                """

                target = os.path.join(self.settings['static'], path)
                if not os.path.exists(target) or os.path.isdir(target):
                    return self.send_error(404)

                self.set_header("Content-Type", mimetypes.guess_type(target)[0] or
                                'application/octet-stream')

                handle = base.web.StaticFileHandler.get_content(target)
                for i in handle:
                    self.write(i)
        else:
            return self.send_error(404)

routes.append((r"/(static|public)/(.+?)", StaticService))


class WebpackHMR(base.NormalBase):
    def get(self):
        return self.redirect("http://localhost:8080/__webpack_hmr")

if DEBUG:
    routes.append((r'/__webpack_hmr', WebpackHMR))

