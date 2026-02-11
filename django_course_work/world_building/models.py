from django.db import models

class World(models.Model):
    seed = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PoliticalEntity(models.Model):
    world = models.ForeignKey(
        World,
        on_delete=models.CASCADE,
        related_name="political_entities"
    )

    name = models.CharField(max_length=100)
    government_type = models.CharField(max_length=100)
    dominant_trait = models.CharField(max_length=100)

    power_level = models.IntegerField(default=50)  # 0–100 scale
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.world.name})"
