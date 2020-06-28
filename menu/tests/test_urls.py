from django.test import TestCase, SimpleTestCase
from menu.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_menu_list(self):
        url = reverse('menu:menu_list')
        self.assertEquals(resolve(url).func, menu_list_view)
    
    def test_menu_create(self):
        url = reverse('menu:menu_criar')
        self.assertEquals(resolve(url).func, menu_create_view)

    def test_prato_criar(self):
        url = reverse('menu:prato_criar')
        self.assertEquals(resolve(url).func, prato_create_view)

    def test_menu_detail(self):
        url = reverse('menu:menu_detail',args=[1002])
        self.assertEquals(resolve(url).func, menu_detail_view)
    
    def test_menu_update(self):
        url = reverse('menu:menu_update',args=[1002])
        self.assertEquals(resolve(url).func, menu_update_view)
    
    def test_prato_update(self):
        url = reverse('menu:prato_update',args=[1002])
        self.assertEquals(resolve(url).func, prato_update_view)
    
    def test_menu_delete(self):
        url = reverse('menu:menu_delete',args=[1002])
        self.assertEquals(resolve(url).func, menu_delete_view)
    
    def test_prato_delete(self):
        url = reverse('menu:prato_delete',args=[1002])
        self.assertEquals(resolve(url).func, prato_delete_view)

    def test_transport_list(self):
        url = reverse('menu:transporte-list')
        self.assertEquals(resolve(url).func, transporte_list_view)

    def test_transporte_create(self):
        url = reverse('menu:transporte-criar')
        self.assertEquals(resolve(url).func, transporte_create_view)

    def test_transportehora_create(self):
        url = reverse('menu:transportehora-criar')
        self.assertEquals(resolve(url).func, transportehora_create_view)

    def test_horario_create(self):
        url = reverse('menu:horario-list')
        self.assertEquals(resolve(url).func, horario_create_view)


    def test_transporte_detail(self):
        url = reverse('menu:transporte-detail',args=[1002])
        self.assertEquals(resolve(url).func,transporte_detail_view)

    def test_transporte_update(self):
        url = reverse('menu:transporte-update',args=[1002])
        self.assertEquals(resolve(url).func, transporte_update_view)

    def test_transporte_update2(self):
        url = reverse('menu:transporte-update2',args=[1002])
        self.assertEquals(resolve(url).func, transporte_update2_view)

    def test_transporte_delete(self):
        url = reverse('menu:transporte-delete',args=[1002])
        self.assertEquals(resolve(url).func, transporte_delete_view)

    def test_transporte_grupo(self):   
        url = reverse('menu:transporte-grupo',args=[1002])
        self.assertEquals(resolve(url).func, transporte_grupo_view)

    def test_transporte_delete(self):
        url = reverse('menu:transporte-horario')
        self.assertEquals(resolve(url).func, horariotransporte_create_view)


    def test_diaaberto_list(self):
        url = reverse('menu:diaaberto_list')
        self.assertEquals(resolve(url).func, diaaberto_list)

    def test_diaaberto_create(self):
        url = reverse('menu:diaaberto_create')
        self.assertEquals(resolve(url).func, diaaberto_create)
    
    def test_diaaberto_update(self):
        url = reverse('menu:diaaberto_update',args=[1002])
        self.assertEquals(resolve(url).func, diaaberto_update)
    
    def test_diaaberto_delete(self):
        url = reverse('menu:diaaberto_delete',args=[1002])
        self.assertEquals(resolve(url).func, diaaberto_delete)
    
    def test_diaaberto_details(self):
        url = reverse('menu:diaaberto_details',args=[1002])
        self.assertEquals(resolve(url).func, diaaberto_details)