from django.contrib import admin
from rentalsystem.properties.models import (
    Property,
    PropertyAddress,
    PropertyRules,
    OwnershipDocument,
    PropertyAmenities,
    AvailableLocation,
    PropertyImage,
)

# Register your models here.
common_fields = ["created_at", "updated_at"]


class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        "landlord",
        "propertyName",
        "propertyType",
        "numberOfBedrooms",
        "numberOfBathrooms",
        "unit",
        "size",
        "propertyStatus",
        "listingDescription",
        "availableFrom",
        "monthlyRent",
        "securityDeposit",
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


class PropertyImageAdmin(admin.ModelAdmin):
    list_display = [
        "property",
        "image",
    ] + common_fields


class PropertyAmenitiesAdmin(admin.ModelAdmin):
    list_display = [
        "property",
        "pool",
        "garden",
        "elevator",
        "doorman",
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


class AvailableLocationAdmin(admin.ModelAdmin):
    list_display = [
        "latitude",
        "longitude",
        "stateName",
        "country",
    ] + common_fields


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyAddress, PropertyAddressAdmin)
admin.site.register(PropertyRules, PropertyRulesAdmin)
admin.site.register(OwnershipDocument, OwnershipDocumentAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
admin.site.register(PropertyAmenities, PropertyAmenitiesAdmin)
admin.site.register(AvailableLocation, AvailableLocationAdmin)
