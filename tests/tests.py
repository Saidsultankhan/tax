from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from taxing_rest.main.models import Company
import json


class CompanyApiTest(APITestCase):

    def test_get_company(self):
        url = '/api/v1/companylist'
        print(url)
        response = self.client.get(path=url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_companies(self):
        new_company = Company(
            name='Company_test',
            type_of_company=int('1'),
            not_paid=int('0'),
            has_fine=False,
            paid_before=True,
            for_militiary=False
        )
        print("add ok")
        new_company.save()

        def delete_all_companies():
            Company.objects.all().delete()

    def test_put_company(self):
        self.delete_all_companies()
        self.test_add_companies()
        id = Company.objects.get().id
        url = f"/api/v1/companylist/{id}"
        data = {
            "name": "Company_test",
            "type_of_company": int('1.00'),
            "not_paid": int('0'),
            "has_fine": False,
            'paid_before': True,
            "for_militiary": False,
        }
        response = self.client.put(path=url, data=json.dumps(data), content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
