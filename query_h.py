import sqlite3 as sqlite
from subprocess import call


class QueryHandler:
    query_id = 1
    current_query = 1
    _queries_with_index = {}

    def __init__(self):
        self.query_insert = None
        self.test_list_of_queries = None
        self.test_file = None

    class _Queries:
        """This class will handle the queries .... it will take the uploaded text of questions and pushes the questions
         with there id into the static dictionary of _queries_with_index
        It also return the whole query text"""

        def __init__(self):
            self._total_queries = 0

        def push_query(self, id_no, student):
            QueryHandler._queries_with_index[id_no] = student

        def return_total_queries(self):
            return QueryHandler._queries_with_index

        def empty(self):
            return len(self._total_queries) == 0

    def questions_uploaded(self, test_file):
        """This method takes the test file an an argument and saves the sends them to the class _Answers"""
        self.test_file = open(test_file).read()
        self.test_list_of_queries = self.test_file.split("\n\n")
        self.test_list_of_queries = [lst for lst in self.test_list_of_queries if lst != ""]
        self.query_insert = QueryHandler._Queries()
        for i in range(len(self.test_list_of_queries)):
            self.query_insert.push_query(i + 1, self.test_list_of_queries[i])

    def show_questions(self):
        trial = QueryHandler()
        if QueryHandler.current_query > QueryHandler.query_id + 2:
            return "You have completed The exam Press Exit the close the exam app"
        else:
            return trial._queries_with_index[QueryHandler.current_query]


class AnswerHandler(QueryHandler):
    answer_of_student = {}

    def __init__(self):
        self.answer = None

    class Answers:
        """Answers from the user are taken here and stored for later analyse in the dictionary if answer_with_id"""

        def __init__(self):
            self._total_answers = 0
            # in the future the students answer length will
            # be compared wit total length of questions

        def push_answers(self, answer):
            AnswerHandler.answer_of_student[QueryHandler.current_query - 1] = answer
            trial = AnswerHandler.answer_of_student[QueryHandler.current_query - 1]
            see = AnswerHandler.Answers()
            print(see.return_total_students())
            
        def return_total_students(self):
            return AnswerHandler.answer_of_student

        def return_peak_index(self):
            return QueryHandler.query_id
        def empty(self):
            return len(self._total_queries) == 0

    def answer_submit(self,answer):
        QueryHandler.current_query += 1
        exec(answer)
        
