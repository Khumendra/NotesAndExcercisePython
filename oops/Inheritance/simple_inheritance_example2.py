class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduation_year = year


x = Student("Mike", 'Tyson', 2021)
print(x.firstname)
print(x.lastname)
print(x.graduation_year)
