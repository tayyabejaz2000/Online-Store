from ..models import AccountModel


class account:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], AccountModel):
            self.data = args[0]
        else:
            self.data = AccountModel(args, kwargs)

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
