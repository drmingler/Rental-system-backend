from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields

from rentalsystem.properties.models import PropertyAddress

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class PropertyAddressDocument(Document):
    """PropertyAddress Elasticsearch document."""

    id = fields.IntegerField(attr="id")
    property = fields.TextField(
        attr="property_indexing",
    )
    address = fields.TextField()
    stateName = fields.TextField()
    latitude = fields.FloatField()
    longitude = fields.FloatField()

    class Django(object):
        """The model associate with this Document"""

        model = PropertyAddress
