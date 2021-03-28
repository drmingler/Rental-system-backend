from django.contrib import admin
from rentalsystem.properties.models import (
    Property,
    PropertyAddress,
    PropertyRules,
    OwnershipDocument,
)

# Register your models here.
common_fields = ["created_at", "updated_at"]


class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "propertyName",
        "propertyType",
        "numberOfBedrooms",
        "numberOfBathrooms",
        "unit",
        "size",
        "listingDescription",
        "availableFrom",
        "monthlyRent",
        "securityDeposit",
        "isOwnerShipVerified",
    ] + common_fields


class PropertyAddressAdmin(admin.ModelAdmin):
    list_display = [
        "property",
        "address",
        "stateName",
        "latitude",
        "longitude",
    ] + common_fields


class PropertyRulesAdmin(admin.ModelAdmin):
    list_display = [
        "property",
        "smoking",
        "pet",
        "musicalInstruments",
    ] + common_fields


class OwnershipDocumentAdmin(admin.ModelAdmin):
    list_display = [
        "property",
        "document",
    ] + common_fields


class PropertyAmenitiesAdmin(admin.ModelAdmin):
    list_display = [
        "property",
        "pool",
        "garden",
        "elevator",
        "doorman",
        "dryer",
        "washer",
        "gym",
        "parking",
        "firePlace",
        "airCondition",
        "itemStorage",
        "wheelchair",
        "balcony",
        "hardFloor",
        "furnished",
        "view",
        "highRise",
        "studentFriendly",
        "utilities",
    ] + common_fields


class AvailableLocationsAdmin(admin.ModelAdmin):
    list_display = [
        "latitude",
        "longitude",
        "stateName",
        "nationality",
    ] + common_fields


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyAddress, PropertyAddressAdmin)
admin.site.register(PropertyRules, PropertyRulesAdmin)
admin.site.register(OwnershipDocument, OwnershipDocumentAdmin)
