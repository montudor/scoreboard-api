from django.db import models

class Score(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField()
    level = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s's Score (%i)" % (self.name, self.score)
