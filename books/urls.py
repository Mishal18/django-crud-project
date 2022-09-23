from django.urls import path
from books.views import index, details, create, update, delete

app_name = 'books'

urlpatterns = [
    path('',index, name='index'),
    path('create/',create, name='create'),
    path('<int:id>/',details, name='details'),
    path('<int:id>/delete/',delete, name='delete'),
    path('<int:id>/update/',update, name='update'),
]
