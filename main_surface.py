import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as ms
import tkinter.filedialog as filedialog

import instructor_final_analyses
import query_h
import user_authentication

from PIL import ImageTk, Image

true_answer = None
name = None
id_no = None
section = None


class ExamHall(tk.Tk):
    secret_key = ""

    def __init__(self):
        super().__init__()
        self.title("Exam Hall")
        self.geometry("1500x800+70+0")
        self.config(bg="black")

        self.resizable(False, False)
        self.title_n = tk.Label(self, text="Welcome To AAiT Programming Exam!", font=("Verdana", 30, "bold"),
                                bg="black", fg="#80c1ff")
        self.title_n.grid(row=0, column=0, padx=230, pady="30")

        sign_in_btn = tk.Button(self, text="Sign In", font=("Arial", 20, "italic"), fg="yellow", bg="black",
                                activebackground="white", activeforeground="black", command=lambda: sign_in(self))
        sign_in_btn.grid(row=2, column=0, pady=40, columnspan=2)
        instruction_lbl = tk.Label(self,text="----> Do not make any sort of activity that can disturb other students\n-----> \
Any sort of cheating is strictly forbidden\n-----> It is not allowed to use more time than given",
                                   font=("Verdana", 24, "bold"), bg="black", fg="white")
        instruction_lbl.place(relx=0.1, rely=0.4)
        self.bg_img = Image.open("image7.webp")
        self.bg_img_int = ImageTk.PhotoImage(self.bg_img)
        self.introduction_frm = tk.Label(self, image = self.bg_img_int)
        self.introduction_frm.place(relwidth=1, relheight=1)

        lbl_intro = tk.Label(self.introduction_frm,
                             text="Please this page is only to be used by the instructor\n\nupload a file with "
                                  ".txt extension",
                             font=("Gill Sans", 30, "bold"), bg="#2F3135", fg="#CCD618")
        lbl_intro.place(relx=0.18, rely=0.1)

        def upload_file():
            self.test_file = tk.filedialog.askopenfilename(initialdir="/")
            test_sent = query_h.QueryHandler()
            test_sent.questions_uploaded(self.test_file)

        def upload_student_info():
            self.student_info = tk.filedialog.askopenfilename(initialdir="/")
            student_info = user_authentication.checkUserCredentials()
            student_info.user_registration(self.student_info)

        def continue_app():
            ExamHall.secret_key += self.secret_key_entry.get()
            self.introduction_frm.destroy()

        self.upload_test_file = tk.Button(self.introduction_frm, text="upload exam file", font=("Verdana", 30, "bold"),
                                          bg="#F9AA33",
                                          command=upload_file)
        self.upload_test_file.place(relx=0.36, rely=0.3)

        self.upload_students_name_and_id = tk.Button(self.introduction_frm, text="upload student information file",
                                                     font=("Verdana", 30, "bold"), bg="#F9AA33",
                                                     command=upload_student_info)
        self.upload_students_name_and_id.place(relx=0.27, rely=0.45)

        secret_key_lbl = tk.Label(self.introduction_frm, text="Enter the secret Key", bg="black", fg="white",
                                  font=("Verdana", 20, "bold"))
        secret_key_lbl.place(relx=0.17, rely=0.81)

        self.secret_key_entry = tk.Entry(self.introduction_frm, font=("Verdana", 30, "bold"), show="*")
        self.secret_key_entry.place(relx=0.4, rely=0.8)

        next_btn_of_intro = tk.Button(self.introduction_frm, text="Next", font=("Arial", 20, "bold"),
                                      command=continue_app)
        next_btn_of_intro.place(relx=0.85, rely=0.8)


def exam_room(name, id_no, section):
    query_frm = tk.Frame()
    query_frm.place(relwidth=0.3, relheight=1)
    query_text = tk.Text(query_frm, font=("Verdana", 15, "bold"), fg="black")
    query_text.place(relwidth=1, relheight=1)
    query_text.config(state="disabled")

    exam_frm = tk.Frame()
    exam_frm.configure(bg="white")
    exam_frm.place(relx=0.3, relwidth=0.7, relheight=1)
    lbl_frm = tk.Frame(exam_frm)
    lbl_frm.configure(bg="#36c3fe")
    lbl_frm.place(relwidth=1, relheight=0.3)
    pro_text = tk.Text(exam_frm, font=("Arial", 13, "bold"))
    pro_text.place(rely=0.2, relwidth=1, relheight=0.8)
    tk.Label(lbl_frm, text="Name", font=("Verdana", 25, "bold"), bg="#36c3fe", fg="black").grid(row=0, column=0)
    tk.Label(lbl_frm, text="ID", font=("Verdana", 25, "bold"), bg="#36c3fe", fg="black").grid(row=1, column=0)
    tk.Label(lbl_frm, text="Section", font=("Verdana", 25, "bold"), bg="#36c3fe", fg="black").grid(row=2, column=0)
    tk.Label(lbl_frm, text=name, font=("Verdana", 25, "bold"), bg="#36c3fe", fg="black").grid(row=0, column=1,
                                                                                              padx=300)
    tk.Label(lbl_frm, text=id_no, font=("Verdana", 25, "bold"), bg="#36c3fe", fg="black").grid(row=1, column=1,
                                                                                               padx=300)
    tk.Label(lbl_frm, text=section, font=("Verdana", 25, "bold"), bg="#36c3fe", fg="black").grid(row=2, column=1,
                                                                                                 padx=300)
    query_text.config(state="normal")

    def start():
        query_display = query_h.QueryHandler()
        query_text.config(state="normal")
        query_text.insert(1.0, query_display.show_questions())
        query_text.config(state="disabled")
        pre_test = open("text_static.txt","r").read()
        pro_text.insert(1.0, pre_test)

    cmd = ms.showinfo("Start the exam", "Press Ok to start the exam")
    if cmd:
        start()

    def submit_ans():
        soln_text = pro_text.get(1.0, "end")
        pre_test = open("text_static.txt","r").read()
        pro_text.delete(1.0,"end")
        pro_text.insert(1.0, pre_test)

        analyser = query_h.AnswerHandler()
        analyser.answer_submit(soln_text)
        query_display = query_h.QueryHandler()
        if query_display.current_query > query_display.query_id + 2:
            btn_submit.config(state="disabled")
        

        query_text.config(state="normal")
        query_text.delete(1.0, "end")
        query_text.insert(1.0, query_display.show_questions())
        query_text.config(state="disabled")

    def exiting_tasks():
        closed_frm = tk.Frame(root)
        closed_frm.config(bg="#80c1ff")
        closed_frm.place(relwidth=1, relheight=1)
        closed_lbl = tk.Label(closed_frm, text="Only to be used by the instructor", font=("Verdana", 30, "bold"),bg = "#80c1ff")
        closed_lbl.place(relx=0.2, rely=0.15)
        
        lbl_secret_key = tk.Label(closed_frm, text="Enter the secret Key", font=("Verdana", 25, "italic"),bg = "#80c1ff")
        lbl_secret_key.place(relx=0.15, rely=0.5)
        entry_secret_key = tk.Entry(closed_frm,font=("Verdana",25,"bold"))
        entry_secret_key.place(relx=0.6, rely=0.5, relwidth=0.4, relheight=0.07)

        upld_answer = tk.Label(closed_frm, text="upload the answer file with .txt extension",
                               font=("Verdana", 25, "bold"),bg = "#80c1ff")
        upld_answer.place(relx=0.05, rely=0.6)

        def upload_answer():
            global true_answer
            true_answer = filedialog.askopenfilename(initialdir="/")

        upld_answer_btn = tk.Button(closed_frm, text="Upload", font=("Verdana", 25, "bold"), command=upload_answer)
        upld_answer_btn.place(relx=0.7, rely=0.6)

        def answer_evaluate():
            if entry_secret_key.get() == ExamHall.secret_key:
                send_analyse = instructor_final_analyses.Analyse_answers()
                send_analyse.answer_upload(true_answer)
                send_analyse.answer_anaylse()
                frm_last_display = tk.Toplevel(closed_frm)
                frm_last_display.config(bg = "#80c1ff")
                frm_last_display.geometry("800x700+350+200")
                frm_last_display.wm_transient(closed_frm)
                tk.Label(frm_last_display, text = "Student Name", font=("Verdana",25,"bold"),bg = "#80c1ff").place(relx=0.1, rely=0.1)
                tk.Label(frm_last_display, text = "id No", font=("Verdana",25,"bold"),bg = "#80c1ff").place(relx=0.1, rely=0.15)
                tk.Label(frm_last_display, text = "Section", font=("Verdana",25,"bold"),bg = "#80c1ff").place(relx=0.1, rely=0.2)

                tk.Label(frm_last_display, text = name, font=("Verdana",25,"bold"),bg = "#80c1ff").place(relx=0.5, rely=0.1)
                tk.Label(frm_last_display, text = id_no, font=("Verdana",25,"bold"),bg = "#80c1ff").place(relx=0.5, rely=0.15)
                tk.Label(frm_last_display, text = section, font=("Verdana",25,"bold"),bg = "#80c1ff").place(relx=0.5, rely=0.2)

                tk.Label(frm_last_display, text = "Total Score", font=("Verdana",25,"bold"),bg = "#80c1ff").place(relx=0.1, rely=0.3)
                score = instructor_final_analyses.Analyse_answers._Score()
                acquired = instructor_final_analyses.Analyse_answers()
                total_question = score.return_score()
                tota_sum = 0
                for n in score.return_score().keys():
                    tota_sum += score.return_score()[n]
                

                tk.Label(frm_last_display, text = str(tota_sum) + "/" + str(len(total_question)), font=("Verdana",25,"bold")).place(relx=0.5, rely=0.3)
                
            else:
                ms.showerror("Invalid key", "Please enter the right key")


        evaluate_answer = tk.Button(closed_frm, text="Evaluate", font=("Verdana", 25, "bold"),
                                    command=answer_evaluate)
        evaluate_answer.place(relx=0.37, rely=0.8)

    btn_submit = tk.Button(exam_frm, text="submit", font=("Verdana", 17, "bold"), command=submit_ans)
    btn_submit.place(relx=0.85, rely=0.9)
    btn_exit = tk.Button(lbl_frm, text="Exit", font=("Verdana", 20, "bold"), command=exiting_tasks)
    btn_exit.place(relx=0.7, rely=0.3)


def sign_in(self):
    sign_frm = tk.Toplevel(self)
    sign_frm.title("Sign In")
    sign_frm.configure(bg="#36c3fe")
    sign_frm.geometry("700x600+400+200")
    sign_frm.wm_transient(self)
    frm_lbl = tk.Label(sign_frm, text="Student Information", font=("Verdana", 25, "bold"), bg="#36c3fe")
    frm_lbl.place(relx=0.25, rely=0.15)

    tk.Label(sign_frm, text="Name", font=("Verdana", 21, "bold"), bg="#36c3fe", fg="black").place(relx=0.1,
                                                                                                  rely=0.3)
    tk.Label(sign_frm, text="ID", font=("Verdana", 21, "bold"), bg="#36c3fe", fg="black").place(relx=0.1, rely=0.4)
    tk.Label(sign_frm, text="Section", font=("Verdana", 21, "bold"), bg="#36c3fe", fg="black").place(relx=0.1,
                                                                                                     rely=0.5)

    name_entry = ttk.Entry(sign_frm, font=("Arial", 16, "italic"))
    name_entry.place(relx=0.3, rely=0.3, relwidth=0.5, relheight=0.05)
    id_entry = ttk.Entry(sign_frm, font=("Arial", 16, "italic"))
    id_entry.place(relx=0.3, rely=0.4, relwidth=0.5, relheight=0.05)
    section_entry = ttk.Entry(sign_frm, font=("Arial", 16, "italic"))
    section_entry.place(relx=0.3, rely=0.5, relwidth=0.5, relheight=0.05)

    def back_c():
        sign_frm.destroy()

    def log_in():
        name = name_entry.get()
        id_no = id_entry.get()
        section = section_entry.get()
        check_user_info = user_authentication.checkUserCredentials()

        if check_user_info.user_authentication(name, id_no) == "Only user name":
            ms.showerror("Invalid id number", "Try again")
        elif check_user_info.user_authentication(name, id_no) == "Incorrect User Name":
            ms.showerror("Invalid user name", "Try again")
        elif check_user_info.user_authentication(name, id_no) == "Invalid User":
            ms.showerror("Invalid User", "invalid user")
        else:
            sign_frm.destroy()
            exam_room(name, id_no, section)

    back_btn = tk.Button(sign_frm, text="Back", font=("Verdana", 17, "bold"), command=back_c)
    back_btn.place(relx=0.01, rely=0.9)
    login_btn = tk.Button(sign_frm, text="Log In", font=("Verdana", 17, "bold"), command=log_in)
    login_btn.place(relx=0.85, rely=0.9)


if __name__ == "__main__":
    root = ExamHall()
    root.mainloop()
