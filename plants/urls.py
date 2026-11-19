from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("new/", views.add_plant_view, name="add_plant_view"),
    path("all/", views.all_plants_view, name="all_plants_view"),
    path("<int:plant_id>/detail/", views.plant_detail_view, name="plant_detail_view"),
]