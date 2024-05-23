from django.urls import path
from .import views
urlpatterns=[
    # path('',views.index),
    path('createprofile/',views.createprofile,name='createprofile'),
    path('createportfolio/',views.createportfolio,name='createportfolio'),
    path('createproject/',views.createproject,name='createproject'),
    path('updateprofile/<int:profileid>/',views.updateprofile,name='updateprofile'),
    path('updateportfolio/<int:portfolioid>/',views.updateportfolio,name='updateportfolio'),
    path('updateproject/<int:projectid>/',views.updateproject,name='updateproject'),
    path('detailprofile/<int:profileid>/',views.detailsprofile,name='detailprofile'),
     path('detailproject/<int:projectid>/',views.detailsproject,name='detailproject'),
     path('detailportfolio/<int:portfolioid>/',views.detailsportfolio,name='detailportfolio'),
    path('deleteprofile/<int:profileid>/',views.deleteprofile,name='deleteprofile'),
    path('deleteproject/<int:projectid>/', views.deleteproject, name='deleteproject'),
    path('deleteportfolio/<int:portfolioid>/', views.deleteportfolio, name='deleteportfolio'),
    path('listprofile/',views.listprofile,name='listprofile'),
    path('listportfolio/', views.listportfolio, name='listprofile'),
    path('listproject/', views.listproject, name='listproject'),
    path('search/',views.search,name='search'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
]