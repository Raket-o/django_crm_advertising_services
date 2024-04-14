from decimal import Decimal

from django.db import connection
from django.shortcuts import render
from django.views.generic.base import View

from advertising_companies.models import AdvertisingCompany
from clients.models import Client
from contracts.models import Contract
from services.models import Service


class CustomerStatistics(View):
    def get(self, request):
        sql_query = """
        SELECT aca.name, aca.budget, services_service.price, cc.active, c.amount, (c.amount-(aca.budget+services_service.price))
        FROM services_service
        JOIN public.advertising_companies_advertisingcompany aca ON services_service.id = aca.services_id
        JOIN public.clients_client cc ON aca.id = cc.advertising_company_id
        LEFT JOIN public.contracts_contract c ON cc.contract_id = c.id;
        """

        res_dict = dict()
        res_list = []

        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()

            company_data = {}

            for result in results:
                company = result[0]
                active_client = result[3]
                profit = result[5] if isinstance(result[5], Decimal) else 0
                if company not in company_data:
                    company_data[company] = {'active': 0, 'potential': 0, 'profit': 0}

                company_data[company]['active'] += int(active_client)
                company_data[company]['potential'] += int(not active_client)
                company_data[company]['profit'] += float(profit)

        content = {"content": company_data}
        return render(request=request,
                      template_name="customer_statistics/statistics.html",
                      context=content)
