#creat a class
class Staff:
    def __init__(self,firstname,lastname,location,role):
        self.fn=firstname
        self.ln=lastname
        self.l=location
        self.r=role

    def staffinformation(self,firstname,lastname,location,role):
        print(firstname,lastname,",",location,",",role)
#with a example(Robert Holmes, International Campus, faculty) to conduct the class
s=Staff("Robert","Holmes","International Campus","faculty")
Staff1 = Staff("Robert","Holmes","International Campus","faculty")
staffinformation_=s.staffinformation("Robert","Holmes","International Campus","faculty")



