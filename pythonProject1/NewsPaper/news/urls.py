from django.urls import path
from .views import NewsList, NewsDetail, Search, NewsCreate, NewsDelete, NewsEdit

urlpatterns = [
   path('', NewsList.as_view(), name='news'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('search/', Search.as_view(), name='search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete')
]