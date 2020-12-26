from .account import account
from .complaint import complaint


class employee(account):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], account):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    def resolveComplaint(self, comp: complaint, response: str):
        comp.resolve(self, response)
