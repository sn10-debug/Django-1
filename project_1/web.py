

from cgitb import text
from django.http import HttpResponse

from django.shortcuts import render

import requests



def invite(request):
    # import subprocess
    # import os
    # os.chdir('C:/Users/user/Desktop/Django')
    # html=subprocess.run('type index.html',shell=True,capture_output=True).stdout
    # # html=Bytes(html,'utf-8')
    

    # with open('info.txt') as file:
    #     html+=bytes("<br>"+file.read(),'utf-8')
        
    # html+=bytes('''<br><a href='https://www.youtube.com/'>You Tube</a><br><a href='http://127.0.0.1:8000/lineremover'>Line Remover</a><br>
    # <a href='http://127.0.0.1:8000/spaceremover'>Space Remover</a><br>
    # <a href='http://127.0.0.1:8000/titlize'>Title the Sentence</a> 
    # ''','utf-8')
    #     # bytes is a class which converts normal string into bytes
    # # print(html)
   
    # return HttpResponse(html)
# Django by defaults puts a parameter request into the function which is a HttpRequest


# Now we can do the same task using templates


# Make sure the templates file is present in folder where manage.py is present and also add 'templates' in the DIRS list in settings.py

    # return render(request,'index.html')

    # This is just one line step

    # We need to pass the http request into the render function
    params={
    'email':'hello@gmail.com'
    }

    data=requests.get('http://127.0.0.1:8000/contact',params=params)
    print(data.text)

    params={
        'greeting':'Whatsup ? This is Shakti Santosh Nayak'
    }
    return render(request,'index.html',params)

    # We can also pass a dictionary into these render function with some keys declared and this is can be accessed by the html

def info(request):
    return HttpResponse("<h3>This is Shakti Santosh Nayak . Welcome to Sigma</h3>")


def details(request):

    # taking value from the form
    text=request.POST.get('email','not provided').lower()
    print(text)
    


    # We give here the name of the element
# We gave default value as like when no text will be entered this will be the value and you can set the default value as chidya also
   

# We colud also get the data about whether a checkbox is selected or not


    remove_line_status=request.POST.get('lineremover','off')
    title_words_status=request.POST.get('title_words','off')
    space_remove_status=request.POST.get('spaceremover','off')
    # off is the default value in all cases and this will be returned when the checkbox is not selected

    print(remove_line_status,title_words_status,space_remove_status)
    output=''

    if title_words_status=='on':
        output+=' '.join([i.title() for i in text.split(' ')])
        print(output)
        # print(output)
    elif space_remove_status=='on':
        output+=''.join(text.split())
    elif remove_line_status=='on':
        output+=' '.join(text.split('\r\n'))
        print(output)
        
    if len(text)>1 and text!='not provided': 
        return HttpResponse(f"<h2>Shakti Santosh Nayak</h2><h3>nshakti.10@gmail.com</h3> <h3>Your output is <pre>{output}</pre></h3>")
    else:
        return HttpResponse(f"<h2>Shakti Santosh Nayak</h2><h3>nshakti.10@gmail.com</h3>")
    


# In the get request the parameters appear in the url and if we dont want that then we have to use get requests

# Also the method of form is by default post


def lineremover(request):
    return HttpResponse('''<a href='/'>Back to Home</a>
    <br> <textarea rows="10" cols="50">Enter your Text ot remove \n</textarea><br>
    <button> Submit</button>''')
    


def spaceremover(request):
    return HttpResponse('''<a href='/'>Back to Home</a>
    <br> <textarea rows="10" cols="50">Enter your Text to remove whitespace </textarea><br>
    <button> Submit</button>''')


def title_words(request):
    return HttpResponse('''<a href='/'>Back to Home</a>
    <br> <textarea rows="10" cols="50">Enter your Text to titlize </textarea><br>
    <button> Submit</button>''')


# There is also a pre tag which print te response as it is received from the Httpresponse