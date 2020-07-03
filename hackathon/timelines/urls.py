from django.urls import path

from timelines import views

urlpatterns = {
    path('', views.index, name='index'),
    path('companys/search/', views.search, name='search'),
    path(
        'timelines/<int:company_id>/<int:release_id>/',
        views.timeline, name='timeline'
    ),
    path(
        'timelines/<int:company_id>/<int:release_id>/more/<int:year>',
        views.more, name='more'
    )
}
