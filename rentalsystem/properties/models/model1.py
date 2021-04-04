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
from rentalsystem.common.models import AbstractBaseModel, AbstractPropertyBaseModel
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

    @property
    def user_indexing(self):
        """
        Used in Elasticsearch indexing.
        """
        if self.landlord is not None:
            return self.landlord.id


class PropertyAddress(AbstractPropertyBaseModel):
    """ Property's Address Model"""

    PROPERTY_ADDRESS = "propertyAddress"
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


class PropertyImage(AbstractPropertyBaseModel):
    """ Property Image Model"""

    PROPERTY_IMAGE = "propertyImage"
    property = ForeignKey(Property, related_name="propertyImage", on_delete=CASCADE)
    image = ImageField(blank=True, storage=MediaRootS3Boto3Storage())


class OwnershipDocument(AbstractPropertyBaseModel):
    """ Property Document Model"""

    property = ForeignKey(Property, related_name="propertyDocument", on_delete=CASCADE)
    document = FileField(blank=True, storage=MediaRootS3Boto3Storage())
