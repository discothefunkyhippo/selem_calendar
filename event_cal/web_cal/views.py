# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
from django.shortcuts import render
from .models import Event
from django.conf import settings
# Create your views here.

from django.http import HttpResponse

def presentations(request):
    event_name = settings.EVENT_NAME
    date_format = '%A, %B %d %Y'
    event_list = Event.objects.filter(event_type__exact='presentation').order_by('event_datetime')
    event_dict = OrderedDict()
    for event in event_list:
        current_event_date = event.event_datetime.date().strftime(date_format)
        if not event_dict.get(current_event_date, None):
            event_dict[current_event_date] = [event]
        else:
            event_dict[current_event_date].append(event)
    context = {
        'event_name': event_name,
        'event_dict': event_dict,
    }
    return render(request, 'web_cal/presentations.html', context)

def laser_shows(request):
    event_name = settings.EVENT_NAME
    date_format = '%A, %B %d %Y'
    event_list = Event.objects.filter(event_type__exact='laser show').order_by('event_datetime')
    event_dict = OrderedDict()
    for event in event_list:
        current_event_date = event.event_datetime.date().strftime(date_format)
        if not event_dict.get(current_event_date, None):
            event_dict[current_event_date] = [event]
        else:
            event_dict[current_event_date].append(event)
    context = {
        'event_name': event_name,
        'event_dict': event_dict,
    }
    return render(request, 'web_cal/lasershows.html', context)

def dj_sets(request):
    event_name = settings.EVENT_NAME
    date_format = '%A, %B %d %Y'
    event_list = Event.objects.filter(event_type__exact='dj set').order_by('event_datetime')
    event_dict = OrderedDict()
    for event in event_list:
        current_event_date = event.event_datetime.date().strftime(date_format)
        if not event_dict.get(current_event_date, None):
            event_dict[current_event_date] = [event]
        else:
            event_dict[current_event_date].append(event)
    context = {
        'event_name': event_name,
        'event_dict': event_dict,
    }
    return render(request, 'web_cal/djsets.html', context)
