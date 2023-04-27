from django.db import models

class Submission(models.Model):
    original_text = models.TextField()
    improved_text = models.TextField()

    def __str__(self):
        return f'Submission {self.pk}'
