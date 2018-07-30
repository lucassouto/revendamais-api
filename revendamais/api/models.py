from django.db import models
from model_utils.models import TimeStampedModel


class Searches(TimeStampedModel):
    search = models.CharField(max_length=50)
