from datetime import datetime

from django.db import models
from django.urls import reverse

# Create your models here.
from accounts.models import User
from critical_list.models import Part


class Comment(models.Model):
    class Meta:
        ordering = ["-posted_by"]

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Original Poster",
                                  related_name='comment_by')
    partid = models.ForeignKey(Part, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(help_text="posted at", default=datetime.now)
    content = models.CharField(max_length=100, help_text="Enter Content")
    media = models.FileField(help_text="Media", upload_to='comment/%Y/%m/%d/', blank=True)
    type = models.BooleanField(help_text="Part or Notification", default=False)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('comment-detail', args=[str(self.id)])