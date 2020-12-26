from ..models import CategoryModel


class category:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], CategoryModel):
            self.data = args[0]
        else:
            self.data = CategoryModel(*args, **kwargs)

    @staticmethod
    def all():
        return CategoryModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return CategoryModel.objects.get(*args, **kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return CategoryModel.objects.filter(*args, **kwargs)

    def getName(self):
        return self.data.name

    def setName(self, value):
        self.data.name = value
    name = property(getName, setName)
