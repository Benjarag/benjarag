    

class Catalog:
    def __init__(self, name):
        self.name = name
        self.collection = []

    def add(self, item):
        self.collection.append(item)

    def remove(self, item):
        if item in self.collection:
            self.collection.remove(item)

    def set_name(self, name):
        self.name = name

    def clear(self):
        self.collection = []

    def __str__(self):
        if not self.collection:
            return str(f"Catalog {self.name}:")
        item_str = "\n".join(["\t" + str(item) for item in self.collection])
        return str(f"Catalog {self.name}:\n{item_str}")
