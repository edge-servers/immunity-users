from immunity_users.tests.test_api import AuthenticationMixin
from immunity_users.tests.utils import TestMultitenantAdminMixin, TestOrganizationMixin

from .. import CreateMixin


class TestMultitenancyMixin(
    CreateMixin, TestMultitenantAdminMixin, AuthenticationMixin, TestOrganizationMixin
):
    pass
