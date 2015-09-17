'''
Created on Jun 23, 2015

@author: Rachit
'''
from django.views import generic
from myapp.models import Course, Book, Author,Topic, Student
from django.shortcuts import get_object_or_404, render, render_to_response
import random
from django.http.response import HttpResponse, HttpResponseRedirect

from myapp.forms import TopicForm, InterestForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from random import randint
from datetime import *
import datetime


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)



class IndexView(generic.ListView):
   # model = Course  # Use when not using get_queryset()
    #courselist=Course.
    template_name = 'myapp/index.html'
    context_object_name = 'courselist'

    def get_queryset(self):
        return Course.objects.all()[:5]
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        index_visits = int(self.request.COOKIES.get('index_visits', '0'))
        context['index_visits'] = index_visits+1
        #luckynum count
        if not 'luckynum' in self.request.session or not self.request.session['luckynum']:
            self.request.session['luckynum'] =  random.randrange(1, 10)
        else:
            pass
        
        context['number'] = self.request.session['luckynum'] #random.randrange(1, 10)
        return context
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        
            
        # count the index visits
        index_visits = int(request.COOKIES.get('index_visits', '0'))
        response=self.render_to_response(self.get_context_data())
        if 'index_last_visit' in request.COOKIES:
            last_visit = request.COOKIES['index_last_visit']
            last_visit_time = datetime.datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
            if (datetime.datetime.now() - last_visit_time).seconds > 0:
                response.set_cookie('index_visits', index_visits+1)
                response.set_cookie('index_last_visit', datetime.datetime.now())
        else:
            response.set_cookie('index_visits', index_visits+1)
            response.set_cookie('index_last_visit', datetime.datetime.now())
            
        return response

  
class TopicView(View):
    template_name = 'myapp/topic.html'
    
    def get(self, request):
        topiclist = Topic.objects.all()[:10]
        if request.session.test_cookie_worked():
            print("Hi")
            request.session.delete_test_cookie()
            return render(request, self.template_name, 
                  {'topiclist':   topiclist,  'user':request.user},)
        
        else:
            return HttpResponse('Please enable cookies and try again.')


class CreateView(LoginRequiredMixin, View):
    template_name = 'myapp/addtopic.html'
    form_class = TopicForm
    
    
    
    def get(self, request):
        form = self.form_class()
        topiclist = Topic.objects.all()
        return render(request, self.template_name, {'form': form, 'topiclist': topiclist})
    
    def post(self, request):
        topiclist = Topic.objects.all()
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            topic = form.save(commit=False)
            topic.num_responses=1
            topic.save()
            #return HttpResponseRedirect(reverse('myapp:topics'))
        
        else:
            form=TopicForm()
       # return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form':form, 'topiclist':topiclist, 'user':request.user},)
    
class DetailView(LoginRequiredMixin, generic.DetailView):
    model=Course
    template_name='myapp/detail.html'
    context_object_name= 'courseval'
    
    def get_object(self):
        course_no = self.kwargs.get('course_no', None);
        return get_object_or_404(Course, course_no=course_no)
    
   
    
"""class DetailView (generic.ListView):

    template_name = 'myapp/detail.html'
    def detail(self, request,course_no):        # This is your index view function
    # This is your index view function
    # Access db to get list of courses. limit 10
        courselist = Course.objects.all()[:10]
            
        response = HttpResponse()        # Create empty response object
        print("hello")
        # For each course, create a str to write to response
        for course in courselist:
            print(course.course_no)
            if (int(course_no) == int(course.course_no)):
                courseval=course
                textbook = course.textbook
                print (course_no)
                #para = '<p>' + str(course.course_no) + '</p>' + '<p>' + str(course.title) + '</p>' +'<p>' + str(course.textbook) + '</p>'      # This is the new string
                para = ' ' + str(course.course_no) + ' ' + ' ' + str(course.title) + ' ' +' ' + str(course.textbook) + ' '      # This is the new string      
                response.write(para) # Add each str as a <p> to response obj
            #else:
               # raise Http404
        return render_to_response('myapp/detail.html' , {'courseval' : courseval, 'textbook' : textbook, }, )
        
    # def get_object(self,course_no):
        
    
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        print(kwargs)
        print(context)
        context['number'] = random.randrange(1, 10)
        return context"""