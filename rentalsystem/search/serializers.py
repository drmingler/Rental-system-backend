from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from rentalsystem.properties.models import Property
from rentalsystem.search.documents.property import PropertyDocument


class PropertyDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = PropertyDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            Property.ID,
            Property.LANDLORD,
            Property.PROPERTY_NAME,
            Property.NUMBER_OF_BEDROOMS,
            Property.NUMBER_OF_BATHROOMS,
            Property.LISTING_DESCRIPTION,
            Property.AVAILABLE_FROM,
            Property.IS_OWNERSHIP_VERIFIED,
            Property.UNIT,
            Property.SIZE,
            Property.PROPERTY_TYPE,
            Property.MONTHLY_RENT,
            Property.SECURITY_DEPOSIT,
        )
