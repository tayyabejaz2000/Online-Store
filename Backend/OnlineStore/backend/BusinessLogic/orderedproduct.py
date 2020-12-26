from ..models import OrderedProduct


class orderedproduct(OrderedProduct):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], OrderedProduct):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)
