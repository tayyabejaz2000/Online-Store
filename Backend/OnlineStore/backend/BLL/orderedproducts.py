from .orderedproduct import orderedproduct


class orderedproducts:
    def all(self):
        return orderedproduct.all()

    def get(self, *args, **kwargs):
        return orderedproduct.get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return orderedproduct.filter(*args, **kwargs)
