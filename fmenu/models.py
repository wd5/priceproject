from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    position = models.PositiveIntegerField(default=100)
    login_required = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["position"]

    def __unicode__(self):
        return u"%s" % (self.title)

    class Meta:
        ordering = ["position"]
 
