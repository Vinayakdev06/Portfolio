from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "Login to Burhan"
admin.site.site_title = "Welocom to DashBord"
admin.site.index_title = "Welocom to Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('project', views.project, name='project'),
    path('#contact', views.contact, name='contact'),
    # path('skills', views.skills, name='skills'),
    # path('contact', views.contact, name='contact'),
]
