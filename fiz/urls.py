from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('cb-view/<shortcode>/', views.FizCBV.as_view(), name='cbv'),
]