from ..models import OrderedProductModel


class orderedproduct:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], OrderedProductModel):
            self.data = args[0]
        else:
            self.data = OrderedProductModel(*args, **kwargs)

    def save(self):
        self.data.save()
