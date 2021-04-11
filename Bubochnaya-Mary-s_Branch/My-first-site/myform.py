from bottle import post, request
import re

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    return "Thanks! The answer will be sent to the mail %s" % mail

#Проверка заполненности полей формы 
@post('/home', method='post')
def my_form():
    if((request.forms.get('ADRESS')=='')|(request.forms.get('QUEST')=='')):
        return "Please, put all information"
    else:
        mail = request.forms.get('ADRESS')
        return "Thanks! The answer will be sent to the mail %s" % mail

#Паттерн для проверки адреса электронной почты 
@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    if((mail=='')|(question=='')):
        return "Please, put all information"
    else:
        if(re.match(r"^\w+@\w+(\.\w+)+$", mail)):
           mail = request.forms.get('ADRESS')
           return "Thanks! The answer will be sent to the mail %s" % mail
        else:
            return "Please, put a correct email."
