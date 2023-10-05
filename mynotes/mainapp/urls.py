from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name='home'),
    path('home', views.home, name="home"),
    path('reg', views.reg, name="reg"),
    path('reg/', views.reg, name="reg"),
    path('login', views.login_page, name='login'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('logout/', views.logout_page, name='logout'),
    # path('notes', views.notes, name='notes'),
    # path('notes/', views.notes, name='notes'),
    path('add_note', views.add_note, name='add_note'),
    path('add_note/', views.add_note, name='add_note'),

]
