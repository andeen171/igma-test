from .models import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ClientTests(APITestCase):

    def test_create_client(self):
        """
        Ensure we can create a new client.
        """
        url = reverse('clientes')
        data = {'name': 'test', 'cpf': '879.887.970-77', 'birth_date': '19/02/2003'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'test')
        self.assertEqual(Client.objects.get().cpf, '87988797077')

    def test_create_client_with_invalid_cpf(self):
        """
        Ensure we can't create a client with an invalid cpf.
        """
        url = reverse('clientes')
        data = {'name': 'test', 'cpf': '879.887.970-76', 'birth_date': '19/02/2003'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(Client.objects.count(), 0)

    def test_get_client(self):
        """
        Ensure we can get a client by id.
        """
        url = reverse('clientes')
        data = {'name': 'test', 'cpf': '879.887.970-77', 'birth_date': '19/02/2003'}
        self.client.post(url, data, format='json')

        url = reverse('cliente', kwargs={'cpf': '87988797077'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'test')
        self.assertEqual(Client.objects.get().cpf, '87988797077')

    def test_update_client(self):
        """
        Ensure we can update a client.
        """
        url = reverse('clientes')
        data = {'name': 'test', 'cpf': '879.887.970-77', 'birth_date': '19/02/2003'}
        self.client.post(url, data, format='json')

        url = reverse('cliente', kwargs={'cpf': '87988797077'})
        data = {'name': 'test2', 'cpf': '879.887.970-77', 'birth_date': '19/02/2003'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'test2')
        self.assertEqual(Client.objects.get().cpf, '87988797077')

    def test_delete_client(self):
        """
        Ensure we can delete a client.
        """
        url = reverse('clientes')
        data = {'name': 'test', 'cpf': '879.887.970-77', 'birth_date': '19/02/2003'}
        self.client.post(url, data, format='json')

        url = reverse('cliente', kwargs={'cpf': '87988797077'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 0)
