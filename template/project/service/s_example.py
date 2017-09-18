from . import base, route
from ..model.eg_model import Hello


@route(r'/hello')
class HelloService(base.NormalBase):
    def get(self):
        self.logger.info("Tornado Said Hi ~")
        self.logger.error("You Should Not Use This Part!")
        return self.write(Hello().say())
