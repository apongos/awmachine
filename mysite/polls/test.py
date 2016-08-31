import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Comment


class CommentMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_comment = Comment(pub_date=time)
        self.assertIs(future_comment.was_published_recently(), False)

def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() should return False for questions whose
    pub_date is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=30)
    old_comment = Comment(pub_date=time)
    self.assertIs(old_comment.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() should return True for questions whose
    pub_date is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_comment = Comment(pub_date=time)
    self.assertIs(recent_comment.was_published_recently(), True)