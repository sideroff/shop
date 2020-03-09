from .service_providers import users

# include all service providers here
service_providers = {
    'users': users
}


def execute_request(service_provider_name: str, service_name: str, params: dict):

    if not service_provider_name in service_providers:
        return 'no such service provider ' + service_provider_name

    service_provider_module = service_providers.get(service_provider_name)

    if not hasattr(service_provider_module, service_name):
        return 'no such service_name in service provider ' + service_name

    service = getattr(service_provider_module, service_name)
    print(service)
    return service(**params)
