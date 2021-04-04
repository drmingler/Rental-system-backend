from django.db import models


# Create your models here.
class AbstractBaseModel(models.Model):
    """
    Base abstract model, that has `uuid` instead of `id` and includes
    `created_at`, `updated_at` fields.
    """

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        abstract = True


class AbstractPropertyBaseModel(AbstractBaseModel):
    """
    Base model for any model that has a relationship with the property model.
    """

    property = None

    def property_indexing(self):
        """
        Used in Elasticsearch indexing.
        """
        if self.property is not None:
            return self.property.id

    class Meta:
        abstract = True
