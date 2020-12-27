from ..models import AccountModel


class account:
    def __init__(self, *args, **kwargs):
        self.data = None
        if len(args) > 0 and isinstance(args[0], AccountModel):
            self.data = args[0]
        else:
            password = kwargs.pop("password", None)
            self.data = AccountModel(*args, **kwargs)
            if password is not None:
                self.data.set_password(password)

    @staticmethod
    def all():
        return AccountModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return AccountModel.objects.get(*args, **kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return AccountModel.objects.filter(*args, **kwargs)

    def save(self):
        self.data.save()
