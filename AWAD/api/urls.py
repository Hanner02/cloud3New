from django.urls import path
from django.contrib import admin
from api.views import ReviewList,ReviewDetail


urlpatterns = [
  path('items/',ReviewList.as_view(), name='review-list'),
  path('items/<int:pk>/',ReviewDetail.as_view(), name='review-detail'),
  path('admin/', admin.site.urls),
]