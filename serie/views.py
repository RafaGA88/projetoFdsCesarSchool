from django.shortcuts import redirect, render
from . models import Anime, Comentario, Episodio


def index(request):
    animeSelecionados = Anime.objects.raw('SELECT * FROM serie_Anime WHERE titulo = "Naruto"')
    return render(request, 'serie/principal.html',{'animes':animeSelecionados})

def listagem(request):
    animes = Anime.objects.raw('SELECT * FROM serie_Anime ORDER BY titulo')
    return render(request, 'serie/listagem.html',{'animes':animes})

def anime(request, anime_id):
    anime = Anime.objects.get(id = anime_id)
    episodios = Episodio.objects.raw(f'SELECT * FROM serie_Episodio WHERE animeEpisodio_id = {anime_id} ORDER BY numeroEpisodio')
    comentarios = Comentario.objects.raw(f'SELECT * FROM serie_comentario WHERE anime_id = {anime_id}')

    if request.method != 'POST':
        return render(request, 'serie/anime.html', {'anime':anime, 'episodios':episodios, 'comentarios':comentarios})


    comentario = request.POST.get("comentario")
    nota = request.POST.get("nota")

    comentario = Comentario(review = comentario, rate = nota, anime = anime)
    comentario.save()

    return render(request, 'serie/anime.html', {'anime':anime, 'episodios':episodios, 'comentarios':comentarios})

def cadastrarAnime(request):
    if request.method != "POST":    
        return render(request, 'serie/cadastrar_anime.html')
    
    titulo = request.POST.get("nome")
    data = request.POST.get("data")
    categoria = request.POST.get("categoria")
    descricao = request.POST.get("descricao")

    tituloConsulta = Anime.objects.raw(f"SELECT titulo FROM serie_anime WHERE titulo = {titulo}")

    print("\n\n\n\n\n\n\n\n\n",titulo,"\n\n\n\n\n\n\n\n", tituloConsulta)

    if titulo == tituloConsulta:
        return render(request, 'serie/cadastrar_anime.html')
    
    anime = Anime(titulo = titulo, data_lancamento = data, categoria = categoria, descricao = descricao)
    anime.save()

    return redirect('listagem')

def cadastrarEpisodio(request):

    if request.method != 'POST':
        return render(request, 'serie/cadastrar_episodio.html')
    
    nome = request.POST.get("nome")
    numeroEpisodio = request.POST.get("numeroEpisodio")
    animeEpisodio = request.POST.get("animeEpisodio")
    video = request.POST.get("video")

    animeConsultado = Anime.objects.get(id = animeEpisodio)

    episodio = Episodio(nome = nome, numeroEpisodio = numeroEpisodio, video = video, animeEpisodio = animeConsultado, fillerOuCanon = True)
    episodio.save()



    return render(request, 'serie/cadastrar_episodio.html')

def episodio(request, episodio_id):
    episodio = Episodio.objects.get(id = episodio_id)
    episodios = Episodio.objects.raw(f'SELECT * FROM serie_Episodio WHERE animeEpisodio_id = {episodio_id} ORDER BY numeroEpisodio')
    return render(request, 'serie/episodio.html', {'episodio':episodio,'episodios':episodios})


