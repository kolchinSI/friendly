from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/Home.html',)

def contact(request):
    return render(request, 'mainApp/basic.html',{'values':['Если возникли вопросы звоните по телефону:',
                                                           '(068)-068-68-68', 'email@mail.ru']})