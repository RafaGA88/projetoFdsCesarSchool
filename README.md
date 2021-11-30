## `Projeto de Fundamento e Desenvolvimento de Software - Cesar SCHOOL`
Projeto da Cesar SCHOOL feito por alunos do 1/2 Período


### `6 integrantes de Ciência da Computação:`
  Rafael Ghinato Albuquerque (rga@cesar.school);\
  Israel Erlich Terceiro Neto (Ietn@cesar.school);\
  Rennan Pontes Cardoso (rpc@cesar.school);\
  João Augusto Pimentel de Melo (japm@cesar.school);\
  
### `Orientador/Professor:`
  Ricardo Araujo Costa - Engenheiro de Software e Doutor em Ciência da Computação UFPE
  
  
### `Proposta do projeto:`
  Plataforma Web de Animes
  
  
  
### `Montagem de Ambiente`
  
  Ao baixar o conteúdo instale as seguintes bibliotecas:\
  
  `pip install ... (códigos abaixo)`
  
  asgiref==3.4.1\
  Django==3.2.9\
  django-environ==0.8.1\
  pytz==2021.3\
  sqlparse==0.4.2\
  whitenoise==5.3.0
  
### `Rodar o ambiente em servidor local:`
 
 `python3 manage.py runserver`
 
### `Informações sobre a documentação:`
  
  `Dentro da pasta 'serie' temos os principais arquivos de configurações, contendo todas as urls, views e modelos`
   
  urls - Todas as urls do projeto\
  views - Todas as views do projeto, que executam as funcionalidades e renderizam os templates\
  models - Todos os modelos de dados: Anime, Episodio e Comentario\
  
  `Dentro da pasta 'serie/templates' temos todos os arquivos HTML referente a cada url`
  
  `Dentro da pasta 'tests' contém todos os testes unitários: das views e dos models`
   
  `Os demais arquivos são de configurações do Django, Integração Contínua e Deploy Automático Heroku`
  
  
  
 
  
