class employee:
    employeeid = 0
    name = None
    gender = None
    department = None
    mobileNo = None
    email = None
    sin_no = None
    salary = None
    Category = None

    def __init__(self, empId, name, gender, dept, mobileno, email, sin_no, salary):
        self.employeeid = empId
        self.name = name
        self.gender = gender
        self.department = dept
        self.mobileNo = mobileno
        self.email = email
        self.sin_no = sin_no
        self.salary = salary