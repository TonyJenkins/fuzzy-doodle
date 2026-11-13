from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    age = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "dog"

        verbose_name = "Dog"
        verbose_name_plural = "Dogs"

        ordering = ["name"]

    def __str__(self):
        return f"{self.name} the {self.breed}"

    @property
    def get_placeholder_image_url(self):
        return f"https://placedog.net/200x200?id={self.pk}"

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("apps.dog_roster:dog_detail", kwargs={"pk": self.pk})
