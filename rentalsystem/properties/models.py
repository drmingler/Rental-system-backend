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
    IntegerField,
)
from django.db.models.fields.files import ImageField

from rentalsystem.accounts.models import User
from rentalsystem.common.models import AbstractBaseModel
from rentalsystem.utils.storages import MediaRootS3Boto3Storage


class Property(AbstractBaseModel):
    """ Property Model """

    ID = "id"
    LANDLORD = "landlord"
    PROPERTY_NAME = "propertyName"
    NUMBER_OF_BEDROOMS = "numberOfBedrooms"
    NUMBER_OF_BATHROOMS = "numberOfBathrooms"
    LISTING_DESCRIPTION = "listingDescription"
    AVAILABLE_FROM = "availableFrom"
    IS_OWNERSHIP_VERIFIED = "isOwnerShipVerified"
    UNIT = "unit"
    SIZE = "size"
    PROPERTY_TYPE = "propertyType"
    MONTHLY_RENT = "monthlyRent"
    SECURITY_DEPOSIT = "securityDeposit"

    APARTMENT = "apartment"
    HOUSE = "house"
    CONDO = "condo"
    DUPLEX = "duplex"
    ROOM = "room"

    PROPERTY_TYPES = (
        (APARTMENT, "apartment"),
        (HOUSE, "house"),
        (CONDO, "condo"),
        (DUPLEX, "duplex"),
        (ROOM, "room"),
    )

    class Meta:
        verbose_name_plural = "Properties"

    landlord = ForeignKey(User, related_name="properties", on_delete=CASCADE)
    propertyName = CharField("Property name", max_length=250, blank=True)
    numberOfBedrooms = IntegerField("Number of bedrooms", default=0)
    numberOfBathrooms = IntegerField("Number of bathrooms", default=0)
    listingDescription = TextField("Listing description", blank=True)
    availableFrom = DateField("Available from", max_length=20, blank=True)
    isOwnerShipVerified = BooleanField("Is ownership verified", default=False)
    unit = IntegerField(default=0)
    size = DecimalField(default=0.00, max_digits=6, decimal_places=2)
    propertyType = CharField(
        "Property type", max_length=20, choices=PROPERTY_TYPES, blank=True
    )
    monthlyRent = DecimalField(
        "Monthly rent", default=0.00, max_digits=10, decimal_places=2
    )
    securityDeposit = DecimalField(
        "Security deposit", default=0.00, max_digits=10, decimal_places=2
    )


class PropertyAddress(AbstractBaseModel):
    """ Property's Address Model"""

    PROPERTY = "property"
    ADDRESS = "address"
    STATE_NAME = "stateName"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"

    class Meta:
        verbose_name_plural = "Property Addresses"

    property = OneToOneField(
        Property, related_name="propertyAddress", on_delete=CASCADE
    )
    address = CharField(default=None, max_length=255)
    stateName = CharField("State name", max_length=50, blank=True)
    latitude = DecimalField(default=None, blank=True, max_digits=6, decimal_places=2)
    longitude = DecimalField(default=None, blank=True, max_digits=6, decimal_places=2)


class PropertyImage(AbstractBaseModel):
    """ Property Image Model"""

    property = ForeignKey(Property, related_name="propertyImage", on_delete=CASCADE)
    image = ImageField(blank=True, storage=MediaRootS3Boto3Storage())


class OwnershipDocument(AbstractBaseModel):
    """ Property Document Model"""

    property = ForeignKey(Property, related_name="propertyDocument", on_delete=CASCADE)
    document = FileField(blank=True, storage=MediaRootS3Boto3Storage())


class PropertyRules(AbstractBaseModel):
    """ Property's Rules Model"""

    class Meta:
        verbose_name_plural = "Property Rules"

    property = OneToOneField(Property, related_name="propertyRule", on_delete=CASCADE)
    smoking = BooleanField(default=False)
    pet = BooleanField(default=False)
    musicalInstruments = BooleanField(default=False)


class PropertyAmenities(AbstractBaseModel):
    """ Property Amenities Model"""

    class Meta:
        verbose_name_plural = "Property Amenities"

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
    firePlace = BooleanField("Fire place", default=False)
    airCondition = BooleanField("Air condition", default=False)
    dishWasher = BooleanField("Dish washer", default=False)
    itemStorage = BooleanField("Item storage", default=False)
    wheelchair = BooleanField("Wheel chair", default=False)
    balcony = BooleanField(default=False)
    hardFloor = BooleanField("Hard floor", default=False)
    furnished = BooleanField(default=False)
    view = BooleanField(default=False)
    highRise = BooleanField("High rise", default=False)
    studentFriendly = BooleanField("Student friendly", default=False)
    utilities = BooleanField(default=False)


class AvailableLocation(AbstractBaseModel):
    """
    This model is not connected to any other model.
    It is used  by the map to get the various states and countries the application currently serves and
    the longitude and latitude of the location, in order to fetch properties from the database
    that falls in the range of the longitude and latitude.
    """

    latitude = DecimalField(default=None, blank=True, max_digits=6, decimal_places=2)
    longitude = DecimalField(default=None, blank=True, max_digits=6, decimal_places=2)
    stateName = CharField("State name", blank=True, max_length=50)
    nationality = CharField(blank=True, max_length=40)
