from .models import Event, Location
from django.shortcuts import redirect, render
from .forms import LocationForm, EventForm
from django.http import HttpResponseRedirect


def all_events(request):

    events = Event.objects.all().order_by('-event_date')

    context = {

        'events': events,
    }

    return render(request, 'events/events.html', context)


def event_details(request, pk):

    event = Event.objects.get(pk=pk)

    context = {

        'event': event,
    }

    return render(request, 'events/event_details.html', context)


def add_location(request):

    submitted = False

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/locations/?submitted=True')
    else:
        form = LocationForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'events/add_location.html', context)


def location_list(request):

    locations = Location.objects.all()

    context = {
        'locations': locations,
    }

    return render(request, 'events/locations.html', context)


def location_details(request, pk):

    location = Location.objects.get(pk=pk)

    context = {
        'location': location,

    }

    return render(request, 'events/location_details.html', context)


def search_locations(request):

    if request.method == "POST":

        searched = request.POST['searched']

        locations = Location.objects.filter(name__contains=searched)

        context = {
            'searched': searched,
            'locations': locations,
        }

        return render(request, 'events/search_locations.html', context)
    else:

        context = {

        }

        return render(request, 'events/search_locations.html', context)


def update_location(request, pk):

    location = Location.objects.get(pk=pk)

    form = LocationForm(request.POST or None, instance=location)

    if form.is_valid():
        form.save()
        return redirect('/locations')

    context = {
        'location': location,
        'form': form,
    }

    return render(request, 'events/update_location.html', context)


def add_event(request):

    submitted = False

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'events/add_event.html', context)


def update_event(request, pk):

    event = Event.objects.get(pk=pk)
    form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect('/events')

    context = {
        'event': event,
        'form': form,
    }

    return render(request, 'events/update_event.html', context)


def delete_event(request, pk):

    event = Event.objects.get(pk=pk)
    event.delete()

    return redirect('/events')


def delete_location(request, pk):

    location = Location.objects.get(pk=pk)
    location.delete()

    return redirect('/locations')
