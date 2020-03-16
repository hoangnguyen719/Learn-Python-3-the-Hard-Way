class Room(object):
    def __init__(self, name, description, password=None):
        self.name = name
        self.description = description
        self.password = password
        self.paths = {}

    def go(self, direction, password=None):
        if self.paths.get(direction).password == password:
            return self.paths.get(direction, None)
        else:
            return self

    def add_paths(self, path):
        self.paths.update(path)