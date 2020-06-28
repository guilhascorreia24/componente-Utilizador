from django.test import TestCase
from inscricao.models import *
from django.apps.registry import Apps
from django.db import models
class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Inscricao.objects.create(ano=2020, local='sdfsdfsdf', 
                            areacientifica='fghfghfgh', transporte='0')
