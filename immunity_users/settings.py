from django.conf import settings
from immunity_utils.utils import default_or_test

ORGANIZATION_USER_ADMIN = getattr(settings, 'IMMUNITY
_ORGANIZATION_USER_ADMIN', True)
ORGANIZATION_OWNER_ADMIN = getattr(settings, 'IMMUNITY
_ORGANIZATION_OWNER_ADMIN', True)
USERS_AUTH_API = getattr(settings, 'IMMUNITY
_USERS_AUTH_API', True)
USERS_AUTH_THROTTLE_RATE = getattr(
    settings,
    'IMMUNITY
_USERS_AUTH_THROTTLE_RATE',
    default_or_test(value='20/day', test=None),
)
AUTH_BACKEND_AUTO_PREFIXES = getattr(
    settings, 'IMMUNITY
_USERS_AUTH_BACKEND_AUTO_PREFIXES', tuple()
)
EXPORT_USERS_COMMAND_CONFIG = {
    'fields': [
        'id',
        'username',
        'email',
        'password',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'phone_number',
        'birth_date',
        'location',
        'notes',
        'language',
        'organizations',
    ],
    'select_related': [],
}
USER_PASSWORD_EXPIRATION = getattr(
    settings, 'IMMUNITY
_USERS_USER_PASSWORD_EXPIRATION', 0
)
STAFF_USER_PASSWORD_EXPIRATION = getattr(
    settings, 'IMMUNITY
_USERS_STAFF_USER_PASSWORD_EXPIRATION', 0
)
# Set the AutocompleteFilter view if it is not defined in the settings
setattr(
    settings,
    'IMMUNITY
_AUTOCOMPLETE_FILTER_VIEW',
    getattr(
        settings,
        'IMMUNITY
_AUTOCOMPLETE_FILTER_VIEW',
        'immunity_users.views.AutocompleteJsonView',
    ),
)
