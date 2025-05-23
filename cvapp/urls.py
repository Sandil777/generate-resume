from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('select-template/', views.SelectTemplate.as_view(), name="select_template"),
    path('resumeTemplate/', views.Accept.as_view(), name='accept'),
    path('list/', views.list, name="list"),
    path('list/<int:id>/', views.UserDetail, name="viewing"),
    path('resume/<int:template_id>/', views.resume, name="resume"),
    path('update/<int:id>/', views.update_form, name="update"),
    path('delete/<int:id>/', views.delete_form, name="deleteform"),
    path('prediction/', views.predict, name="predict"),
]