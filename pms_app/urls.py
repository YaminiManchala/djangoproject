from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home_redirect, name='home_redirect'),
    path('student/register/', views.student_register, name='student_register'),
    path('student/login/', views.student_login, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('search/jobs/', views.student_search_jobs, name='student_search_jobs'),
    path('apply/job/<int:job_id>/', views.apply_job, name='apply_job'),
    path('applications/', views.student_application_status, name='student_application_status'),
    path('applied_jobs/', views.applied_jobs, name='applied_jobs'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/logout/', views.student_logout, name='student_logout'),
    #========company urls============
    path('company/register/', views.company_register, name='company_register'),
    path('company/login/', views.company_login, name='company_login'),
    path('company/dashboard/', views.company_dashboard, name='company_dashboard'),
    path('company/post-job/', views.post_job, name='post_job'),
    path('company/applicants/<int:job_id>/', views.view_applicants, name='view_applicants'),
    path('company/logout/', views.company_logout, name='company_logout'),
    path('update-application-status/<int:application_id>/', views.update_application_status, name='update_application_status'),
    path('confirm-application/<int:id>/', views.confirm_application, name='confirm_application'),
    path('reject-application/<int:id>/', views.reject_application, name='reject_application'),
]