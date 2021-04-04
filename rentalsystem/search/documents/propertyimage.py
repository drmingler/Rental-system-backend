from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields, TextField

from rentalsystem.properties.models import PropertyImage

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class PropertyImageDocument(Document):
    """PropertyImage Elasticsearch document."""

    id = fields.IntegerField(attr="id")
    property = fields.TextField(attr="property_indexing")
    image = fields.FileField()

    class Django(object):
        """The model associate with this Document"""

        model = PropertyImage
