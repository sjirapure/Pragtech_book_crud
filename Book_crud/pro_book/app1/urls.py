from django.urls import path
from . import views
urlpatterns =[
    path('av/',views.AddBook.as_view(),name='add_url'),
    path('sv/',views.ShowBook.as_view(),name='show_url'),
    path('uv/<int:id>/',views.UpdateBook.as_view(),name='update_url')
]