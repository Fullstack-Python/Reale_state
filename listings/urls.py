from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index, name="listings"),
    path ('<int:listing_id>/listing',views.listing, name="listing"),
    path('', views.search, name="search"),
]