# Create your models here.
from django.db.models import (
    ForeignKey,
    CASCADE,
    CharField,
    BooleanField,
    TextField,
    DateField,
    DecimalField,
    OneToOneField,
    FileField,
)
from django.forms import IntegerField

from rentalsystem.accounts.models import User
from rentalsystem.common.models import AbstractBaseModel
from rentalsystem.utils.storages import MediaRootS3Boto3Storage


class Property(AbstractBaseModel):
    """ Property Model """

    APARTMENT = "apartment"
    HOUSE = "house"
    CONDO = "condo"
    DUPLEX = "duplex"
    ROOM = "room"

    PROPERTY_TYPE = (
        (APARTMENT, "apartment"),
        (HOUSE, "house"),
        (CONDO, "condo"),
        (DUPLEX, "duplex"),
        (ROOM, "room"),
    )

    class Meta:
        verbose_name_plural = "Properties"

    user = ForeignKey(User, related_name="properties", on_delete=CASCADE)
    propertyName = CharField(max_length=250, blank=True)
    propertyType = CharField(max_length=20, choices=PROPERTY_TYPE, blank=True)
    numberOfBedrooms = IntegerField(max_value=20)
    numberOfBathrooms = IntegerField(max_value=20)
    unit = IntegerField(max_value=20)
    size = DecimalField(default=0.00)
    listingDescription = TextField(blank=True)
    availableFrom = DateField(max_length=20, blank=True)
    monthlyRent = DecimalField(default=0.00)
    securityDeposit = DecimalField(default=0.00)
    isOwnerShipVerified = BooleanField(default=False, max_length=20)


class PropertyAddress(AbstractBaseModel):
    """ Property's Address Model"""

    property = OneToOneField(
        Property, related_name="propertyAddress", on_delete=CASCADE
    )
    address = CharField(default=None, max_length=255)
    stateName = CharField(max_length=50, blank=True)
    latitude = DecimalField(default=None, blank=True)
    longitude = DecimalField(default=None, blank=True)


class PropertyRules(AbstractBaseModel):
    """ Property's Rules Model"""

    property = OneToOneField(Property, related_name="propertyRule", on_delete=CASCADE)
    smoking = BooleanField(default=False)
    pet = BooleanField(default=False)
    musicalInstruments = BooleanField(default=False)


class OwnershipDocument(AbstractBaseModel):
    """ Property Document Model"""

    property = ForeignKey(Property, related_name="propertyDocuments", on_delete=CASCADE)
    document = FileField(blank=True, storage=MediaRootS3Boto3Storage())


class PropertyAmenities(AbstractBaseModel):
    """ Property Amenities Model"""

    property = OneToOneField(
        Property, related_name="propertyAmenities", on_delete=CASCADE
    )
    pool = BooleanField(default=False)
    garden = BooleanField(default=False)
    elevator = BooleanField(default=False)
    doorman = BooleanField(default=False)
    dryer = BooleanField(default=False)
    deck = BooleanField(default=False)
    washer = BooleanField(default=False)
    gym = BooleanField(default=False)
    parking = BooleanField(default=False)
    firePlace = BooleanField(default=False)
    airCondition = BooleanField(default=False)
    dishWasher = BooleanField(default=False)
    storage = BooleanField(default=False)
    wheelchair = BooleanField(default=False)
    balcony = BooleanField(default=False)
    hardFloor = BooleanField(default=False)
    furnished = BooleanField(default=False)
    view = BooleanField(default=False)
    highRise = BooleanField(default=False)
    studentFriendly = BooleanField(default=False)
    utilities = BooleanField(default=False)
