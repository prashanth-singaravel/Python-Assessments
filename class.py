class student:
    college = 'SONA'
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
    
    def __str__(self):
        return(f"object for {self.name}")

    def printresult(self, mark):
            self.mark = mark
            if (mark>=90):
                print(f"Name of student is {self.name} and reg no {self.regno} is outstanding")
            elif(mark>=75)and(mark<90):
                print(f"Name of student is {self.name} and regno {self.regno} is above avg")
            elif(mark>=50)and(mark<75):
                print(f"Name of student is {self.name} and regno {self.regno} is avg")
            else:
                print(f"Name of student is {self.name} and regno {self.regno} is fail")

prashanth = student("Prashanth", 7001)
print(prashanth)
print(prashanth.regno)
loki = student("loki", 7002)
mark = int(input("Enter the mark"))
prashanth.printresult(mark)
loki.printresult(30)
