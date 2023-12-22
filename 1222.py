class Course:
    def __init__(self, course_code, course_name, credit, compulsory, instructor, class_time):
        self.course_code = course_code
        self.course_name = course_name
        self.credit = credit
        self.compulsory = compulsory
        self.instructor = instructor
        self.class_time = class_time

    def print_course_info(self):
        print("課程代碼: {}".format(self.course_code))
        print("課程名稱: {}".format(self.course_name))
        print("學分數: {}".format(self.credit))
        print("必選修: {}".format("必修" if self.compulsory else "選修"))
        print("任課老師: {}".format(self.instructor))
        print("上課時間: {}".format(self.class_time))

    def modify_course_name(self, new_name):
        self.course_name = new_name
        print("課程名稱已修改為: {}".format(new_name))

    def modify_instructor(self, new_instructor):
        self.instructor = new_instructor
        print("任課老師已修改為: {}".format(new_instructor))

    def modify_class_time(self, new_class_time):
        self.class_time = new_class_time
        print("上課時間已修改為: {}".format(new_class_time))

    def query_class_time(self):
        return self.class_time

    def query_instructor(self):
        return self.instructor


# 使用建構子建立物件
c1 = Course("1215", "微處理機應用實務", 3, True, "吳建中", "禮拜一 1,2,3節")
c2 = Course("1222", "套裝軟體應用", 3, False, "李宗儒", "禮拜五 1,2,3節")

# 使用副函式操作物件
c1.print_course_info()
c1.modify_course_name("套裝軟體應用")
c1.modify_instructor("李宗儒")
c1.modify_class_time("禮拜五 1,2,3節")

# 再次列印課程資訊
c1.print_course_info()

# 查詢上課時間和任課老師
print("上課時間:", c1.query_class_time())
print("任課老師:", c1.query_instructor())
