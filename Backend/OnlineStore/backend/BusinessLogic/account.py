from ..models import UserAccount


class account(UserAccount):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], UserAccount):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)
            password = kwargs.pop("password", None)
            if password is not None:
                self.set_password(password)
            self.save()

    @staticmethod
    def all():
        return UserAccount.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return UserAccount.objects.get(args, kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return UserAccount.objects.filter(args, kwargs)
