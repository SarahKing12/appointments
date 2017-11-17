# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..main.models import User

class Appointment(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, related_name="appointments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Appointment object: {} {} {} {}>".format(self.task, self.status, self.date, self.time)