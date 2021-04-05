from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry


@receiver([post_save])
def update_document(sender, instance, **kwargs):
    model_name = sender._meta.model_name
    if model_name == "propertyrules":
        registry.update(instance.property)

    if model_name == "propertyamenities":
        registry.update(instance.property)

    if model_name == "propertyimage":
        registry.update(instance.property)

    if model_name == "propertyaddress":
        registry.update(instance.property)


@receiver([post_delete])
def delete_document(sender, **kwargs):
    model_name = sender._meta.model_name
    instance = kwargs["instance"]

    if model_name == "propertyrules":
        registry.delete(instance, raise_on_error=False)

    if model_name == "propertyamenities":
        registry.delete(instance, raise_on_error=False)

    if model_name == "propertyimage":
        registry.delete(instance, raise_on_error=False)

    if model_name == "propertyaddress":
        registry.delete(instance, raise_on_error=False)
