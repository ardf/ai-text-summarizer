from django.db import models

# Create your models here.


class TextSummary(models.Model):
    text = models.TextField()
    summary = models.TextField()
    bullet_points = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Summary {self.pk}"
