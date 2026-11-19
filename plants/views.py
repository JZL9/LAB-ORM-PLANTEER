from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Plant


def add_plant_view(request: HttpRequest):
    if request.method == "POST":
        if "image" not in request.FILES:
            return render(request, "plants/add_plant.html", {
                "categories": Plant.Category.choices,
                "error": "Please upload an image of the plant.",
            })

        category = request.POST.get("category", "")
        if category not in Plant.Category.values:
            category = Plant.Category.TREE

        plant = Plant(
            name=request.POST["name"].strip(),
            about=request.POST["about"].strip(),
            used_for=request.POST["used_for"].strip(),
            category=category,
            is_edible="is_edible" in request.POST,
            image=request.FILES["image"],
        )
        plant.save()
        return redirect("main:home_view")

    return render(request, "plants/add_plant.html", {"categories": Plant.Category.choices})

def all_plants_view(request: HttpRequest):
    plants = Plant.objects.all()

    category = request.GET.get("category", "")
    edible = request.GET.get("edible", "")

    if category in Plant.Category.values:
        plants = plants.filter(category=category)

    if edible == "yes":
        plants = plants.filter(is_edible=True)
    elif edible == "no":
        plants = plants.filter(is_edible=False)

    plants = plants.order_by("-created_at")

    return render(request, "plants/all_plants.html", {
        "plants": plants,
        "total": plants.count(),
        "categories": Plant.Category.choices,
        "category": category,
        "edible": edible,
    })

def plant_detail_view(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, pk=plant_id)

    related_plants = (
        Plant.objects.filter(category=plant.category)
        .exclude(pk=plant.pk)
        .order_by("-created_at")[:3]
    )

    return render(request, "plants/plant_detail.html", {
        "plant": plant,
        "related_plants": related_plants,
    })