from ..models import ReviewModel


class review(ReviewModel):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], ReviewModel):
            self.data = args[0]
        else:
            self.data = ReviewModel(*args, **kwargs)

    @staticmethod
    def all():
        return ReviewModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return ReviewModel.objects.get(*args, **kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return ReviewModel.objects.filter(*args, **kwargs)

    def save(self):
        self.data.save()
