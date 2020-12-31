from ..models import OrderedProductModel


class orderedproduct:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], OrderedProductModel):
            self.data = args[0]
        else:
            self.data = OrderedProductModel(*args, **kwargs)

    @staticmethod
    def all():
        return OrderedProductModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return OrderedProductModel.objects.get(*args, **kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return OrderedProductModel.objects.filter(*args, **kwargs)

    def save(self):
        self.data.save()
