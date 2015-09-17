from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Author(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, default="")
    birthdate=models.DateField()
    country=models.CharField(max_length=20, default='Canada')
    
    def __str__(self):
        return "(%s, %s, %s, %s)" % (self.firstname, str(self.lastname),str(self.birthdate), str(self.country))



    
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.ManyToManyField(Author)
    numpages=models.IntegerField(null=True, blank=True)
    is_stock=models.BooleanField(True)
    pubyear=models.DateField(null=True)
    def __str__(self):
        #return self.title
        return "(%s, %s, %s, %s)" % (self.title, str(self.author),str(self.numpages), str(self.is_stock))

class Student(models.Model):
    user=models.OneToOneField(User, primary_key=True)
    student_id = models.IntegerField(null=True,blank=True) 
    UNDERGRAD = 1
    MSC = 2
    PHD = 3
    LEVEL_CHOICES = (
        (UNDERGRAD, 'Undergrad'),
        (MSC, 'Masters'),
        (PHD, 'PhD')
    )
    level = models.IntegerField(default=UNDERGRAD, choices=LEVEL_CHOICES)
    
    def list_of_courses(self):
        return [course.title for course in Course.objects.all()]
   # def courselist(user):
        
        
    def __str__(self):
        name=self.user.first_name+' '+self.user.last_name
        return "(%s)" % (name)

class Instructor(models.Model):
    user=models.OneToOneField(User, primary_key=True)
    webpage=models.URLField(default="");
    office=models.CharField(max_length=100, default='EH 120')
    def __str__(self):
        name=self.user.first_name+' '+self.user.last_name
        return "(%s)" % (name)

    
class Course(models.Model):
    course_no=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    textbook=models.ForeignKey(Book)
    instructor=models.ForeignKey(Instructor, null=True)
    student=models.ManyToManyField(Student)
    def __str__(self):
        return "(%s, %s, %s)" % (self.title, str(self.course_no),str(self.textbook))

class Topic(models.Model):
    subject = models.CharField(max_length=100, unique=True)   
    intro_course = models.BooleanField(default=True)
    NO_PREFERENCE = 0
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3
    TIME_CHOICES = (
        (0, 'No preference'),
        (1, 'Morning'),
        (2, 'Afternoon'),
        (3, 'Evening')
    )
    time = models.IntegerField(default=0, choices=TIME_CHOICES)
    num_responses = models.IntegerField(default=0)
    avg_age =models.IntegerField(default=20)
    def __str__(self):
        return "(%s, %s, %s)" % (self.subject, str(self.intro_course),str(self.avg_age))
    
    
class ModelImageUpload(models.Model):
    name=models.ForeignKey(Instructor, null=True)
    image=models.ImageField(upload_to='userimage')
   