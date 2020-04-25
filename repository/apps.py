from django.apps import AppConfig

class RepositoryConfig(AppConfig):
    name = 'repository'

    def ready(self):
        import repository.signals
        from ProgImageService.settings.dependency_injection.config import di_configuration
        import inject

        inject.configure(di_configuration)

