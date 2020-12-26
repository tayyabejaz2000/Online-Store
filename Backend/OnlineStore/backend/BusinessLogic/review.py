from ..models import Review


class review(Review):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Review):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @staticmethod
    def all():
        return Review.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return Review.objects.get(args, kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return Review.objects.filter(args, kwargs)
