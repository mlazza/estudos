from django.contrib import admin
from django.urls import path
from livros.views import livros_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', livros_view)
]
