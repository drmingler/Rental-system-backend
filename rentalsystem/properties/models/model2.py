from django.db.models import CASCADE, CharField, BooleanField, OneToOneField, FloatField

from rentalsystem.common.models import AbstractBaseModel, AbstractPropertyBaseModel
from rentalsystem.properties.models import Property


class PropertyRules(AbstractPropertyBaseModel):
    """ Property's Rules Model"""

    PROPERTY_RULES = "propertyRules"
    SMOKING = "smoking"
    PET = "pet"
    MUSICAL_INSTRUMENTS = "musicalInstruments"

    class Meta:
        verbose_name_plural = "Property Rules"

    property = OneToOneField(Property, related_name="propertyRules", on_delete=CASCADE)
    smoking = BooleanField(default=False)
    pet = BooleanField(default=False)
    musicalInstruments = BooleanField(default=False)


class PropertyAmenities(AbstractPropertyBaseModel):
    """ Property Amenities Model"""

    PROPERTY_AMENITIES = "propertyAmenities"
    POOL = "pool"
    GARDEN = "garden"
    ELEVATOR = "elevator"
    DOORMAN = "doorman"
    DECK = "deck"
    WASHER = "washer"
    GYM = "gym"
    PARKING = "parking"
    FIRE_PLACE = "firePlace"
    AIR_CONDITION = "airCondition"
    DISH_WASHER = "dishWasher"
    ITEM_STORAGE = "itemStorage"
    WHEELCHAIR = "wheelchair"
    BALCONY = "balcony"
    HARD_FLOOR = "hardFloor"
    FURNISHED = "furnished"
    VIEW = "view"
    HIGH_RISE = "highRise"
    STUDENT_FRIENDLY = "studentFriendly"
    UTILITIES = "utilities"

    class Meta:
        verbose_name_plural = "Property Amenities"

    property = OneToOneField(
        Property, related_name="propertyAmenities", on_delete=CASCADE
    )
    pool = BooleanField(default=False)
    garden = BooleanField(default=False)
    elevator = BooleanField(default=False)
    doorman = BooleanField(default=False)
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

    latitude = FloatField(
        default=0.00,
        blank=True,
    )
    longitude = FloatField(
        default=0.00,
        blank=True,
    )
    stateName = CharField("State name", blank=True, max_length=50)
    country = CharField(blank=True, max_length=40)
