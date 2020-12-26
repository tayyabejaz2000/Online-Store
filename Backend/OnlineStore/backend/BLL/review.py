from ..models import ReviewModel


class review(ReviewModel):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], ReviewModel):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @staticmethod
    def all():
        return ReviewModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return ReviewModel.objects.get(*args, **kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return ReviewModel.objects.filter(*args, **kwargs)

    class Meta:
        abstract = True
