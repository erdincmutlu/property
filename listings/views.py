from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Listing


def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 6)
    page_number = request.GET.get("page")
    paged_listings = paginator.get_page(page_number)
    context = {"listings": paged_listings}
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    return render(request, "listings/listing.html")


def search(request):
    return render(request, "listings/search.html")
