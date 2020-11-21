from django.urls import path
from . import views
# importato la funzione url di Django e tutte
#  le nostre views dalla applicazione blog 


#modello di URL
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]