import sqlite3 as sql


class checkUserCredentials:
    _student_name_with_id = {}

    def __init__(self):

        self.student_register = None
        self.student_info_list = None
        self.student_file = None

    class _Students_info:
        def __init__(self):
            self.student_total = 0

        def push_student(self, student, id_no):
            self.student_total += 1
            checkUserCredentials._student_name_with_id[student] = id_no

        def return_total_students(self):
            return checkUserCredentials._student_name_with_id

        def empty(self):
            return len(self._score) == 0

    def user_authentication(self, name, id_no):

        user_check = self._Students_info()

        if name in user_check.return_total_students():
            if user_check.return_total_students()[name] == id_no:
                return True
            else:
                return "Only user name"
        elif id_no in user_check.return_total_students().values():
            return "Incorrect User Name"
        else:
            return "Invalid User"

    def user_registration(self, student_file):
        self.student_file = open(student_file).read()
        self.student_info_list = self.student_file.split("\n")
        self.student_register = checkUserCredentials._Students_info()
        for i in range(len(self.student_info_list)):
            single_student_info = self.student_info_list[i].split("-")
            self.student_register.push_student(single_student_info[0].strip(), single_student_info[1].strip())

