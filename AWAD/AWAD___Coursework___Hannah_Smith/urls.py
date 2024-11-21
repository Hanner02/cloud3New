"""
Definition of urls for AWAD___Coursework.
"""

from django.urls import path, include
from django.contrib import admin
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter
from app.views import set_cookie, show_template
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
    path('api/',include('api.urls')),
    path('set_cookie/',views.set_cookie,name='set_cookie'),
    path('show_template/',views.show_template, name='show_template'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('',views.login_view, name="login"),
    path('home/',views.home, name="home"),
    path('search/',views.search, name="search_films"),
    path('add/',views.addMessage, name="add"),
    path('reviewlist/',views.showMessages, name="reviewlist"),
    path('login/',views.login_view, name="login"),
    path('signup/',views.signup_view, name="signup"),
    path('filmreviews/<int:film_id>/', views.film_reviews, name='film_reviews'),
    
    path('log/', views.addMessage, name="log"),
    path('show/', views.showMessages, name="show"),
    path('search/<str:q>/', views.searchAjax, name="search"),
    
    path('edit/<int:pk>/', views.editMessage, name='edit'),
    path('delete/<int:pk>/', views.deleteMessage, name='delete'),
    path('sort/', views.sortReviews, name='sort'),
    
    path('filmreviews/<int:film_id>/', views.film_reviews, name='film_reviews'),
    path('watchlist/add/<int:film_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/remove/<int:film_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('mywatchlist/', views.view_watchlist, name='view_watchlist'),
]


urlpatterns += staticfiles_urlpatterns()



