from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    group = models.ForeignKey("Groups.Group", on_delete=models.DO_NOTHING, null=True, related_name="teachers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
