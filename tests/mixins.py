import sys
from unittest.mock import patch

from .decorators import social_auth_mock


class SocialAuthTestsMixin:

    @social_auth_mock
    @patch('graphql_social_auth.decorators.login')
    def test_social_auth(self, *args):
        response = self.execute({
            'provider': 'google-oauth2',
            'accessToken': '-token-',
        })

        social = response.data['socialAuth']['social']
        self.assertEqual('test', social['uid'])


class SocialAuthJWTTestsMixin:

    @social_auth_mock
    @patch.dict(sys.modules, {'graphql_jwt.shortcuts': None})
    def test_social_auth_import_error(self, *args):
        response = self.execute({
            'provider': 'google-oauth2',
            'accessToken': '-token-',
        })

        self.assertTrue(response.errors)
        self.assertIsNone(response.data['socialAuth'])
