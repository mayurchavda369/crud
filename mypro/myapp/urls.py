
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adddata/',views.adddata,name='adddata'),
    path('showdata/',views.showdata,name='showdata'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    

]