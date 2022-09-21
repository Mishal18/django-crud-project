from django.urls import path
from books.views import index, details, create, update, delete

urlpatterns = [
    path('',index),
    path('create/',create),
    path('<int:id>/',details),
    path('<int:id>/delete/',delete),
    path('<int:id>/update/',update),
]
