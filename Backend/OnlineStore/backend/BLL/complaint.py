from ..models import ComplaintModel


class complaint:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], ComplaintModel):
            self.data = args[0]
        else:
            self.data = ComplaintModel(*args, **kwargs)

    @staticmethod
    def all():
        return ComplaintModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return ComplaintModel.objects.get(*args, **kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return ComplaintModel.objects.filter(*args, **kwargs)

    def getComplaintBody(self):
        return self.data.complaint_body

    def setComplaintBody(self, value):
        self.data.complaint_body = value
    complaint_body = property(getComplaintBody, setComplaintBody)

    def getAnswerBody(self):
        return self.data.answer_body

    def setAnswerBody(self, value):
        self.data.answer_body = value
    answer_body = property(getAnswerBody, setAnswerBody)

    def getUser(self):
        return self.data.user

    def setUser(self, value):
        self.data.user = value
    user = property(getUser, setUser)

    def getLookUpEmployee(self):
        return self.data.lookup_employee

    def setLookUpEmployee(self, value):
        self.data.lookup_employee = value
    lookup_employee = property(getLookUpEmployee, setLookUpEmployee)

    def resolve(self, employee, response: str):
        try:
            self.lookup_employee = employee
            self.answer_body = response
            self.save()
        except:
            raise Exception("Couldn't Resolve Complaint")

    def save(self):
        self.data.save()
