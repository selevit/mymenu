from django.db import models


class Menu(models.Model):
    "Site menu entity"

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    def items(self):
        return self.menuitem_set.all()


class MenuItem(models.Model):
    "Site menu items"

    LINK_TARGET_CHOICES = (
        ('_blank', '_blank'),
        ('_top', '_top'),
        ('_parent', '_parent'),
    )

    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(
        max_length=10,
        choices=LINK_TARGET_CHOICES,
        null=True,
        blank=True
    )
    menu = models.ForeignKey('Menu')

    def __unicode__(self):
        return self.url
