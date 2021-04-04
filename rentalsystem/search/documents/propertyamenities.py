from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields

from rentalsystem.properties.models import PropertyAmenities

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class PropertyAmenitiesDocument(Document):
    """PropertyAmenities Elasticsearch document."""

    id = fields.IntegerField(attr="id")
    property = fields.TextField(
        attr="property_indexing",
    )
    pool = fields.BooleanField()
    garden = fields.BooleanField()
    elevator = fields.BooleanField()
    doorman = fields.BooleanField()
    deck = fields.BooleanField()
    washer = fields.BooleanField()
    gym = fields.BooleanField()
    parking = fields.BooleanField()
    firePlace = fields.BooleanField()
    airCondition = fields.BooleanField()
    dishWasher = fields.BooleanField()
    itemStorage = fields.BooleanField()
    wheelchair = fields.BooleanField()
    balcony = fields.BooleanField()
    hardFloor = fields.BooleanField()
    furnished = fields.BooleanField()
    view = fields.BooleanField()
    highRise = fields.BooleanField()
    studentFriendly = fields.BooleanField()
    utilities = fields.BooleanField()

    class Django(object):
        """The model associate with this Document"""

        model = PropertyAmenities
