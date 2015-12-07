from django.db import models
from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField

class Document(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    search_index = VectorField()

    objects = SearchManager(
        fields = (('title', 'A'),('text', 'D')),
        config = 'pg_catalog.english', # this is default
        search_field = 'search_index', # this is default
        auto_update_search_field = True
    )

    def __str__(self):
        return self.title
