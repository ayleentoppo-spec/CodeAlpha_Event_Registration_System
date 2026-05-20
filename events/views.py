from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from .forms import RegistrationForm

def event_list(request):
    return render(request, 'events/event_list.html', {'events': Event.objects.all().order_by('date')})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        reg = form.save(commit=False)
        reg.event = event
        reg.save()
        return redirect('my_registrations')
    return render(request, 'events/event_detail.html', {'event': event, 'form': form})

def my_registrations(request):
    regs = Registration.objects.all().order_by('-created_at')
    return render(request, 'events/my_registrations.html', {'registrations': regs})

def cancel_registration(request, pk):
    Registration.objects.filter(pk=pk).delete()
    return redirect('my_registrations')
