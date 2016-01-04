from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Client(models.Model):
    GSTATUS = (
        (0,'New'),
        (1,'Guidebuilding'),
        (2,'Guidebuild Sufficient for Submission'),
        (3,'Complete'),
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
    gstatus = models.IntegerField(choices=GSTATUS, default=0, verbose_name=_('Guidebuilding Status'))
    appstatus = models.IntegerField(choices=APPSTATUS, default=0, verbose_name=_('Apple Store Status'))
    pstatus = models.IntegerField(choices=PSTATUS, default=0, verbose_name=_('Google Play Status'))
    bstatus = models.IntegerField(choices=BSTATUS, default=0, verbose_name=_('Blackberry Status'))
    astatus = models.IntegerField(choices=ASTATUS, default=0, verbose_name=_('Amazon Status'))
    intro = models.DateField(null=True, blank=True, verbose_name=_('Intro Email Sent'))
    appsub = models.DateField(null=True, blank=True, verbose_name=_('Apple Submitted'))
    apppub = models.DateField(null=True, blank=True, verbose_name=_('Apple Published'))
    applaunch = models.DateField(null=True, blank=True, verbose_name=_('Apple Launch Date'))
    guides = models.TextField(default='Guide Names')
    def __unicode__(self):
        return self.name