from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.get_index, name='index'),
    path('login/', views.get_login, name='login'),
    path('signup/', views.get_signup, name='signup'),
    path('logout/', views.get_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('event/add/', views.add_edit_event, name='event'),
    path('event/edit/<int:event_id>/', views.add_edit_event, name='event'),
    path('event/detail/<int:event_id>/', views.eventdetail, name='eventdetail'),
    path('event/end/<int:event_id>/', views.endevent, name='endevent'),
    path('event/delete/<int:event_id>/', views.deleteevent, name='deleteevent'),
    path('event/<int:event_id>/buy/', views.buyticket, name='buyticket'),
    path('your-tickets/', views.yourtickets, name='yourtickets'),
    path('eventlist/', views.evenlist, name='eventlist'),
    path('introduction/', views.introduction, name='introduction'),
    path('search/', views.search_events, name='search_events'),
    path('event-management/', views.eventmanagement, name='eventmanagement'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)