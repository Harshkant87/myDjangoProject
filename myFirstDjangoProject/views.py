from django.http import HttpResponse
from django.shortcuts import render #for rendering html pages 

# def homePage(request):
#     data = {
#         'title': 'Home Page',
#         'text_data': 'Hi My Name is Harsh Kant!',
#         'skills': ['C', 'C++', 'Python'],
#         'numbers': [10, 20, 30, 40, 50],
#         'parents_details' : [
#             {'name': 'Uday', 'Age': '45'},
#             {'name': 'Niva', 'Age': '40'}
#         ]
#     }
#     return render(request, "index.html" ,data) #rendering the homepage html page

def homePage(request):
    return render(request, "index.html") #rendering the homepage html page

def aboutUs(request):
    return render(request, "about.html") #defining views

def Course(request):
    return HttpResponse("<b> These are the courses we offer! </b>")

def contact(request):
    return render(request, "contact.html")

def calculator(request):
    result = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                result = n1 + n2
            elif opr == "-":
                result = n1 - n2
            elif opr == "*":
                result = n1 * n2
            elif opr == "/":
                result = n1 / n2

    except:
        result = "Invalid Operation!"
    # print(result) print the result
    return render(request, 'calculator.html', {'result': result})

def courseDetails(request, courseid):
    return HttpResponse(courseid)

def evenodd(request):
    result = ' '

    if request.method == "POST":
        num = eval(request.POST.get('num1'))
        if num % 2 == 0:
            result = 'Even'
        else:
            result = 'Odd'

    return render(request, 'evenodd.html', {'result': result})