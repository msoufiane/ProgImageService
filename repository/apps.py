from django.apps import AppConfig


class RepositoryConfig(AppConfig):
    name = 'repository'

    def ready(self):
        from ProgImageService.settings.dependency_injection.config import di_configuration
        from repository import signals
        import inject

        inject.configure(di_configuration)
