from django.conf import settings
from django_elasticsearch_dsl import (
    Document,
    Index,
    IntegerField,
    TextField,
    DateField,
    BooleanField,
    FloatField,
    ObjectField,
)

from rentalsystem.common.models import PROPERTY
from rentalsystem.properties.models import PropertyRules, Property, PropertyAddress

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class PropertyDocument(Document):
    """Property Elasticsearch document."""

    id = IntegerField(attr="id")
    propertyName = TextField()
    landlord = TextField(
        attr="user_indexing",
    )
    numberOfBedrooms = IntegerField()
    numberOfBathrooms = IntegerField()
    propertyType = TextField()
    availableFrom = DateField()
    listingDescription = TextField()
    isOwnerShipVerified = BooleanField()
    unit = IntegerField()
    size = FloatField()
    monthlyRent = FloatField()
    securityDeposit = FloatField()
    created_at = DateField()
    propertyRules = ObjectField(
        properties={
            PROPERTY: TextField(
                attr="property_indexing",
            ),
            PropertyRules.SMOKING: BooleanField(),
            PropertyRules.PET: BooleanField(),
            PropertyRules.MUSICAL_INSTRUMENTS: BooleanField(),
        }
    )
    propertyAddress = ObjectField(
        properties={
            PROPERTY: TextField(
                attr="property_indexing",
            ),
            PropertyAddress.ADDRESS: TextField(),
            PropertyAddress.STATE_NAME: TextField(),
            PropertyAddress.LATITUDE: FloatField(),
            PropertyAddress.LONGITUDE: FloatField(),
        }
    )

    class Django(object):
        """The Django model associate with this Document"""

        model = Property
