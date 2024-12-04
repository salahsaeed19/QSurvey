from django.db import models
from surveys.models import Survey


class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='responses')
    respondent_email = models.EmailField()
    answers = models.JSONField()  # Store responses as JSON
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.survey.title} by {self.respondent_email}"