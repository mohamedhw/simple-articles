from django.urls import path
from .views import articel_list, articel_detail, articel_create

app_name='articles'

urlpatterns = [
    path('', articel_list, name='list'),
    path('<int:id>/', articel_detail, name='detail'),
    path('create/', articel_create, name='create'),
]