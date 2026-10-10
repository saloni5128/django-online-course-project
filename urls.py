from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # ... your other path statements (like course list, details, etc.) ...
    
    # Path for submitting exam answers
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    
    # Path for showing exam results
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='exam_result'),
]
