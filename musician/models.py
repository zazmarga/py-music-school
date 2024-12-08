from django.db import models
from django.db.models import Q


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self) -> bool:
        return self.age >= 21

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(age__gte=14),
                name="acceptable_age"
            ),
        ]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
