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
    FileField,
)

from rentalsystem.common.models import PROPERTY, ID
from rentalsystem.properties.models import (
    PropertyRules,
    Property,
    PropertyAddress,
    PropertyAmenities,
    PropertyImage,
)

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
    unit = IntegerField()
    size = FloatField()
    propertyStatus = TextField()
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
    propertyAmenities = ObjectField(
        properties={
            PROPERTY: TextField(
                attr="property_indexing",
            ),
            PropertyAmenities.POOL: BooleanField(),
            PropertyAmenities.GARDEN: BooleanField(),
            PropertyAmenities.ELEVATOR: BooleanField(),
            PropertyAmenities.DOORMAN: BooleanField(),
            PropertyAmenities.DECK: BooleanField(),
            PropertyAmenities.WASHER: BooleanField(),
            PropertyAmenities.GYM: BooleanField(),
            PropertyAmenities.PARKING: BooleanField(),
            PropertyAmenities.FIRE_PLACE: BooleanField(),
            PropertyAmenities.AIR_CONDITION: BooleanField(),
            PropertyAmenities.DISH_WASHER: BooleanField(),
            PropertyAmenities.ITEM_STORAGE: BooleanField(),
            PropertyAmenities.WHEELCHAIR: BooleanField(),
            PropertyAmenities.BALCONY: BooleanField(),
            PropertyAmenities.HARD_FLOOR: BooleanField(),
            PropertyAmenities.FURNISHED: BooleanField(),
            PropertyAmenities.VIEW: BooleanField(),
            PropertyAmenities.HIGH_RISE: BooleanField(),
            PropertyAmenities.STUDENT_FRIENDLY: BooleanField(),
            PropertyAmenities.UTILITIES: BooleanField(),
        }
    )
    propertyImage = ObjectField(
        properties={
            ID: IntegerField(attr="id"),
            PROPERTY: TextField(
                attr="property_indexing",
            ),
            PropertyImage.IMAGE: FileField(),
        }
    )

    class Django(object):
        """The Django model associate with this Document"""

        model = Property
