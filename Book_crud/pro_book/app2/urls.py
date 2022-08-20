from django.urls import path
from . import views
urlpatterns=[
    path('in/',views.LoginUser.as_view(),name='login_url'),
    path('reg/',views.RegisterUser.as_view(),name='register_url'),
    path('out/',views.LogoutUser.as_view(),name='logout_url')
]