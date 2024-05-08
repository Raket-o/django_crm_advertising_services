from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import AdvertisingCompany
from .serializers import AdvertisingCompanySerializers


DATA = {
    "name": "AdvertisingCompanyTest",
    "description": "AdvertisingCompanyTest",
    "promotion": "TV",
    "services": 1,
    "budget": 7777.00,
}


class AdvertisingCompanyListViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

    def test_advertising_company_list(self) -> None:
        response = self.client.get(reverse('advertising_companies:advertising_companies_list'))
        self.assertQuerysetEqual(
            qs=AdvertisingCompany.objects.all(),
            values=(adv.pk for adv in response.context["object_list"]),
            transform=lambda adv: adv.pk
        )

    def test_advertising_company_list_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse('advertising_companies:advertising_companies_list'))
        self.assertEqual(302, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class AdvertisingCompanyDetailViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

    def test_advertising_company_details(self) -> None:
        response = self.client.get(reverse(
            'advertising_companies:advertising_company_details',
            kwargs={'pk': 1})
        )
        response_data = response.context['object']

        queryset = AdvertisingCompany.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, queryset)

    def test_advertising_company_details_not_auth(self) -> None:
        self.client.logout()

        response = self.client.get(reverse(
            'advertising_companies:advertising_company_details',
            kwargs={'pk': 1})
        )

        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class AdvertisingCompanyCreateViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

    def test_advertising_company_create(self) -> None:
        response = self.client.post(reverse(
            'advertising_companies:advertising_company_create'),
            DATA,
        )

        queryset = AdvertisingCompany.objects.get(name=DATA["name"])
        serializers_data = AdvertisingCompanySerializers(queryset).data

        self.assertEqual(serializers_data["name"], DATA["name"])
        self.assertEqual(serializers_data["description"], DATA["description"])
        self.assertRedirects(response, reverse('advertising_companies:advertising_companies_list'))

    def test_advertising_company_create_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'advertising_companies:advertising_company_create'),
            DATA,
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class AdvertisingCompanyUpdateViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

        self.data = {
            "name": "Update_name",
            "description": "Update_description",
            "promotion": "Update_promotion",
            "services": 1,
            "budget": 7777.00,
        }

    def test_advertising_company_update(self) -> None:
        response = self.client.post(reverse(
            'advertising_companies:advertising_company_update',
            kwargs={'pk': 1}),
            self.data
        )

        queryset = AdvertisingCompany.objects.get(name=self.data["name"])
        self.assertEqual(queryset.name, self.data["name"])

        self.assertRedirects(response, reverse(
            'advertising_companies:advertising_company_details',
            kwargs={'pk': 1}),
                             )

    def test_advertising_company_update_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'advertising_companies:advertising_company_update',
            kwargs={'pk': 1}),
            self.data
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class AdvertisingCompanyDeleteViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=4)
        self.client.force_login(user)

    def test_advertising_company_delete(self) -> None:
        response = self.client.post(reverse(
            'advertising_companies:advertising_company_archived',
            kwargs={'pk': 1}),
        )

        self.assertFalse(AdvertisingCompany.objects.filter(id=1).exists())
        self.assertRedirects(response, reverse('advertising_companies:advertising_companies_list'))

    def test_advertising_company_delete_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'advertising_companies:advertising_company_archived',
            kwargs={'pk': 1}),
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class AdvertisingCompanyViewSetTestCase(APITestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self):
        user = User.objects.get(id=4)
        self.client.force_authenticate(user=user)

    def test_list(self):
        response = self.client.get(reverse("advertising_companies-list"))
        queryset = AdvertisingCompany.objects.get(id=1)
        serializers_data = AdvertisingCompanySerializers([queryset], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], serializers_data)

    def test_list_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse("advertising_companies-list"))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create(self):
        response = self.client.post(reverse(
            'advertising_companies-list'),
            DATA,
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        queryset = AdvertisingCompany.objects.get(name=DATA["name"])
        self.assertEqual(queryset.description, DATA["description"])
        self.assertEqual(queryset.promotion, DATA["promotion"])
        self.assertEqual(queryset.budget, DATA["budget"])

    def test_create_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'advertising_companies-list'),
            DATA,
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_detail(self):
        response = self.client.get(reverse(
            "advertising_companies-detail",
            kwargs={'pk': 1})
        )

        queryset = AdvertisingCompany.objects.get(id=1)
        serializers_data = AdvertisingCompanySerializers(queryset).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializers_data)

    def test_detail_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'advertising_companies-list'),
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update(self):
        data = {
            "name": "UpdateAPI_name",
            "description": "UpdateAPI_description",
            "promotion": "UpdateAPI_promotion",
            "services": 1,
            "budget": 7887.00,
        }

        response = self.client.put(reverse(
            "advertising_companies-detail",
            kwargs={'pk': 1}),
            data=data
        )

        queryset = AdvertisingCompany.objects.get(id=1)
        serializers_data = AdvertisingCompanySerializers(queryset).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializers_data)

    def test_update_not_auth(self) -> None:
        self.client.logout()
        response = self.client.put(reverse(
            "advertising_companies-detail",
            kwargs={'pk': 1}),
            data=DATA
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_delete(self):
        response = self.client.delete(reverse(
            "advertising_companies-detail",
            kwargs={'pk': 1}),
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AdvertisingCompany.objects.filter(id=1).exists())

    def test_delete_not_auth(self) -> None:
        self.client.logout()
        response = self.client.delete(reverse(
            "advertising_companies-detail",
            kwargs={'pk': 1}),
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
