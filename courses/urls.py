from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.course_details, name='course_details'),
    path('<int:course_id>/submit/', views.submit_exam, name='submit_exam'),
    path('result/<int:submission_id>/', views.exam_result, name='exam_result'),
]
