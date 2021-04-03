from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from rentalsystem.properties.models import Property

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(number_of_shards=1, number_of_replicas=1)

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


@INDEX.doc_type
class PropertyDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr="id")

    landlord = fields.TextField(
        attr="user_indexing",
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    propertyName = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    numberOfBedrooms = fields.IntegerField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    numberOfBathrooms = fields.IntegerField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    availableFrom = fields.DateField()

    listingDescription = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    isOwnerShipVerified = fields.BooleanField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    unit = fields.IntegerField()

    size = fields.FloatField()

    propertyType = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    monthlyRent = fields.FloatField()

    securityDeposit = fields.FloatField()

    created_at = fields.DateField()

    class Django(object):
        """Inner nested class Django."""

        model = Property  # The model associate with this Document
