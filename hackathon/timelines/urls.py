from django.urls import path

from timelines import views

urlpatterns = {
    path('companys/search/', views.search, name='search'),
    path('timelines/', views.timeline, name='timeline')
}
