from ..models import Complaint


class complaints:

    def addComplaint(self, user, complaint_body):
        complaint = Complaint(complaint_body=complaint_body,
                              account=user)
        complaint.save()

    def getAllComplaints(self):
        return Complaint.objects.all()

    def getComplaint(self, complaint_id):
        return Complaint.objects.get(pk=complaint_id)

    def resolveComplaint(self, complaint_id, account, response):
        complaint = self.getComplaint(complaint_id)
        complaint.lookup_employee = account
        complaint.answer = response
        complaint.save()
