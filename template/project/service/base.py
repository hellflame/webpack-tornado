import tornado.web as web


class NormalBase(web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Server', 'NO TELLING YOU')

    def set_safe_cookie(self, key, val):
        from ..config import DEBUG
        if not DEBUG:
            self.set_secure_cookie(key, val, secure=True, httponly=True)
        else:
            self.set_secure_cookie(key, val)

    def get(self, *args, **kwargs):
        return self.send_error(404)

    def post(self, *args, **kwargs):
        return self.send_error(404)

    def write_error(self, status_code, **kwargs):
        if self.request.method == 'GET':
            words = {
                404: ">_< The page is Missing @_@",
                500: "x_x The Server is Crashed Orz"
            }
            return self.render('error.html',
                               code='{}'.format(status_code),
                               msg='{}'.format(
                                   words.get(
                                       status_code,
                                       'Orz= Whoops, Bad things happened !<_<')))
        else:
            return self.write({
                'msg': 'Reference Invalid'
            })



