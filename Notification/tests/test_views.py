import unittest
from Notification.models import *
class Test(unittest.TestCase):
    def test(self):
        Campus.objects.create(nome="gamb")