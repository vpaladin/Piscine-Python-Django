from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ex00.urls'), name='ex00'),
    path('ex00/', include('ex00.urls'), name='ex00'),
    path('ex01/', include('ex01.urls'), name='ex01'),
    path('ex02/', include('ex02.urls'), name='ex02'),
    path('ex03/', include('ex03.urls'), name='ex03'),
    path('ex04/', include('ex04.urls'), name='ex04'),
    path('ex05/', include('ex05.urls'), name='ex05'),
    path('ex06/', include('ex06.urls'), name='ex06'),
    path('ex07/', include('ex07.urls'), name='ex07'),
    path('ex08/', include('ex08.urls'), name='ex08'),
    path('ex09/', include('ex09.urls'), name='ex09'),
    path('ex10/', include('ex10.urls'), name='ex10'),
]
