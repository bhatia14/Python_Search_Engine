from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.models import Course, Book, Author,Topic, Student, ModelImageUpload
from myapp.forms import TopicForm, InterestForm, ForgotForm, RegisterForm, ModelImageUploadForm
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response 
from django.core.urlresolvers import reverse
from django.db.transaction import commit
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from pip._vendor import requests
from django.core.mail import send_mail
import random
from datetime import *
import datetime

# Create your views here.
auth= User.objects.all()




def set_cookie(response, key, value, counter):
  if counter is None:
    counter=0;
  else:
    counter+=1
  #expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value)

def index(request):        # This is your index view function
    # Access db to get list of courses. limit 10
    courselist = Course.objects.all()[:10]        
    response = HttpResponse()        # Create empty response object
    
   # For each course, create a str to write to response
    for course in courselist:
        para = '<p>' + str(course) + '</p>'      # This is the new string      
       # response.write(para) # Add each str as a <p> to response obj
   # return response
    return render_to_response('myapp/index.html', {'courselist': courselist, 'auth': auth},) 

def about(request):        # This is your index view function
    # Access db to get list of courses. limit 10
    message = "This APP let you view and select courses to register in."        
    response = HttpResponse()        # Create empty response object

   # For each course, create a str to write to response
    a={}
    para = '<p>' + str(message) + '</p>'      # This is the new string      
    response.write(para) # Add each str as a <p> to response obj
    request.session.set_test_cookie()
   
    """  a=request.COOKIES.get('key', 'nocookie')
    #if a.get("key")==None:
    response = HttpResponse("hello")
    set_cookie(response, 'key', 'value',1) """
    
    visits = int(request.COOKIES.get('visits', '1'))
    
    if request.session.test_cookie_worked():
    # Does the cookie last_visit exist?
        if 'last_visit' in request.COOKIES:
        # Yes it does! Get the cookie's value.
            print("worj")
            last_visit = request.COOKIES['last_visit']
        # Cast the value to a Python date/time object.
            last_visit_time = datetime.datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        # If it's been more than a day since the last visit...
    
            # ...reassign the value of the cookie to +1 of what it was before...
            response.set_cookie('visits', visits+1)
            # ...and update the last visit cookie, too.
            response.set_cookie('last_visit', datetime.datetime.now())
        else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        #response = HttpResponse("last_visit")
            response.set_cookie('last_visit', datetime.datetime.now())

            print("not")
    
    response = HttpResponse()
    response = render(request,'myapp/about.html' )
    response.set_cookie(key='id', value=1)   
    #return render_to_response('myapp/about.html')
    #response=render_to_response('myapp/about.html' , {'message': message, },)
    #return response
    #return response
   # extra_context = {}
    #extra_context['course_no'] = 'This is what I want to show'
    return render(request,'myapp/about.html' , {'message': message,  },)

"""@login_required
def detail(request,course_no):        # This is your index view function
# This is your index view function
    # Access db to get list of courses. limit 10
    courselist = Course.objects.all()[:10]
            
    response = HttpResponse()        # Create empty response object
   
   # For each course, create a str to write to response
    for course in courselist:
        print(course.course_no)
        print("   ")
        print(course_no)
        if (int(course_no) == int(course.course_no)):
            courseval=course
            textbook = course.textbook
            print (course_no)
            #para = '<p>' + str(course.course_no) + '</p>' + '<p>' + str(course.title) + '</p>' +'<p>' + str(course.textbook) + '</p>'      # This is the new string
            para = ' ' + str(course.course_no) + ' ' + ' ' + str(course.title) + ' ' +' ' + str(course.textbook) + ' '      # This is the new string      
            response.write(para) # Add each str as a <p> to response obj
    
        #else:
           # raise Http404
    return render_to_response('myapp/detail.html' , {'courseval' : courseval, 'auth': auth, 'textbook' : textbook, 'user':request.user}, )
"""
"""@login_required
def topics(request):
    topiclist = Topic.objects.all()[:10]
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return render(request, 'myapp/topic.html', 
                  {'topiclist':   topiclist,  'user':request.user},)
    else:
        return HttpResponse('Please enable cookies and try again.')"""


"""@login_required   
def addtopic(request):
    
    topiclist = Topic.objects.all()
    if request.method=='POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.num_responses=1
            topic.save()
            return HttpResponseRedirect(reverse('myapp:topics'))
        
    else:
        form=TopicForm()
    
    return render(request, 'myapp/addtopic.html', {'form':form, 'topiclist':topiclist, 'user':request.user},)
    
    #return render(request, 'myapp/addtopic.html') """
 
@login_required 
def topicdetail(request, topic_id):

    topicval=Topic.objects.get(id=topic_id)
    
    if request.method=='POST':
        form=InterestForm(request.POST)
        if form.is_valid():
            # interestType=interest.save(commit=False)
            if (form.cleaned_data['interested']==1):
                topicval.num_responses=topicval.num_responses+1
                topicval.save()
          
                #interest.save()
    else:
        form=InterestForm()
        
    return render(request,'myapp/topicdetail.html' , {'form': form , 'topicval':topicval, 'user':request.user }, )
             
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(username=username, password=password) 
      
        if user:
            if user.is_active:
                login(request, user)
                courselist=Course.objects.all()[:5]
                number = random.randrange(1, 10)
                #return render(request, 'myapp/index.html', {'courselist':courselist, 'number':number})
                return HttpResponseRedirect(reverse(('myapp:index')))
                #return render(request,'myapp/about.html')
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.') 
    else:
        return render(request, 'myapp/login.html', {'user':request.user})

@login_required
def user_logout(request):
    logout(request)
    message = "This APP let you view and select courses to register in." 
    return HttpResponseRedirect(reverse(('myapp:index')))
    #return render(request,'myapp/about.html', {'message':message})
    
@login_required
def mycourses(request):
    #stu=Student.objects.filter(user=request.user)
    try:
        stu=Student.objects.get(user=request.user)
    except Student.DoesNotExist:
       message="You are not a student!"
    courselist=Course.objects.filter(student=stu)
    
    message="You are not a student!"  
    
    return render(request,'myapp/mycourses.html' , {'user':request.user, 'courselist' : courselist, 'message': message, 'stu':stu }, )




def register(request):
    message=""
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            #print("sa")
            try:
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                firstname=form.cleaned_data['firstname']
                lastname=form.cleaned_data['lastname']
                email=form.cleaned_data['email']
                user = User.objects.create_user(username, email, password)
                user.last_name = lastname
                user.first_name = firstname
                user.save()
                stu=Student(user=user)
                stu.save()                
                message="Congrats!! Successfully Registered...."
            except:
                message="Error Encounter in Registration!!"
                #interest.save()
    else:
        form=RegisterForm()
        
    return render(request,'myapp/register.html' , {'form': form , 'message': message }, )


def forgotPass(request):
    message=""
    if request.method=='POST':
        form=ForgotForm(request.POST)
        if form.is_valid():
            print("sa")
            try:
                emailForm=form.cleaned_data['email']
                u=User.objects.get(email=emailForm)
                send_mail('New Password', 'Your new Password will be same as your username', 'bhatia14@uwindsor.ca',
                          [emailForm], fail_silently=False)
                u.set_password(u.username)
                message="Password send to email!!"
            except:
                message="Not Valid User name!!"
                #interest.save()
    else:
        form=ForgotForm()
        
    return render(request,'myapp/forgotpass.html' , {'form': form , 'message': message }, )

@login_required
def uploadfile(request):
    if request.method == 'POST':
        form = ModelImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelImageUploadForm()
    return render(request, 'myapp/uploadfile.html', {'form': form})
    #return render_to_response('myapp/detail.html' , {'courseval' : courseval, 'auth': auth, 'textbook' : textbook, }, )
     

