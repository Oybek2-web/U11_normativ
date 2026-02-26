from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('list/', views.book_list, name="book_list"),
    path('create/', views.book_create, name="book_create"),
    path('delete/<int:id>/', views.book_delete, name="book_delete"),
    path('update/<int:id>/', views.book_update, name="book_update")
]