# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .test_base import BaseAPITestCase


class APITestSignature(BaseAPITestCase):
    """
    Case #1:
    - user profile: defined
    - custom registration: backend defined
    """

    MOBILE = '18742514206'
    VERIFY = '123456'

    def setUp(self):
        self.init()

        owenr = get_user_model()(mobile=self.MOBILE)
        owenr.save()

        self._generate_uid_and_token(user=owenr)

    def test_identity_validation(self):
        payload = {
            "certId": "230221198902203010",
            "name": "刘鹏",
            "phone": "13141039522",
            "cardNo": "6227000014150347510",
            "bankID": "CCB",
            "level": "D",
        }
    
        resp = self.post('/api/sign/identity/', data=payload, status_code=200)
