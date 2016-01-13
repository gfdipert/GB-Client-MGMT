from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.conf import settings
from datetime import datetime 
from datetime import timedelta
from datetime import time


class Client(models.Model):
    """Create CLIENT object with status, date, and guide attributes"""
    GSTATUS = (
        (0,'New - Guide Not Built'),
        (1,'Guidebuilding'),
        (2,'Guidebuild Sufficient for Submission'),
        (3,'Complete'),
    )
    PROSTATUS = (
        (0,'Pro'),
        (1,'DIY'),
    )
    APPTYPE = (
        (0, 'GB Premium'),
        (1, 'Standalone'),
        (2, 'Multiguide'),
    )
    APPSTATUS = (
        (0,'Pending Assets'),
        (1,'Mockups Sent'),
        (2,'Screenshots Sent'),
        (3,'Apple Submitted'),
        (4,'Apple Published'),
    )
    PSTATUS = (
        (0,'Not Submitted'),
        (1,'Submitted'),
        (2,'Play Published'),
    )
    BSTATUS = (
        (0,'Not Submitted'),
        (1,'Submitted'),
        (2,'Blackberry Published'),
    )
    ASTATUS = (
        (0,'Not Submitted'),
        (1,'Submitted'),
        (2,'Amazon Published'),
    )
    name = models.CharField(max_length=45, unique=True, verbose_name=_('Name'))
    apptype = models.IntegerField(choices=APPTYPE, default=0, verbose_name=_('App Type'))
    prostatus = models.IntegerField(choices=PROSTATUS, default=0, verbose_name=_('Guidebuilding Service'))
    gstatus = models.IntegerField(choices=GSTATUS, default=0, verbose_name=_('Guidebuilding Status'))
    appstatus = models.IntegerField(choices=APPSTATUS, default=0, verbose_name=_('Apple Submission Status'))
    pstatus = models.IntegerField(choices=PSTATUS, default=0, verbose_name=_('Google Play Status'))
    bstatus = models.IntegerField(choices=BSTATUS, default=0, verbose_name=_('Blackberry Status'))
    astatus = models.IntegerField(choices=ASTATUS, default=0, verbose_name=_('Amazon Status'))
    intro = models.DateField(null=True, blank=True, verbose_name=_('Intro Email Sent'))
    appsub = models.DateField(null=True, blank=True, verbose_name=_('Apple Submitted'))
    checkapp = models.DateField(null=True, blank=True, verbose_name=_('Check Apple Submission'))
    apppub = models.DateField(null=True, blank=True, verbose_name=_('Apple Published'))
    applaunch = models.DateField(null=True, blank=True, verbose_name=_('Apple Launch Date'))
    eventdate = models.DateField(null=True, blank=True, verbose_name=_('Event Date'))
    guides = models.TextField(default='Guide Names')
    
    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class ClientBuild(models.Model):

    buildusername = models.CharField(max_length=45, unique=True, verbose_name=_('Build Username'))
    buildpassword = models.CharField(max_length=45, unique=True, verbose_name=_('Build Password'))

    def __str__(self):
        return self.name