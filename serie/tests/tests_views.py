from django.http import response
from django.test import TestCase
from django.urls import reverse

class viewPrincipalTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('principal'))
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get(reverse("principal"))
        self.assertTemplateUsed(response, "serie/principal.html")


class viewEpisodioTestCase(TestCase):
    pass
    # def test_status_code_200(self):
    #     response = self.client.get(reverse("episodio"))
    #     self.assertEquals(response.status_code, 200)