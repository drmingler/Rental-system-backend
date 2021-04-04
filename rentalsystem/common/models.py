from django.db import models

# Common model fields
ID = "id"
CREATED_AT = "created_at"
UPDATED_AT = "updated_at"
PROPERTY = "property"


class AbstractBaseModel(models.Model):
    """
    Base abstract model, that includes
    `created_at` and `updated_at` fields.
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
