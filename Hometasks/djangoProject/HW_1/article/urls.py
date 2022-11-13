from django.urls import path
from .views import PostCreateView, index, PostUpdateView, PostDeleteView

app_name = 'article'

urlpatterns = [
    path('', index, name='list'),
    path('create/', PostCreateView.as_view()),
    path('update/<int:pk>', PostUpdateView.as_view()),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
]
