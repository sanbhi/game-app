from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
]


from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
]
