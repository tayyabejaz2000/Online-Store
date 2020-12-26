from ..models import UserAccount


class account(UserAccount):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], UserAccount):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)
