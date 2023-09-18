from django.apps import AppConfig
from django_elasticsearch_dsl.apps import DEDConfig

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'


class MyAppDEDConfig(DEDConfig):
    name = 'inventory'
    
