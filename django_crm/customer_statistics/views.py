from decimal import Decimal

from django.db import connection
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import UserPassesTestMixin


from advertising_companies.models import AdvertisingCompany
from clients.models import Client
from contracts.models import Contract
from services.models import Service


class CustomerStatistics(UserPassesTestMixin, View):
    def get(self, request):
        sql_query = """
SELECT aca.name, aca.budget, service.price, client.active, contract.amount, (contract.amount-(aca.budget+service.price))
FROM advertising_companies_advertisingcompany as aca
JOIN public.services_service service on service.id = aca.services_id
LEFT JOIN public.clients_client client on aca.id = client.advertising_company_id
LEFT OUTER JOIN  public.contracts_contract contract on contract.id = client.contract_id
        """

        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()

            company_data = {}

            for result in results:
                company = result[0]
                active_client = result[3] if isinstance(result[3], bool) else None
                profit = result[5] if isinstance(result[5], Decimal) else False
                if company not in company_data:
                    company_data[company] = {'active': 0, 'potential': 0, 'profit': 0}

                try:
                    company_data[company]['active'] += int(active_client)
                    company_data[company]['potential'] += int(not active_client)
                    company_data[company]['profit'] += float(profit)
                except TypeError:
                    pass

        content = {"content": company_data}
        print(content)
        return render(request=request,
                      template_name="customer_statistics/statistics.html",
                      context=content)

    def test_func(self):
        user = self.request.user
        return user.is_authenticated
