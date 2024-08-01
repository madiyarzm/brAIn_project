from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('attend/', views.attend, name="attend"),
    path('join_us/', views.join_us, name="join_us"),
    path('resources/', views.resources, name="resources"),
    path('sponsorship/', views.sponsorship, name="sponsorship"),
    path('linkedIn/', views.linkedIn, name="linkedIn"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create_post/', views.create_post, name="create_post"),
    path('resources/', views.resources, name="resources"),
    path('resources/<slug:slug>/', views.resource_view, name="resource_view"),
    path('edit_post/<slug:slug>/', views.edit_post, name="edit_post"),
    path('delete_post/<slug:slug>/', views.delete_post, name="delete_post")
]