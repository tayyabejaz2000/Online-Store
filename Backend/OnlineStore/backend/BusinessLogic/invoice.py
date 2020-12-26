from ..models import Invoice


class invoice(Invoice):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Invoice):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @property
    def total(self):
        return self.net - (self.net * (self.discount/100))
