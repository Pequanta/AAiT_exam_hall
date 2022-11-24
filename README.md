# class_projects
Class projects : both in progress and completed#
Notice : This porject was undertaken as a group assignment to be submitted in a given diedline(AAiT)
#Requirements:
--->To run the executable file , there is no much of required
To run the source code:
1.python3.x version
2.tkinter module(any version compatable with python3)
3.pillow module(any version compatable with python3)



#Introduction
    The programme was assigned as ExamHall in order to be more descriptive.Its usage is to offer a protatype for making fully developed, self-contained and
easly usable examination system.It has 5 surfaces in which there are particular tasks that can be carried out either by the instructor or the student.
In the first surface there are two upload buttons using which the instructor inserts the test file and the student list file. Both files should be in 
extension of .txt and the test file should be in the following format:
example(test.txt):
1.First question

2.Second question

3. And so on!

!! This format is required so that the written code can identify one question from another one using the method '.split("\n")'
And also the student list file should be in the following foramt:

student1 - id_number1
student2 - id_number2
and so on.

Ther is also the secret_key_entry in this page. This task is needed so that only the teacher will analyse the final result on the last page and no one else
would have access to do so.

    In the next page the student is given a caution which are general in exam hall.After hitting the 'sign in' button the authentication page will be poped
out.In this page the user is required to enter his/her name and his/her id number(This are what are used in order to authenticate the user).When the user 
hitsthe 'Log in' button, the 'checkUserCredentials()' class of the 'user_authentication' module is called.If the user is not authentic, she/he will recieve succecic
errors implying what gone wrong.If qualified , then the user will be led to the exam page.



