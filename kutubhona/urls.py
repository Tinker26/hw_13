from django.urls import path
from .views import *

urlpatterns = [
    path('kitob/', KitobListView.as_view()),
    path('kitob/<int:pk>', KitobDetailView.as_view()),
    path('muallif/', MuallifListView.as_view()),
    path('muallif/<int:pk>', MuallifDetailView.as_view())
]