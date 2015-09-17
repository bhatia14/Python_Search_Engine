'''
Created on May 31, 2015

@author: Rachit
'''
from django.conf.urls import patterns, url
from myapp import views, genviews
from myapp.genviews import IndexView, DetailView  
from myapp.models import Course, Topic
from myapp.views import Course
from myapp.genviews import TopicView, CreateView


urlpatterns = patterns('',
        url(r'^$', IndexView.as_view(model = Course, template_name='myapp/index.html'), name='index'), #ListView.as_view(model=Course, template_name='myapp/index.html')),
        url(r'^about$', views.about, name='about'),
        (r'^detail/(?P<course_no>\d{3})$', DetailView.as_view(model = Course, template_name='myapp/detail.html')),
        #url(r'^detail/(?P<course_no>\d{3})$', views.detail, name='detail'),
        #url(r'^topics$', views.topics, name='topics'),
        (r'^topics$', TopicView.as_view( template_name='myapp/topic.html')),
        #url(r'^addtopic$', views.addtopic, name='addtopic'),
        (r'^addtopic$', CreateView.as_view(template_name='myapp/addtopic.html')),
        url(r'^topicdetail/(?P<topic_id>\d+)$', views.topicdetail, name='topicdetail'),
        url(r'^user_logout$', views.user_logout, name='user_logout'),
        url(r'^user_login$', views.user_login, name='user_login'),
        url(r'^mycourses$', views.mycourses, name='mycourses'),
        url(r'^register$', views.register, name='register'),
        url(r'^forgotpass$', views.forgotPass, name='forgotpass'),
        url(r'^uploadfile$', views.uploadfile, name='uploadfile'),
        )
