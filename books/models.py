from django.db import models

class BookQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_deleted=True)

class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)

    objects = BookManager()
    all_objects = models.Manager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.title

# Create your models heree.

# Create your models heree.
