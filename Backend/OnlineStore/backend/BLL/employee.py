from .account import account


class employee(account):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], account):
            self.data = args[0].data
        else:
            super().__init__(*args, **kwargs)
