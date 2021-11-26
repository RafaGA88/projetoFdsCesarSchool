from datetime import date
from django.test import TestCase

from serie.views import anime
from ..models import Anime, Episodio, Comentario

class AnimeTestCase(TestCase):

    def setUp(self):
        Anime.objects.create(
            titulo = 'Naruto',
            data_lancamento = '2020-06-30',
            descricao = "Naruto é um jovem órfão habitante da Vila da Folha que sonha se tornar o quinto Hokage, o maior guerreiro e governante da vila. ... Agora Naruto vai contar com a ajuda dos colegas Sakura e Sasuke e do professor dos três, Kakashi Hatake, para perseguir seu sonho e deter os ninjas que planejam fazer mal á sua cidade.",
            categoria = "Romance"
        )
    
    def test_retorno_str(self):
        a1 = Anime.objects.get(titulo = "Naruto")
        self.assertEquals(a1.__str__(), "Naruto")
    

    def test_retorna_TituloIsString(self):
        a1 = Anime.objects.get(titulo = "Naruto")
        self.assertEquals(isinstance(a1.titulo, str) ,True)
    
    
    def test_retorna_DescricaoIsString(self):
        a1 = Anime.objects.get(descricao = "Naruto é um jovem órfão habitante da Vila da Folha que sonha se tornar o quinto Hokage, o maior guerreiro e governante da vila. ... Agora Naruto vai contar com a ajuda dos colegas Sakura e Sasuke e do professor dos três, Kakashi Hatake, para perseguir seu sonho e deter os ninjas que planejam fazer mal á sua cidade.")
        self.assertEquals(isinstance(a1.descricao, str) ,True)
    

    def test_retorna_DataIsDate(self):
        a1 = Anime.objects.get(data_lancamento = '2020-06-30')
        self.assertEquals(isinstance(a1.data_lancamento, date) ,True)
    

    def test_retorna_CategoriaIsString(self):
        a1 = Anime.objects.get(categoria = "Romance")
        self.assertEquals(isinstance(a1.categoria, str) ,True)
    
class EpisodioTestCase(TestCase):

    def setUp(self):

        anime = Anime(titulo = "Naruto", data_lancamento = '2020-06-30',  descricao = "Naruto é um jovem órfão habitante da Vila da Folha que sonha se tornar o quinto Hokage, o maior guerreiro e governante da vila. ... Agora Naruto vai contar com a ajuda dos colegas Sakura e Sasuke e do professor dos três, Kakashi Hatake, para perseguir seu sonho e deter os ninjas que planejam fazer mal á sua cidade.", categoria = "Romance")
        anime.save()

        Episodio.objects.create(
            nome = "Uma viagem até o fim do tunel",
            numeroEpisodio = 2,
            video = "",
            animeEpisodio = anime
        )
 
    def test_retorno_str(self):
        a1 = Episodio.objects.get(nome = "Uma viagem até o fim do tunel")
        self.assertEquals(a1.__str__(), "Uma viagem até o fim do tunel")
    
    def test_retorna_NomeIsString(self):
        a1 = Episodio.objects.get(nome = "Uma viagem até o fim do tunel")
        self.assertEquals(isinstance(a1.nome, str) ,True)
    
    def test_retorna_NumeroEpisodioIsInt(self):
        a1 = Episodio.objects.get(numeroEpisodio = 2)
        self.assertEquals(isinstance(a1.numeroEpisodio, int) ,True)
    
    def test_retorna_AnimeEpisodioIsObject(self):
        a1 = Episodio.objects.get(animeEpisodio = 1)
        self.assertEquals(isinstance(a1.animeEpisodio, object) ,True)

class ComentarioTestCase(TestCase):

    def setUp(self):

        anime = Anime(titulo = "Naruto", data_lancamento = '2020-06-30',  descricao = "Naruto é um jovem órfão habitante da Vila da Folha que sonha se tornar o quinto Hokage, o maior guerreiro e governante da vila. ... Agora Naruto vai contar com a ajuda dos colegas Sakura e Sasuke e do professor dos três, Kakashi Hatake, para perseguir seu sonho e deter os ninjas que planejam fazer mal á sua cidade.", categoria = "Romance")
        anime.save()

        Comentario.objects.create(
            rate = 1,
            review = "Anime muito show de bola",
            anime = anime 
        )

    def test_retorna_RateIsInt(self):
        a1 = Comentario.objects.get(rate = 1)
        self.assertEquals(isinstance(a1.rate, int) ,True)
    
    def test_retorna_ReviewIsString(self):
        a1 = Comentario.objects.get(review = "Anime muito show de bola")
        self.assertEquals(isinstance(a1.review, str) ,True)

    def test_retorna_AnimeIsObject(self):
        a1 = Comentario.objects.get(anime = 1)
        self.assertEquals(isinstance(a1.anime, object) ,True)