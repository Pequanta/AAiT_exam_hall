import query_h


class Analyse_answers:
    def __init__(self, answer_dictionary):
        self.answer_text = open(answer_dictionary).read().split("\n")
        self.answer_with_index = {}
        for ans in range(self.answer_text):
            self.answer_with_index[ans.split(".")[0]] = ans.split(".")[1]

    class _Score:
        def __init__(self):
            self._all_scores = {}
            self._total_score = 0

        def push_score(self, answer_id, score):
            self._all_scores[answer_id] = score
            self._total_score += score

        def return_score(self):
            return self._all_scores

    class _Executer:
        def __init__(self):
            self._all_answers = {}

        def push_answer(self, answer_id, answer):
            self._all_answers[answer_id] = answer

        def return_answers(self):
            return self._all_answers

        def check_the_answer(self, answer):
            #this method will check the answer and it is gonna compare with the exepected
            exec(answer)


    def answer_anaylse(self, true_answers):
        st_answer = query_h.AnswerHandler()
        execute_it = Analyse_answers._Executer()
        for i in range(len(st_answer.answer_of_student)):
            execute_it.check_the_answer(st_answer.answer_of_student[i])


