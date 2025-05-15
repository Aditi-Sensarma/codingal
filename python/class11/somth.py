class Emp:
    def __init__(self, id, name, dept, sal):
        self.id = id
        self.name = name
        self.dept = dept
        self.sal = sal

    def info(self):
        print("ID:", self.id, "Name:", self.name, "Dept:", self.dept, "Salary: ₹", self.sal)

    def raise_sal(self, amt):
        self.sal += amt
        print(self.name, "got a raise of ₹", amt, ". New salary: ₹", self.sal)

    def change_dept(self, new_dept):
        print(self.name, "moved from", self.dept, "to", new_dept)
        self.dept = new_dept

e1 = Emp(101, "Alice", "HR", 50000)
e2 = Emp(102, "Bob", "Engineering", 70000)
e3 = Emp(103, "Charlie", "Marketing", 60000)


e1.info()
e3.raise_sal()