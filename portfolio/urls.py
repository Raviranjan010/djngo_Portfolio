from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('project/<slug:slug>/', views.project_detail_view, name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
]
