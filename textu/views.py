# Created by me for creating different views
from django.http import HttpResponse
from django.shortcuts import render,redirect
from textu.models import Contact
from django.contrib import messages
from datetime import datetime
import pyperclip

# ---------------------------------HOME PAGE---------------------------------------------------
def index(request):
    return render(request,'index.html')

# ------------------------------ANALYZED SECTION---------------------------------------------
def analyze(request):
    djtext = request.POST.get('text-area','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    lowercase = request.POST.get('lowercase','off')
    extraspace = request.POST.get('extraspace','off')
    etext = request.POST.get('etext','off')
    decrypttext = request.POST.get('decrypttext','off')

  
    if removepunc == "on":
        punctuations = '''!@#$%^&*()_-=,.<>/?\|[]{}:;`~'"'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        parameters = {'purpose':'Removed Punctuations',"analyzed_text":analyzed}
        djtext = analyzed

    if fullcaps=="on":
        analyzed = ""
        analyzed = djtext.upper()
        parameters = {'purpose':"To Uppercase","analyzed_text":analyzed}
        djtext = analyzed
    
    if lowercase =="on":
        analyzed = ""
        analyzed = djtext.lower()
        parameters = {'purpose':"To LowerCase","analyzed_text":analyzed}
        djtext = analyzed


    if extraspace=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed+char
        parameters = {'purpose':"Extra space remover","analyzed_text":analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed+char
        parameters = {'purpose':"New-line remover","analyzed_text":analyzed}

    if etext == 'on':
        analyzed = ""
        for char in djtext:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + 3) % 26 + ascii_offset)
                analyzed = analyzed + encrypted_char
            else:
                analyzed = analyzed + char
            
        parameters = {'purpose':"Encrypted text","analyzed_text":analyzed}

    if decrypttext == 'on':
        analyzed = ""
        for char in djtext:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - 3) % 26 + ascii_offset)
                analyzed += decrypted_char
            else:
                analyzed += char

        parameters = {'purpose':"Decrypted text","analyzed_text":analyzed}
    
    if(removepunc!='on' and fullcaps!='on' and newlineremover !='on' and extraspace !='on' and lowercase !='on' and etext != 'on' and decrypttext != 'on'):
        parameters = {'purpose':'Not-selected'}
        return render(request,'analyze.html',parameters)
    else:
        return render(request,'analyze.html',parameters)

# --------------------------------------TEXT COPY---------------------------------------------
def copytext(request):
    analyzed_text = request.POST.get('ctext')
    pyperclip.copy(analyzed_text)
    return redirect("/")

# ----------------------------------------ABOUT-----------------------------------------------
def about(request):
    return render(request,'about.html')

# ---------------------------------------CONTACT-----------------------------------------------
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,mail=mail,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request,'contact.html')
