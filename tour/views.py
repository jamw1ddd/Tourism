from django.shortcuts import render,get_object_or_404
from .models import Region, City, Place
from .forms import ContactForm

def index(request):
    regions = Region.objects.all()
    cities = City.objects.all()
    places = Place.objects.all()[:6]
    return render(request, 'index.html', {'regions': regions, 'cities': cities, 'places': places})


def contact(request):
    regions = Region.objects.all()
    cities = City.objects.all()
    success_message = None  # Initializing variable for success message

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz."  # Success message
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'regions': regions,
        'cities': cities,
        'success_message': success_message,  # Passing success message to template
    })

def region_detail(request, pk):
    region = get_object_or_404(Region, pk=pk)
    regions = Region.objects.all()
    cities = City.objects.all()
    return render(request, 'region_detail.html', {'region': region, 'regions': regions, 'cities': cities})

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    cities = City.objects.all()
    regions = Region.objects.all()
    return render(request, 'city_detail.html', {'city': city, 'cities': cities, 'regions': regions})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    places = Place.objects.all()
    regions = Region.objects.all()
    cities = City.objects.all()
    return render(request, 'place_detail.html', {'place': place, 'places': places, 'regions': regions, 'cities': cities})

def place_list(request):
    places = Place.objects.all()
    regions = Region.objects.all()
    cities = City.objects.all()
    return render(request, 'place.html', {'places': places, 'regions': regions, 'cities': cities})
