from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('short',views.short),
    path('<str:pk>', views.go, name='go')
]