from ..models import Complaint
from typing import overload


class complaint(Complaint):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Complaint):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @staticmethod
    def all():
        return Complaint.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return Complaint.objects.get(args, kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return Complaint.objects.filter(args, kwargs)

    def resolve(self, employee, response: str):
        try:
            self.lookup_employee = employee
            self.answer_body = response
            self.save()
        except:
            raise Exception("Couldn't Resolve Complaint")
