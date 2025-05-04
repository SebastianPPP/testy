from django.db import models

class DroneData(models.Model):
    drone_id = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.drone_id} @ {self.timestamp}"