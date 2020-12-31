from .complaint import complaint


class complaints:
    def addComplaint(self, user, complaint_body):
        c = complaint(complaint_body=complaint_body,
                      user=user.data)
        c.save()

    def all(self):
        return complaint.all()

    def get(self, *args, **kwargs):
        return complaint.get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return complaint.filter(*args, **kwargs)

    def exclude(self, *args, **kwargs):
        return complaint.exclude(*args, **kwargs)

    def resolveComplaint(self, complaint_id, employee, response):
        c = complaint(self.get(pk=complaint_id))
        c.resolve(employee, response)
