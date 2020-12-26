from ..models import BillingAddressModel


class billingAddress:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], BillingAddressModel):
            self.data = args[0]
        else:
            self.data = BillingAddressModel(*args, **kwargs)

    def save(self):
        self.data.save()
