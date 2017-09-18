import os
import fnmatch

__all__ = ['routes']

routes = []


def route(path_pattern, extra=None):
    def path_route(cls):
        routes.append((path_pattern, cls, extra))
        return cls
    return path_route


import static  # static file handler
import templates  # template file handler

# common handler
for _, _, service in os.walk(os.path.dirname(__file__)):
    for i in filter(lambda py: fnmatch.fnmatch(py, 's_*.py'), service):
        __import__('project.service.' + i[:-3])
    break  # import just the same level

# import other

