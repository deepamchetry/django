from django.urls import path
from . import views

urlpatterns = [
    path("project/",views.project,name='project'),
    path("projects/<str:pk>/",views.projects,name='projects'),
]