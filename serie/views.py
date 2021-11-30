from django.shortcuts import redirect, render
from . models import Anime, Comentario, Episodio
from datetime import date


def index(request):
    try:
        animeSelecionados = Anime.objects.filter(categoria = "Aventura") 
    except Anime.DoesNotExist:
        animeSelecionados = None
    return render(request, 'serie/principal.html',{'animes':animeSelecionados})





def listagem(request):
    animes = Anime.objects.raw('SELECT * FROM serie_Anime ORDER BY titulo')
    return render(request, 'serie/listagem.html',{'animes':animes})





def anime(request, anime_id):
    anime = Anime.objects.get(id = anime_id)
    comentarios = Comentario.objects.filter(anime_id = anime_id)
    episodios = Episodio.objects.filter(animeEpisodio_id = anime_id)
    if request.method != 'POST':
        return render(request, 'serie/anime.html', {'anime':anime, 'episodios':episodios, 'comentarios':comentarios})


    comentario = request.POST.get("comentario")
    nota = request.POST.get("nota")


    #Verificando se os campos não estão vazios antes de serem enviados
    if comentario == None or nota == None or comentario == "" or comentario == " ":
        return render(request, 'serie/anime.html', {'anime':anime, 'episodios':episodios, 'comentarios':comentarios})


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


    #Script for itens NULL
    if titulo == None or data == None or categoria == None or descricao == None or descricao == "" or descricao == " " or titulo =="" or titulo == " ":
        return render(request, 'serie/cadastrar_anime.html')


    #Script consult "titulo"
    try:
        tituloConsulta = Anime.objects.get(titulo = titulo)
    except Anime.DoesNotExist:
        tituloConsulta = False

    if tituloConsulta:
        return render(request, 'serie/cadastrar_anime.html')


    #Script convert date
    dataValida = str(data)
    dataValida = dataValida.split("-")
    dataToday = str(date.today())
    dataToday = (dataToday).split("-")

    dataValida = int("".join(dataValida))
    dataToday = int("".join(dataToday))

    if dataValida >= dataToday:
        return render(request, 'serie/cadastrar_anime.html')

    
    #Create Elements
    anime = Anime(titulo = titulo, data_lancamento = data, categoria = categoria, descricao = descricao)
    anime.save()

    return redirect('listagem')


    


def cadastrarEpisodio(request):


    todosAnimes = Anime.objects.all()


    if request.method != 'POST':
        return render(request, 'serie/cadastrar_episodio.html' ,{'todosAnimes':todosAnimes})
    

    nome = request.POST.get("nome")
    numeroEpisodio = int(request.POST.get("numeroEpisodio"))
    animeEpisodio = request.POST.get("animeEpisodio")
    video = request.POST.get("video")


    #Taking the object from the varieble(str) 'animeEpisodio'
    try:
        objeto = Anime.objects.get(titulo = animeEpisodio)
    except Anime.DoesNotExist:
        return render(request, 'serie/cadastrar_episodio.html', {'todosAnimes':todosAnimes})


    #Script for itens NULL
    if nome == None or numeroEpisodio == None or animeEpisodio == None or video == None or nome == "" or nome == " ":
        return render(request, 'serie/cadastrar_episodio.html', {'todosAnimes':todosAnimes})


    #verificar se o número do episódio é menor do que 0
    if numeroEpisodio <= 0:
        return render(request, 'serie/cadastrar_episodio.html', {'todosAnimes':todosAnimes})


    #Script for consults if "Episódio" exists
    try:
        episodioConsulta = Episodio.objects.get(numeroEpisodio = numeroEpisodio, animeEpisodio = objeto)
    except Episodio.DoesNotExist:
        episodioConsulta = False
    
    if episodioConsulta:
        return render(request, 'serie/cadastrar_episodio.html', {'todosAnimes':todosAnimes})


    #Create Elements
    numeroEpisodio = str(numeroEpisodio)
    episodio = Episodio(nome = nome, numeroEpisodio = numeroEpisodio, video = video, animeEpisodio = objeto)
    episodio.save()


    return redirect('listagem')





def episodio(request, episodio_id):
    episodio = Episodio.objects.get(id = episodio_id)
    episodios = Episodio.objects.filter(animeEpisodio_id = episodio_id)
    return render(request, 'serie/episodio.html', {'episodio':episodio,'episodios':episodios})


