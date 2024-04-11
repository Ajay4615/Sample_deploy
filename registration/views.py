from django.shortcuts import render , redirect
from django.http import HttpResponse
# from .forms import GymRegistrationForm   


# def welcome(request):
#     return render(request , 'welcome.html')    

def welcome(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to Deployment</title>
    </head>
    <body>
        <h1>Welcome to Deployment</h1>
        <img src="registration/static/deploy.jpeg" alt="Deployment Image">
    </body>
    </html>
    """
    return HttpResponse(html_content)
