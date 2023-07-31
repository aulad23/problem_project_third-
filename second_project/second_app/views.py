from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def courses(request):
   return HttpResponse('''
                        <h1>this a courses page</h1>
                      <a href = '/second_app/feedback/'>feedback</a>
                      <a href = '/first_app/about/'>about</a>
                      <a href = '/first_app/contact/'>contact</a>
                        
                        ''')
def feedback(request):
   return HttpResponse('''
                        <h1>this a feedback page</h1>
                        <a href = '/second_app/courses/'>courses</a>
                        <a href = '/first_app/about/'>about</a>
                        <a href = '/first_app/contact/'>contact</a>
                        
                        ''')



