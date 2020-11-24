from django.shortcuts import render,redirect

from datetime import date

import sys

from django.core.files.storage import FileSystemStorage

from .models import StudentRegister,EmployeeRegister,ChartInformation
# Create your views here.


def index(request):
   
   
    return render(request, 'index.html')

def explore(request):

    return render(request,'explorePath.html')

def subscription(request):

    return render(request,'subscription.html')

def resource(request):

    return render(request,'resource.html')

def article(request):

    return render(request,'article.html')

def about(request):

    return render(request,'about.html')

def contact(request):

    return render(request,'contact.html')

def signin(request):

    context={}

    if  request.method=="POST":

        email=request.POST.get('email')

        password=request.POST.get('password')

        
        try:
            print(email,password)

            enter=StudentRegister.objects.get(email=email,password=password)

            request.session['email']=enter.email

            request.session['id']=enter.id

            request.session['name']=enter.name

            return redirect('StudentHome')

           

        except:

            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])

            context['error']=sys.exc_info()[0]
            pass
    return render(request,'signin.html',context)

def signin1(request):

    context={}

    if  request.method=="POST":

        email=request.POST.get('email')

        password=request.POST.get('password')

        
        try:
            print(email,password)

            enter=EmployeeRegister.objects.get(email=email,password=password)

            request.session['email']=enter.email

            request.session['id']=enter.id

            request.session['name']=enter.name


            return redirect('EmployeeHome')


        except:

            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])

            context['error']=sys.exc_info()[0]
            pass



    return render(request,'signin1.html')


def register(request):
    
    context={}

    if request.method=='POST':

        name=request.POST.get('name')

        email=request.POST.get('email')

        password=request.POST.get('password')

        college=request.POST.get('college')

        sid=request.POST.get('sid')

        qual=request.POST.get('qual')

        loc=request.POST.get('loc')

        sex=request.POST.get('sex')

        uploaded_file=request.FILES['image']
   
        fs=FileSystemStorage()

        iname=fs.save(uploaded_file.name,uploaded_file)

        context['url']=fs.url(iname)
        try:
            sr=StudentRegister(name=name,email=email,password=password,college=college,sid=sid,qualification=qual,location=loc,sex=sex,image=iname)
            sr.save()
            context['success']="Registraion Success"
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            context['error']=sys.exc_info()[0]
            pass
        
    return render(request,'register.html',context)

def register1(request):

    context={}

    if request.method=='POST':

        name=request.POST.get('name')

        email=request.POST.get('email')

        password=request.POST.get('password')

        college=request.POST.get('college')

        eid=request.POST.get('eid')

        desg=request.POST.get('desg')

        qual=request.POST.get('qual')

        loc=request.POST.get('loc')

        sex=request.POST.get('sex')

        cfee=request.POST.get('cfee')

        uploaded_file=request.FILES['image']
   
        fs=FileSystemStorage()

        iname=fs.save(uploaded_file.name,uploaded_file)

        context['url']=fs.url(iname)

        try:
            er=EmployeeRegister(name=name,email=email,password=password,college=college,eid=eid,designation=desg,qualification=qual,location=loc,sex=sex,image=iname,cfee=cfee)
            er.save()
            context['success']="Registraion Success"
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            context['error']=sys.exc_info()[0]
            pass


    return render(request,'register1.html',context)

def StudentHome(request):

    context={}

    context['name']=request.session['name']
    
    return render(request,'StudentHome.html',context)

def EmployeeHome(request):

    context={}

    context['name']=request.session['name']
    

    return render(request,'EmployeeHome.html',context)

def vcounciler(request):

    context={}

    obj=EmployeeRegister.objects.all()

    context['obj']=obj

    return render(request,'vcounciler.html',context)

def ViewDetails(request,id):

     context={}
     
     print("The c id is ",id)
     c_id=int(id)
     try:

        c_sel=EmployeeRegister.objects.get(id=c_id)

        context['obj']=c_sel
        print(c_sel.id)
        print(c_sel.name)

     except EmployeeRegister.DoesNotExist:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            context['error']=sys.exc_info()[0]
            pass
            
     
     return render(request,'ViewDetails.html',context)


def ChartDetails(request,eid):

     context={}
     print("Hello world")
     print("The eid is ",eid)

     if request.method=='POST':

        msg=request.POST.get('message')
        
        sid=request.session['id']

        today = date.today()

        # dd/mm/YY
        d1 = today.strftime("%Y/%m/%d") 

        print("Message is ",msg)


    
        try:
            ci=ChartInformation(sid=sid,eid=eid,message=msg,today=d1)
            ci.save()
            context['success']="Message Sent  Success"
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            context['error']=sys.exc_info()[0]
            pass

     #id=int(id)

     context['obj']=eid



     return render(request,"ChartDetails.html",context)

def ChartDetails1(request):

    context={}

    print("Hello world")

    eid=0
    
    if request.method=='POST':

        msg=request.POST.get('message')

        eid=request.POST.get('eid')
        
        sid=request.session['id']

        today = date.today()

        # dd/mm/YY
        d1 = today.strftime("%Y-%m-%d") 

        print("Message is ",msg)


    
        try:
            ci=ChartInformation(sid=sid,eid=eid,message=msg,today=d1)
            ci.save()
            context['success']="Message Sent  Success"
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            context['error']=sys.exc_info()[0]
            pass

     #id=int(id)

    context['obj']=eid



    return render(request,"ChartDetails.html",context)

def  vreplies(request):

    context={}

    sid=request.session['id']

    obj=ChartInformation.objects.all().filter(sid=sid)

    context['obj']=obj


    return render(request,"vreplies.html",context)



def vclients(request):

    context={}

    eid=request.session['id']

    obj=ChartInformation.objects.all().filter(eid=eid)

    context['obj']=obj


    return render(request,"vclients.html",context)





