#creat a class
class Staff:
    def __init__(self,firstname,lastname,location,role):
        self.fn=firstname
        self.ln=lastname
        self.l=location
        self.r=role

    def staffinformation(self):
        print(self.fn,self.ln,",",self.l,",",self.r)
#with a example(Robert Holmes, International Campus, faculty) to conduct the class
Staff1 = Staff("Robert","Holmes","International Campus","faculty")
Staff1.staffinformation()




