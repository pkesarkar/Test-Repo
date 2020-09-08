from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', views.first_view ), # here URl will be http://localhost:8000/testapp/first/
    path('second/', views.second_view ),
    path('third/', views.third_view )
]
