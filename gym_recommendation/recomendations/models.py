from django.db import models

class UserPreference(models.Model):
    user_id = models.IntegerField(unique=True)
    protein = models.IntegerField()
    creatine = models.IntegerField()
    bcaa = models.IntegerField()

    def __str__(self):
        return f"User {self.user_id}"
