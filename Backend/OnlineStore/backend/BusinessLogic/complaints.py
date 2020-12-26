from .complaint import complaint


class complaints:
    def addComplaint(self, user, complaint_body):
        c = complaint(complaint_body=complaint_body,
                      account=user)
        c.save()

    def all(self):
        return complaint.all()

    def get(self, *args, **kwargs):
        return complaint.get(args, kwargs)

    def filter(self, *args, **kwargs):
        return complaint.filter(args, kwargs)

    def resolveComplaint(self, complaint: complaint, account, response):
        complaint.resolve(account, response)
