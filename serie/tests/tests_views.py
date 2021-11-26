from django.http import response
from django.test import TestCase
from django.urls import reverse
from ..models import Anime, Episodio, Comentario

class viewPrincipalTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "serie/principal.html")


class viewListagemTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get('/listagem/')
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get("/listagem/")
        self.assertTemplateUsed(response, "serie/listagem.html")


class viewCadastrarAnimeTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get('/cadastrar_anime/')
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get("/cadastrar_anime/")
        self.assertTemplateUsed(response, "serie/cadastrar_anime.html")


class viewCadastrarEpisodioTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get('/cadastrar_episodio/')
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get("/cadastrar_episodio/")
        self.assertTemplateUsed(response, "serie/cadastrar_episodio.html")


class viewEpisodioTestCase(TestCase):
    def setUp(self):

        anime = Anime(titulo = "Naruto", data_lancamento = '2020-06-30',  descricao = "Naruto é um jovem órfão habitante da Vila da Folha que sonha se tornar o quinto Hokage, o maior guerreiro e governante da vila. ... Agora Naruto vai contar com a ajuda dos colegas Sakura e Sasuke e do professor dos três, Kakashi Hatake, para perseguir seu sonho e deter os ninjas que planejam fazer mal á sua cidade.", categoria = "Romance")
        anime.save()

        Episodio.objects.create(
            nome = "Uma viagem até o fim do tunel",
            numeroEpisodio = 2,
            video = "",
            animeEpisodio = anime
        )
    def test_status_code(self):
        response = self.client.get('/episodio/1')
        self.assertEquals(response.status_code, 200)
    
    def test_template_usado(self):
        response = self.client.get("/episodio/1")
        self.assertTemplateUsed(response, "serie/episodio.html")



class viewAnimeTestCase(TestCase):
    def setUp(self):
        Anime.objects.create(
            titulo = 'Naruto',
            data_lancamento = '2020-06-30',
            descricao = "Naruto é um jovem órfão habitante da Vila da Folha que sonha se tornar o quinto Hokage, o maior guerreiro e governante da vila. ... Agora Naruto vai contar com a ajuda dos colegas Sakura e Sasuke e do professor dos três, Kakashi Hatake, para perseguir seu sonho e deter os ninjas que planejam fazer mal á sua cidade.",
            categoria = "Romance"
        )
    def test_status_code(self):
        response = self.client.get('/anime/1')
        self.assertEquals(response.status_code, 200)
    
    def test_template_usado(self):
        response = self.client.get("/anime/1")
        self.assertTemplateUsed(response, "serie/anime.html")