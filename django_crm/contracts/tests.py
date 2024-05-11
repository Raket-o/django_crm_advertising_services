from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Contract
from .serializers import ContractSerializers


# DATA = {
#     "name": "contract_test",
#     "service": 1,
#     "document_file": "contracts/contracts/requirements.txt",
#     "date_conclusion": "2024-04-30T00:00:00Z",
#     "period_validity": "2 year",
#     "amount": "10000.00",
# }

DATA ={"name": "contract1",
 "service": 1,
 "document_file": "contracts/contracts/requirements.txt",
 "date_conclusion": "2024-04-30T00:00:00Z",
 "period_validity": "2 year",
 "amount": "50000.00"}

# class ContractListViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=3)
#         self.client.force_login(user)
#
#     def test_contract_list(self) -> None:
#         response = self.client.get(reverse('contracts:contract_list'))
#         self.assertQuerysetEqual(
#             qs=Contract.objects.all(),
#             values=(contract.pk for contract in response.context["object_list"]),
#             transform=lambda contract: contract.pk
#         )
#
#     def test_contract_list_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.get(reverse('contracts:contract_list'))
#         self.assertEqual(302, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ContractDetailViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=3)
#         self.client.force_login(user)
#
#     def test_contract_details(self) -> None:
#         response = self.client.get(reverse(
#             'contracts:contract_details',
#             kwargs={'pk': 1})
#         )
#         response_data = response.context['object']
#         queryset = Contract.objects.get(id=1)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response_data, queryset)
#
#     def test_contract_details_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.get(reverse(
#             'contracts:contract_details',
#             kwargs={'pk': 1})
#         )
#         self.assertEqual(status.HTTP_302_FOUND, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)


class ContractCreateViewTestCase(TestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self) -> None:
        user = User.objects.get(id=3)
        self.client.force_login(user)

    def test_contract_create(self) -> None:
        response = self.client.post(reverse(
            'contracts:contract_create'),
            DATA,
        )
        print(response)

        # queryset = Contract.objects.get(name=DATA["name"])
        queryset = Contract.objects.all()
        print(queryset)
        # serializers_data = ContractSerializers(queryset).data
        # self.assertEqual(serializers_data["name"], DATA["name"])
        # self.assertEqual(serializers_data["date_conclusion"], DATA["date_conclusion"])
        # self.assertEqual(serializers_data["period_validity"], DATA["period_validity"])
        # self.assertEqual(serializers_data["amount"], DATA["amount"])
        # self.assertRedirects(response, reverse('contracts:contract_list'))
#
#     def test_contract_create_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.post(reverse(
#             'advertising_companies:advertising_company_create'),
#             DATA,
#         )
#         self.assertEqual(status.HTTP_302_FOUND, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ContractUpdateViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=4)
#         self.client.force_login(user)
#         self.data = {
#             "name": "Update_name",
#             "description": "Update_description",
#             "promotion": "Update_promotion",
#             "services": 1,
#             "budget": 7777.00,
#         }
#
#     def test_contract_update(self) -> None:
#         response = self.client.post(reverse(
#             'advertising_companies:advertising_company_update',
#             kwargs={'pk': 1}),
#             self.data
#         )
#         queryset = AdvertisingCompany.objects.get(name=self.data["name"])
#         self.assertEqual(queryset.name, self.data["name"])
#         self.assertRedirects(response, reverse(
#             'advertising_companies:advertising_company_details',
#             kwargs={'pk': 1}),
#                              )
#
#     def test_contract_update_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.post(reverse(
#             'advertising_companies:advertising_company_update',
#             kwargs={'pk': 1}),
#             self.data
#         )
#         self.assertEqual(status.HTTP_302_FOUND, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ContractDeleteViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=4)
#         self.client.force_login(user)
#
#     def test_contract_delete(self) -> None:
#         response = self.client.post(reverse(
#             'advertising_companies:advertising_company_archived',
#             kwargs={'pk': 1}),
#         )
#         self.assertFalse(AdvertisingCompany.objects.filter(id=1).exists())
#         self.assertRedirects(response, reverse('advertising_companies:advertising_companies_list'))
#
#     def test_contract_delete_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.post(reverse(
#             'advertising_companies:advertising_company_archived',
#             kwargs={'pk': 1}),
#         )
#         self.assertEqual(status.HTTP_302_FOUND, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ContractViewSetTestCase(APITestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self):
#         user = User.objects.get(id=4)
#         self.client.force_authenticate(user=user)
#
#     def test_list(self):
#         response = self.client.get(reverse("advertising_companies-list"))
#         queryset = AdvertisingCompany.objects.get(id=1)
#         serializers_data = AdvertisingCompanySerializers([queryset], many=True).data
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["results"], serializers_data)
#
#     def test_list_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.get(reverse("advertising_companies-list"))
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
#
#     def test_create(self):
#         response = self.client.post(reverse(
#             'advertising_companies-list'),
#             DATA,
#         )
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         queryset = AdvertisingCompany.objects.get(name=DATA["name"])
#         self.assertEqual(queryset.description, DATA["description"])
#         self.assertEqual(queryset.promotion, DATA["promotion"])
#         self.assertEqual(queryset.budget, DATA["budget"])
#
#     def test_create_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.post(reverse(
#             'advertising_companies-list'),
#             DATA,
#         )
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
#
#     def test_detail(self):
#         response = self.client.get(reverse(
#             "advertising_companies-detail",
#             kwargs={'pk': 1})
#         )
#         queryset = AdvertisingCompany.objects.get(id=1)
#         serializers_data = AdvertisingCompanySerializers(queryset).data
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializers_data)
#
#     def test_detail_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.post(reverse(
#             'advertising_companies-list'),
#         )
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
#
#     def test_update(self):
#         data = {
#             "name": "UpdateAPI_name",
#             "description": "UpdateAPI_description",
#             "promotion": "UpdateAPI_promotion",
#             "services": 1,
#             "budget": 7887.00,
#         }
#         response = self.client.put(reverse(
#             "advertising_companies-detail",
#             kwargs={'pk': 1}),
#             data=data
#         )
#         queryset = AdvertisingCompany.objects.get(id=1)
#         serializers_data = AdvertisingCompanySerializers(queryset).data
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializers_data)
#
#     def test_update_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.put(reverse(
#             "advertising_companies-detail",
#             kwargs={'pk': 1}),
#             data=DATA
#         )
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
#
#     def test_delete(self):
#         response = self.client.delete(reverse(
#             "advertising_companies-detail",
#             kwargs={'pk': 1}),
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(AdvertisingCompany.objects.filter(id=1).exists())
#
#     def test_delete_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.delete(reverse(
#             "advertising_companies-detail",
#             kwargs={'pk': 1}),
#         )
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
