from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Service
from .serializers import ServiceSerializers

DATA = {
    "name": "ServiceTest",
    "description": "ServiceTest",
    "price": 7777.00,
}


class ServiceListViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

    def test_service_list(self) -> None:
        response = self.client.get(reverse('services:service_list'))
        self.assertQuerysetEqual(
            qs=Service.objects.all(),
            values=(service.pk for service in response.context["object_list"]),
            transform=lambda service: service.pk
        )

    def test_service_list_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse('services:service_list'))
        self.assertEqual(302, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ServiceDetailViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

    def test_service_details(self) -> None:
        response = self.client.get(reverse(
            'services:service_details',
            kwargs={'pk': 1})
        )
        response_data = response.context['object']
        queryset = Service.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, queryset)

    def test_service_details_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse(
            'services:service_details',
            kwargs={'pk': 1})
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ServiceCreateViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

    def test_service_create(self) -> None:
        response = self.client.post(reverse(
            'services:service_create'),
            DATA,
        )
        queryset = Service.objects.get(name=DATA["name"])
        serializers_data = ServiceSerializers(queryset).data
        self.assertEqual(serializers_data["name"], DATA["name"])
        self.assertEqual(serializers_data["description"], DATA["description"])
        self.assertRedirects(response, reverse('services:service_list'))

    def test_service_create_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'services:service_create'),
            DATA,
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ServiceViewUpdateTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

        self.data = {
            "name": "Update_name",
            "description": "Update_description",
            "price": 5555,

        }

    def test_service_update(self) -> None:
        response = self.client.post(reverse(
            'services:service_update',
            kwargs={'pk': 1}),
            self.data
        )
        queryset = Service.objects.get(name=self.data["name"])
        serializers_data = ServiceSerializers(queryset).data
        self.assertEqual(serializers_data["name"], self.data["name"])
        self.assertEqual(serializers_data["description"], self.data["description"])
        self.assertRedirects(response, reverse(
            'services:service_details',
            kwargs={'pk': 1}),
                             )

    def test_service_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'services:service_update',
            kwargs={'pk': 1}),
            self.data
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ServiceDeleteViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

    def test_service_delete(self) -> None:
        response = self.client.post(reverse(
            'services:service_archived',
            kwargs={'pk': 1}),
        )
        self.assertFalse(Service.objects.filter(id=1).exists())
        self.assertRedirects(response, reverse('services:service_list'))

    def test_service_delete_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'services:service_archived',
            kwargs={'pk': 1}),
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ServiceViewSetTestCase(APITestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self):
        user = User.objects.get(id=4)
        self.client.force_authenticate(user=user)

    def test_list(self):
        response = self.client.get(reverse("services-list"))
        queryset = Service.objects.get(id=1)
        serializers_data = ServiceSerializers([queryset], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], serializers_data)

    def test_list_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse("services-list"))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create(self):
        response = self.client.post(reverse(
            'services-list'),
            DATA,
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        queryset = Service.objects.get(name=DATA["name"])
        self.assertEqual(queryset.description, DATA["description"])
        self.assertEqual(queryset.price, DATA["price"])

    def test_create_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'services-list'),
            DATA,
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_detail(self):
        response = self.client.get(reverse(
            "services-detail",
            kwargs={'pk': 1})
        )
        queryset = Service.objects.get(id=1)
        serializers_data = ServiceSerializers(queryset).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializers_data)

    def test_detail_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse(
            "services-detail",
            kwargs={'pk': 1})
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update(self):
        data = {
            "name": "UpdateAPI_name",
            "description": "UpdateAPI_description",
            "price": 7887.00,
        }
        response = self.client.put(reverse(
            "services-detail",
            kwargs={'pk': 1}),
            data=data
        )
        queryset = Service.objects.get(id=1)
        serializers_data = ServiceSerializers(queryset).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializers_data)

    def test_update_not_auth(self) -> None:
        self.client.logout()
        data = {
            "name": "UpdateAPI_name",
            "description": "UpdateAPI_description",
            "price": 7887.00,
        }
        response = self.client.put(reverse(
            "services-detail",
            kwargs={'pk': 1}),
            data=data
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_delete(self):
        response = self.client.delete(reverse(
            "services-detail",
            kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Service.objects.filter(id=1).exists())

    def test_delete_not_auth(self) -> None:
        self.client.logout()
        response = self.client.delete(reverse(
            "services-detail",
            kwargs={'pk': 1}),
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
