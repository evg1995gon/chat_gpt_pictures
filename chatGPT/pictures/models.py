from django.db import models
from sorl.thumbnail import ImageField


class Pictures(models.Model):
    name = models.TextField(
        blank=False,
        null=False,
    )
    picture = ImageField(
        'Picture',
        upload_to='pictures/',
        blank=True,
    )
    picture_url = models.URLField(
        max_length=1000,
        blank=False,
        null=False,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        if len(self.name) < 15:
            return self.name
        return self.name[:13] + '...'
