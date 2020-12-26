from ..models import Category


class category(Category):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Category):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @staticmethod
    def all():
        return Category.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return Category.objects.get(args, kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return Category.objects.filter(args, kwargs)
