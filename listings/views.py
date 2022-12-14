from django.shortcuts import render, get_object_or_404

from .choices import state_choices, bedroom_choices, price_choices
from .models import Listing
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
    }
    return render (request, 'listings/listings.html',context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id )
    context ={
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords

    if 'keywords' in request.Get:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # city

    if 'city' in request.Get:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__exact=city)

    # state

    if 'state' in request.Get:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__exact=state)

    # Bedroom

    if 'bedrooms' in request.Get:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)  # lte means one or two bedrooms


    # price

    if 'price' in request.Get:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context ={
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings': queryset_list,
        'values': request.Get,
    }
    return render(request, 'listings/search.html', context)
















