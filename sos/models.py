from datetime import datetime

from django.db import models
from django.urls import reverse

# Create your models here.
from accounts.models import User
from critical_list.models import Part


class Sos(models.Model):
    class Meta:
        ordering = ["-id"]
        permissions = (
            ("can_change_status", "Can Change Status"),
        )

    name = models.CharField(max_length=50, help_text="Name")
    content = models.CharField(max_length=100, help_text="Enter Content")
    media = models.FileField(help_text="Media", upload_to='content/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(max_length=30, help_text="Date", default=datetime.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Original Poster", related_name='post_by')
    users = models.ManyToManyField(User, help_text="Employee Involved", related_name='employee_involved', blank=True)
    level = models.IntegerField(help_text="Enter Level")
    status = models.BooleanField(help_text="Open Or Closed", default=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('sos-detail', args=[str(self.id)])


class Comment(models.Model):
    class Meta:
        ordering = ["-posted_by"]

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Original Poster",
                                  related_name='comment_by')
    sosid = models.ForeignKey(Sos, on_delete=models.CASCADE, blank=True, null=True)
    partid = models.ForeignKey(Part, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(help_text="Enter Level", default=datetime.now)
    content = models.CharField(max_length=100, help_text="Enter Content")
    media = models.FileField(help_text="Media", upload_to='comment/%Y/%m/%d/', blank=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('comment-detail', args=[str(self.id)])
