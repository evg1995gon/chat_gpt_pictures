from django.urls import path
from .views import picture_view, picture_view_list, picture_detail

app_name = 'pictures'

urlpatterns = [
    path('', view=picture_view, name='index'),
    path('list/', view=picture_view_list, name='list'),
    path('detail/<int:id>/', view=picture_detail, name='detail'),
]
