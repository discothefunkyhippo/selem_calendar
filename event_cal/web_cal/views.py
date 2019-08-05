# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
from django.shortcuts import render
from .models import Event
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone

from pytz import timezone as tz
import datetime

# Create your views here.

# def update_db(request):
    
#     event_name = settings.EVENT_NAME
#     event_list = Event.objects.all()
#     td = datetime.timedelta(hours=1)
#     for event in event_list:
#         event.event_datetime = event.event_datetime - td
#         event.save()


#     html = "<html><body>DB UPDATED</body></html>"
#     return HttpResponse(html)

def all(request):
    event_name = settings.EVENT_NAME
    date_format = '%A, %B %d %Y'
    event_list = Event.objects.all().order_by('event_datetime')
    event_dict = OrderedDict()
    for event in event_list:
        localized_event_datetime = event.event_datetime.astimezone(tz('US/Eastern'))
        # current_event_date = event.event_datetime.date().strftime(date_format)
        current_event_date = localized_event_datetime.date()
        if not event_dict.get(current_event_date, None):
            event_dict[current_event_date] = [event]
        else:
            event_dict[current_event_date].append(event)
    context = {
        'event_name': event_name,
        'event_dict': event_dict,
    }
    return render(request, 'web_cal/all.html', context)


def presentations(request):
    event_name = settings.EVENT_NAME
    date_format = '%A, %B %d %Y'
    event_list = Event.objects.filter(event_type__in=['presentation', 'general']).order_by('event_datetime')
    event_dict = OrderedDict()
    for event in event_list:
        localized_event_datetime = event.event_datetime.astimezone(tz('US/Eastern'))
        # current_event_date = event.event_datetime.date().strftime(date_format)
        current_event_date = localized_event_datetime.date()
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
    event_list = Event.objects.filter(event_type__in=['laser show', 'general']).order_by('event_datetime')
    event_dict = OrderedDict()
    for event in event_list:
        localized_event_datetime = event.event_datetime.astimezone(tz('US/Eastern'))
        # current_event_date = event.event_datetime.date().strftime(date_format)
        current_event_date = localized_event_datetime.date()
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
        localized_event_datetime = event.event_datetime.astimezone(tz('US/Eastern'))
        # current_event_date = event.event_datetime.date().strftime(date_format)
        current_event_date = localized_event_datetime.date()
        if not event_dict.get(current_event_date, None):
            event_dict[current_event_date] = [event]
        else:
            event_dict[current_event_date].append(event)
    context = {
        'event_name': event_name,
        'event_dict': event_dict,
    }
    return render(request, 'web_cal/djsets.html', context)
