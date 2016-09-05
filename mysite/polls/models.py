import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.urlresolvers import reverse


class Comment(models.Model):
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('polls:index' )
    def __str__(self):
        return self.comment_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.put_date <= now


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    def __str__(self):
    	return self.choice_text