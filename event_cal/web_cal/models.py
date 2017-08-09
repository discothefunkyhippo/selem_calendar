# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

EVENT_TYPE_CHOICES = (
        ('presentation', 'PRESENTATION'),
        ('laser show', 'LASER SHOW'),
        ('dj set', 'DJ SET'),
)

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_datetime = models.DateTimeField('event time')
    event_location = models.CharField(max_length=200)
    event_presenter = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default='presentation')

    def __str__(self):
        return self.event_name

    def has_already_occurred(self):
        return self.event_datetime < timezone.now()
