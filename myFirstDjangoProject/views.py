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

def courseDetails(request, courseid):
    return HttpResponse(courseid)

def userForm(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            sex = request.POST['sex']
            print(name)
            print(sex)
    except:
        pass
    return render(request, "userforms.html")