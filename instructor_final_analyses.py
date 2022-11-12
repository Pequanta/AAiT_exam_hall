import query_h


class Analyse_answers:
    true_answer_with_index = {}
    all_scores = {}
    total_result = 0
    def __init__(self):
            pass
    class _Score:
        def __init__(self):
            self.all_scores = Analyse_answers.all_scores
        def push_score(self, answer_id, score):
            self.all_scores[answer_id] = score
        def return_score(self):
            return self.all_scores


    def answer_anaylse(self):
        st_answer = query_h.AnswerHandler()
        tr_ans = Analyse_answers()
        sc_instance = Analyse_answers._Score()
        for i in range(len(tr_ans.true_answer_with_index)):
            if tr_ans.true_answer_with_index[i+1] == st_answer.answer_of_student[i+1]:
                sc_instance.push_score(i+1,1)
                tr_ans.total_result += 1
                print(sc_instance.return_score())
                
            else:
                sc_instance.push_score(i+1, 0)
                print(sc_instance.return_score())
        self.sum = tr_ans
    def return_res(self):
        return Analyse_answers.total_result
        
    def return_result(self):
        return Analyse_answers.total_result
        
        

    def answer_upload(self, true_answer):
        true_answer_lst = open(true_answer).read().strip().split("\n")
        ans_instance = Analyse_answers()
        for ans in true_answer_lst:
            ans_instance.true_answer_with_index[int(ans.split(".")[0].strip())] = ans.split(".")[1].strip()
    
