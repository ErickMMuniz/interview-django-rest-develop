from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Product

class ProductoAPITest(APITestCase):
    def setUp(self):
        self.producto = Product.objects.create(
            name="Teléfono",
            description="Un teléfono inteligente",
            price=500.00,
            is_available=True
        )
        self.url_list = reverse('producto-list')
        self.url_detail = reverse('producto-detail', args=[self.producto.id])

    def test_create_producto(self):
        """Asegura que podemos crear un nuevo producto."""
        data = {
            "name": "Tablet",
            "description": "Una tablet de 10 pulgadas",
            "price": 300.00
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(id=response.data['id']).name, 'Tablet')

    def test_list_productos(self):
        """Asegura que la lista de productos funciona."""
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Teléfono')

    def test_retrieve_producto(self):
        """Asegura que podemos obtener un producto específico."""
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Teléfono')

    def test_update_producto(self):
        """Asegura que podemos actualizar un producto."""
        data = {
            "name": "Teléfono actualizado",
            "description": "Un teléfono inteligente actualizado",
            "price": 600.00,
            "is_available": False
        }
        response = self.client.put(self.url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.name, 'Teléfono actualizado')

    def test_delete_producto(self):
        """Asegura que podemos eliminar un producto."""
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)