from . import base, routes
from ..model.eg_model import Hello


class HelloService(base.NormalBase):
    def get(self):
        return self.write(Hello().say())

routes.append((r'/hello', HelloService))

