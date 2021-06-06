from django.db.models import (
    ForeignKey,
    CASCADE,
    CharField,
    TextField,
    DateField,
    DecimalField,
    OneToOneField,
    FileField,
    IntegerField,
    FloatField,
    ImageField,
)

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
    UNIT = "unit"
    SIZE = "size"
    PROPERTY_STATUS = "propertyStatus"
    PROPERTY_TYPE = "propertyType"
    MONTHLY_RENT = "monthlyRent"
    SECURITY_DEPOSIT = "securityDeposit"

    APARTMENT = "Apartment"
    HOUSE = "House"
    CONDO = "Condo"
    DUPLEX = "Duplex"
    ROOM = "Room"

    PENDING = "Pending"
    VERIFIED = "Verified"
    REJECTED = "Rejected"
    EXPIRED = "Expired"

    PROPERTY_TYPES = (
        (APARTMENT, "Apartment"),
        (HOUSE, "House"),
        (CONDO, "Condo"),
        (DUPLEX, "Duplex"),
        (ROOM, "Room"),
    )

    LISTING_STATUS = (
        (PENDING, "Pending"),
        (VERIFIED, "Verified"),
        (REJECTED, "Rejected"),
        (EXPIRED, "Expired"),
    )

    class Meta:
        verbose_name_plural = "Properties"

    landlord = ForeignKey(User, related_name="properties", on_delete=CASCADE)
    propertyName = CharField("Property name", max_length=250, blank=True)
    numberOfBedrooms = IntegerField("Number of bedrooms", default=0)
    numberOfBathrooms = IntegerField("Number of bathrooms", default=0)
    listingDescription = TextField("Listing description", blank=True)
    availableFrom = DateField("Available from", max_length=20, blank=True)
    propertyType = CharField(
        "Property type", max_length=20, choices=PROPERTY_TYPES, blank=True
    )
    unit = IntegerField(default=0)
    size = DecimalField(default=0.00, max_digits=6, decimal_places=2)
    propertyStatus = CharField(
        "Property status", max_length=20, choices=LISTING_STATUS, default=PENDING
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
    latitude = FloatField(
        default=0.00,
        blank=True,
    )
    longitude = FloatField(
        default=0.00,
        blank=True,
    )


class PropertyImage(AbstractPropertyBaseModel):
    """ Property Image Model"""

    PROPERTY_IMAGE = "propertyImage"
    IMAGE = "image"

    property = ForeignKey(Property, related_name="propertyImage", on_delete=CASCADE)
    image = ImageField(blank=True, storage=MediaRootS3Boto3Storage())


class OwnershipDocument(AbstractPropertyBaseModel):
    """ Property Document Model"""

    PROPERTY_DOCUMENT = "propertyDocument"
    DOCUMENT = "document"

    property = ForeignKey(Property, related_name="propertyDocument", on_delete=CASCADE)
    document = FileField(blank=True, storage=MediaRootS3Boto3Storage())
