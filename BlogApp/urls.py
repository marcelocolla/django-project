
from django.urls import path, include
from .views import home, blog

urlpatterns = [
    path('', home, name="home"),
    path('blog/<int:id>', blog, name="blog")
]
