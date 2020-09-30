from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# post model
class Post(models.Model):
    # title will be a field with characters
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # cascade deletes all user's posts when author is deleted, but doesnt delete author when post is deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

