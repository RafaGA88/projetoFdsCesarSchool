from django.test import TestCase
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
        self.assertEquals(a1.__str__(), "")


