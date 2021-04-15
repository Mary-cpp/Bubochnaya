from bottle import post, request
import re
import pdb


#Паттерн для проверки адреса электронной почты 
@post('/home', method='post')
def my_form():
    user_requests = {}
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    if((mail=='')|(question=='')):
        return "Please, put all information"
    else:
        if(re.match(r"^\w+@\w+(\.\w+)+$", mail)):
           mail = request.forms.get('ADRESS')
           user_requests[mail] = question
           pdb.set_trace()
           return "Thanks! The answer will be sent to the mail %s" % mail         
        else:
            return "Please, put a correct email (like www@mail.com)"