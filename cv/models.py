from django.db import models

class BrainScans(models.Model):
    name        = models.CharField(max_length=200)
    image       = models.ImageField(upload_to='images')
    imageName   = models.CharField(max_length=200, editable=False, null=True, blank=True)
    prediction  = models.FloatField(editable=False, name="prediction", null=True, max_length=5, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        app_label  = 'cv'
