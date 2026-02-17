from django.db import models

class TileMap(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField(default=20)
    height = models.IntegerField(default=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tile(models.Model):
    tilemap = models.ForeignKey(
        TileMap,
        on_delete=models.CASCADE,
        related_name="tiles"
    )

    x = models.IntegerField()
    y = models.IntegerField()
    terrain_type = models.CharField(max_length=50, default="grass")
