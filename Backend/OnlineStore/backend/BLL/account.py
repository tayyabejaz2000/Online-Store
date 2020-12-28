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

    def editAccount(self, username, password, email, first_name, last_name, phone_number):
        self.data.username = username
        self.data.email = email
        self.data.first_name = first_name
        self.data.last_name = last_name
        self.data.phone_number = phone_number
        if password is not None:
            self.data.set_password(password)
        self.data.save()

    def save(self):
        self.data.save()
