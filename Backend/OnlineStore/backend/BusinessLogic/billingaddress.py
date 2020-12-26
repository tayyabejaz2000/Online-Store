from ..models import BillingAddress


class billingAddress(BillingAddress):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], BillingAddress):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)
