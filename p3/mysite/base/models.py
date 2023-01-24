from django.db import models

class News(models.Model):
    heading = models.CharField(max_length=100)
    all_news = models.TextField()
    def __str__(self):
        return self.heading

