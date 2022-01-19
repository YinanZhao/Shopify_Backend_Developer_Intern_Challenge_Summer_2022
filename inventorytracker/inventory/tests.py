from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from.models import Item, Location


# Test cases for index APIs
class TestIndexPage(APITestCase):
    def test_valid_index_get(self):
        """
        Testing get items
        """
        url = reverse('index')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test cases for create APIs
class TestCreatePage(APITestCase):
    def test_valid_create(self):
        """
        Testing create item
        """
        url = reverse('create')
        data = {
            "count": "26",
            "name": "alphabet",
            "description": "First letter",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Test Cases for update items API
class TestUpdateItems(APITestCase):
    def setUp(self):
        mtl = Location.objects.create(
            city_name="Montreal"
        )
        trt = Location.objects.create(
            city_name="Toronto"
        )
        a = Location.objects.create(
            city_name="A"
        )

        Item.objects.create(
            count="12",
            name="Shovels",
            description="Good for snow",
            location=mtl
        )

        Item.objects.create(
            count="1",
            name="CN Tower",
            description="Nice View!",
            location=trt
        )

        Item.objects.create(
            count="26",
            name="alphabet",
            description="First letter",
            location=a
        )

    def test_update_Items(self):
        """
        Ensure we can update item in Inventory.
        """
        data = {
            "count": "1",
            "name": "Shovel",
            "description": "changed number of shovels"
        }
        url = '/1/detail/'

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_details(self):
        """
        Ensure we can update item in Inventory.
        """
        data = {
            "count": "1",
            "name": "Shovel",
            "description": "changed number of shovels"
        }
        url = '/1/detail/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test cases for delete APIs
class TestDelete(APITestCase):
    def setUp(self):
        mtl = Location.objects.create(
            city_name="Montreal"
        )
        trt = Location.objects.create(
            city_name="Toronto"
        )
        a = Location.objects.create(
            city_name="A"
        )

        Item.objects.create(
            count="12",
            name="Shovels",
            description="Good for snow",
            location=mtl
        )

        Item.objects.create(
            count="1",
            name="CN Tower",
            description="Nice View!",
            location=trt
        )

        Item.objects.create(
            count="26",
            name="alphabet",
            description="First letter",
            location=a
        )

    def test_valid_delete_item(self):
        """
        Test we can delete item in Inventory.
        """

        response1 = self.client.get('/1/delete/')
        self.assertEqual(response1.status_code, status.HTTP_302_FOUND)

        # now that we deleted it, we shouldn't be able to find it anymore
        url = '/1/detail/'
        response2 = self.client.get(url)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_delete_location(self):
        """
        Test we can delete location
        """

        response1 = self.client.get('/1/delete_location/')
        self.assertEqual(response1.status_code, status.HTTP_302_FOUND)