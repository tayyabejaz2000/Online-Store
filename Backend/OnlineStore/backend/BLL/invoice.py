from ..models import InvoiceModel


class invoice:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], InvoiceModel):
            self.data = args[0]
        else:
            self.data = InvoiceModel(*args, **kwargs)

    @property
    def total(self):
        return self.net - (self.net * (self.discount/100))

    def getNet(self):
        return self.data.net

    def setNet(self, value):
        self.data.net = value
    net = property(getNet, setNet)

    def getDiscount(self):
        return self.data.discount

    def setDiscount(self, value):
        self.data.discount = value
    discount = property(getDiscount, setDiscount)
