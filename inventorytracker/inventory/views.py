from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view

from .models import Item, Location
from .forms import CreateItemForm, LocationForm


# get list of items
@api_view(["GET"])
def index(request):
    latest_items_list = Item.objects.order_by("name")
    locations = Location.objects.order_by("city_name")
    template = loader.get_template('index.html')
    context = {
        'latest_items_list': latest_items_list,
        'locations': locations
    }
    return HttpResponse(template.render(context, request))


# create new item
@api_view(["GET", "POST"])
def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            try:
                location = Location.objects.get(city_name=form.cleaned_data["your_location"])
            except Location.DoesNotExist:
                raise Http404("Item does not exist", form.cleaned_data["your_location"])
            Item(name=form.cleaned_data["your_name"], description=form.cleaned_data["your_description"],
                 count=form.cleaned_data["your_count"], location=location).save()
            locations = Location.objects.order_by("city_name")
            latest_items_list = Item.objects.order_by("name")
            template = loader.get_template('index.html')
            context = {
                'latest_items_list': latest_items_list,
                'locations': locations
            }

            return HttpResponseRedirect("/", template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateItemForm()

    return render(request, "create.html", {'form': form})


# update or delete items
@api_view(["GET", "PUT", "POST"])
def detail(request, item_id):
    # if POST request, we need to process data
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # same item form is okay because its the same data
        form = CreateItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            try:
                location = Location.objects.get(city_name=form.cleaned_data["your_location"])
            except Location.DoesNotExist:
                raise Http404("Item does not exist", form.cleaned_data["your_location"])
            Item.objects.filter(pk=item_id).update(name=form.cleaned_data["your_name"], description=form.cleaned_data\
                ["your_description"], count=form.cleaned_data["your_count"], location=location)

            locations = Location.objects.order_by("city_name")
            latest_items_list = Item.objects.order_by("name")
            template = loader.get_template('index.html')
            context = {
                'latest_items_list': latest_items_list,
                'locations': locations
            }

            return HttpResponseRedirect("/", template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateItemForm(initial={'your_name': item.name, 'your_description': item.description, 'your_count':
            item.count, 'your_location': item.location.city_name})

    return render(request, "detail.html", {'form': form, 'item_id': item_id})


# delete an item
@api_view(["GET", "POST"])
def delete_item(request, item_id):
    Item.objects.get(pk=item_id).delete()  # now that we've deleted, return to index page essentially

    latest_items_list = Item.objects.order_by("name")
    locations = Location.objects.order_by("city_name")
    template = loader.get_template('index.html')
    context = {
        'latest_items_list': latest_items_list,
        'locations': locations
    }
    return HttpResponseRedirect("/", template.render(context, request))


# delete a location
@api_view(["GET", "POST"])
def delete_location(request, location_id):
    Location.objects.get(pk=location_id).delete()  # now that we've deleted, return to index page essentially

    latest_items_list = Item.objects.order_by("name")
    locations = Location.objects.order_by("city_name")
    template = loader.get_template('index.html')
    context = {
        'latest_items_list': latest_items_list,
        'locations': locations
    }
    return HttpResponseRedirect("/locations", template.render(context, request))


# add new location or modify existing ones
@api_view(["GET", "POST"])
def modify_locations(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LocationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            Location(city_name=form.cleaned_data["your_city_name"]).save()
            locations = Location.objects.order_by("city_name")
            latest_items_list = Item.objects.order_by("name")
            template = loader.get_template('index.html')
            context = {
                'latest_items_list': latest_items_list,
                'locations': locations
            }

            return HttpResponseRedirect("/locations/", template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LocationForm()
        locations = Location.objects.order_by("city_name")
        print(locations)

    return render(request, "locations.html", {'form': form, 'locations': locations})