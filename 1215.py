class Student:
    def __init__(self, id, name, major):
        self._id = id
        self._name = name
        self._major = major

class Teacher:
    pass

class Student_A:
    pass

class Student_B:
    pass

s1 = Student('STUST001','大A','資工')
print("學生s1姓名=",s1._name)
print("學生s1學號=",s1._id)
print("學生s1科系=",s1._major)

s2 = Student('STUST002','大B','資工')
print("學生s2姓名=",s2._name)
print("學生s2學號=",s2._id)
print("學生s2科系=",s2._major)
