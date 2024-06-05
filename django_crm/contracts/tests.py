from os import path

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Contract
from .serializers import ContractSerializers

DATA = {
    "name": "contract_test",
    "service": 1,
    "date_conclusion": "2024-04-30T00:00:00Z",
    "period_validity": "2 year",
    "amount": 10000,
}


class ContractListViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=3)
        self.client.force_login(user)

    def test_contract_list(self) -> None:
        response = self.client.get(reverse('contracts:contract_list'))
        self.assertQuerysetEqual(
            qs=Contract.objects.all(),
            values=(contract.pk for contract in response.context["object_list"]),
            transform=lambda contract: contract.pk
        )

    def test_contract_list_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse('contracts:contract_list'))
        self.assertEqual(302, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ContractDetailViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=3)
        self.client.force_login(user)

    def test_contract_details(self) -> None:
        response = self.client.get(reverse(
            'contracts:contract_details',
            kwargs={'pk': 1})
        )
        response_data = response.context['object']
        queryset = Contract.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, queryset)

    def test_contract_details_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse(
            'contracts:contract_details',
            kwargs={'pk': 1})
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ContractCreateViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=3)
        self.client.force_login(user)
        file_name = "test_contract.txt"
        abs_path_file = path.join(settings.BASE_DIR, "django_crm", "fixtures", file_name)
        self.files = {"file": (file_name, open(abs_path_file, "r"))}

    def test_contract_create(self) -> None:
        response = self.client.post(reverse(
            'contracts:contract_create'),
            DATA,
            files=self.files,
        )
        queryset = Contract.objects.get(name=DATA["name"])
        serializers_data = ContractSerializers(queryset).data
        self.assertEqual(serializers_data["name"], DATA["name"])
        self.assertEqual(serializers_data["date_conclusion"], DATA["date_conclusion"])
        self.assertEqual(serializers_data["period_validity"], DATA["period_validity"])
        self.assertRedirects(response, reverse('contracts:contract_list'))

    def test_contract_create_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'contracts:contract_create'),
            DATA,
            files=self.files,
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ContractUpdateViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=3)
        self.client.force_login(user)
        file_name = "test_contract.txt"
        abs_path_file = path.join(settings.BASE_DIR, "django_crm", "fixtures", file_name)
        self.files = {"file": (file_name, open(abs_path_file, "r"))}

        self.data = {
            "name": "contract_test_update",
            "service": 1,
            "date_conclusion": "2024-10-30T00:00:00Z",
            "period_validity": "3 year",
            "amount": "11000",
        }

    def test_advertising_company_update(self) -> None:
        response = self.client.post(reverse(
            'contracts:contract_update',
            kwargs={'pk': 1}),
            self.data,
            files=self.files,
        )
        queryset = Contract.objects.get(name=self.data["name"])
        self.assertEqual(queryset.name, self.data["name"])
        self.assertRedirects(response, reverse(
            'contracts:contract_details',
            kwargs={'pk': 1}),
                             )

    def test_contract_update_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'contracts:contract_update',
            kwargs={'pk': 1}),
            self.data
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ContractDeleteViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=3)
        self.client.force_login(user)

    def test_contract_delete(self) -> None:
        response = self.client.post(reverse(
            'contracts:contract_archived',
            kwargs={'pk': 1}),
        )
        self.assertFalse(Contract.objects.filter(id=1).exists())
        self.assertRedirects(response, reverse('contracts:contract_list'))

    def test_contract_delete_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'contracts:contract_archived',
            kwargs={'pk': 1}),
        )
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ContractViewSetTestCase(APITestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self):
        user = User.objects.get(id=3)
        self.client.force_authenticate(user=user)

    def test_list(self):
        response = self.client.get(reverse("contracts-list"))
        queryset = Contract.objects.get(id=1)
        serializers_data = ContractSerializers(queryset).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["name"], serializers_data["name"])

    def test_list_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse("contracts-list"))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create(self):
        response = self.client.post(reverse(
            'contracts-list'),
            DATA,
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        queryset = Contract.objects.get(name=DATA["name"])
        self.assertEqual(queryset.period_validity, DATA["period_validity"])
        self.assertEqual(queryset.amount, DATA["amount"])

    def test_create_not_auth(self) -> None:
        self.client.logout()
        response = self.client.post(reverse(
            'contracts-list'),
            DATA,
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_detail(self):
        response = self.client.get(reverse(
            "contracts-detail",
            kwargs={'pk': 1})
        )
        queryset = Contract.objects.get(id=1)
        serializers_data = ContractSerializers(queryset).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], serializers_data["name"])

    def test_detail_not_auth(self) -> None:
        self.client.logout()
        response = self.client.get(reverse(
            "contracts-detail",
            kwargs={'pk': 1})
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update(self):
        data = {
            "name": "UpdateAPI_name",
            "service": 1,
            "date_conclusion": "2024-10-30T00:00:00Z",
            "period_validity": "3 year",
            "amount": 15000.00,

        }
        response = self.client.put(reverse(
            "contracts-detail",
            kwargs={'pk': 1}),
            data=data
        )
        queryset = Contract.objects.get(id=1)
        serializers_data = ContractSerializers(queryset).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], serializers_data["name"])

    def test_update_not_auth(self) -> None:
        self.client.logout()
        response = self.client.put(reverse(
            "contracts-detail",
            kwargs={'pk': 1}),
            data=DATA
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_delete(self):
        response = self.client.delete(reverse(
            "contracts-detail",
            kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Contract.objects.filter(id=1).exists())

    def test_delete_not_auth(self) -> None:
        self.client.logout()
        response = self.client.delete(reverse(
            "contracts-detail",
            kwargs={'pk': 1}),
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
