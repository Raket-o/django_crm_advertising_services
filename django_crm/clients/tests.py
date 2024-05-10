from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Client
from .serializers import ClientSerializers


DATA = {
    "name": "ClientTest",
    "phone": "1234567890",
    "email": "email@test.ru",
    "advertising_company": 1,

}
# name = models.CharField(max_length=50, blank=False, unique=True)
# phone = models.CharField(max_length=10, blank=False)
# email = models.EmailField(blank=True)
# active = models.BooleanField(default=False)
# advertising_company = models.ForeignKey(AdvertisingCompany, on_delete=models.CASCADE, null=True)
# contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, default=None)


# class ClientListViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=5)
#         self.client.force_login(user)
#
#     def test_client_list(self) -> None:
#         response = self.client.get(reverse('clients:client_list'))
#         self.assertQuerysetEqual(
#             qs=Client.objects.filter(active=False),
#             values=(client.pk for client in response.context["object_list"]),
#             transform=lambda client: client.pk
#         )
#
#     def test_client_list_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.get(reverse('clients:client_list'))
#         self.assertEqual(302, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ClientDetailViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=5)
#         self.client.force_login(user)
#
#     def test_client_details(self) -> None:
#         response = self.client.get(reverse(
#             'clients:client_details',
#             kwargs={'pk': 8})
#         )
#         response_data = response.context['object']
#         queryset = Client.objects.get(id=8)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response_data, queryset)
#
#     def test_client_details_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.get(reverse(
#             'clients:client_details',
#             kwargs={'pk': 8})
#         )
#         self.assertEqual(status.HTTP_302_FOUND, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ClientCreateViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=5)
#         self.client.force_login(user)
#
#     def test_client_create(self) -> None:
#         response = self.client.post(reverse(
#             'clients:client_create'),
#             DATA,
#         )
#         queryset = Client.objects.get(name=DATA["name"])
#         serializers_data = ClientSerializers(queryset).data
#         self.assertEqual(serializers_data["name"], DATA["name"])
#         self.assertEqual(serializers_data["phone"], DATA["phone"])
#         self.assertEqual(serializers_data["email"], DATA["email"])
#         self.assertEqual(serializers_data["advertising_company"], DATA["advertising_company"])
#
#     def test_client_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.post(reverse(
#             'clients:client_create'),
#             DATA,
#         )
#         self.assertEqual(status.HTTP_302_FOUND, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ClientUpdateViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=5)
#         self.client.force_login(user)
#         self.data = {
#             "id":8,
#             "name": "Update_name",
#             "phone": 2222222222,
#             "email": "Update_email@test.ru",
#             "advertising_company": 1,
#         }
#
#     def test_client_update(self) -> None:
#         response = self.client.post(reverse(
#             'clients:client_update',
#             kwargs={'pk': 8}),
#             self.data
#         )
#         queryset = Client.objects.get(name=self.data["name"])
#         self.assertEqual(queryset.name, self.data["name"])
#         self.assertRedirects(response, reverse(
#             'clients:client_details',
#             kwargs={'pk': 8}),
#                              )
#
#     def test_client_update_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.post(reverse(
#             'clients:client_update',
#             kwargs={'pk': 8}),
#             self.data
#         )
#         self.assertEqual(status.HTTP_302_FOUND, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ClientDeleteViewTestCase(TestCase):
#     fixtures = [
#         'django_crm/fixtures/db_dump_v3.json',
#     ]
#
#     def setUp(self) -> None:
#         user = User.objects.get(id=5)
#         self.client.force_login(user)
#
#     def test_client_delete(self) -> None:
#         response = self.client.post(reverse(
#             'clients:client_archived',
#             kwargs={'pk': 8}),
#         )
#         self.assertFalse(Client.objects.filter(id=8).exists())
#         self.assertRedirects(response, reverse('clients:client_list'))
#
#     def test_client_delete_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.post(reverse(
#             'clients:client_archived',
#             kwargs={'pk': 8}),
#         )
#         self.assertEqual(status.HTTP_302_FOUND, response.status_code)
#         self.assertIn(str(settings.LOGIN_URL), response.url)


class ClientViewSetTestCase(APITestCase):
    fixtures = [
        'django_crm/fixtures/db_dump_v3.json',
    ]

    def setUp(self):
        user = User.objects.get(id=5)
        self.client.force_authenticate(user=user)

    def test_list(self):
        response = self.client.get(reverse("clients-list"))
        print(response.__dict__)

        queryset = Client.objects.filter(active=False)
        for i in queryset:
            print(i.__dict__)
        serializers_data = ClientSerializers(queryset[0]).data
        print(serializers_data)

        # serializers_data = ClientSerializers([queryset], many=True).data
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data["results"], serializers_data)
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
#         queryset = Client.objects.get(name=DATA["name"])
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
#         queryset = Client.objects.get(id=1)
#         serializers_data = ClientSerializers(queryset).data
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
#         queryset = Client.objects.get(id=1)
#         serializers_data = ClientSerializers(queryset).data
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
#         self.assertFalse(Client.objects.filter(id=1).exists())
#
#     def test_delete_not_auth(self) -> None:
#         self.client.logout()
#         response = self.client.delete(reverse(
#             "advertising_companies-detail",
#             kwargs={'pk': 1}),
#         )
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
