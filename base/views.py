from django.shortcuts import render, redirect
from base.forms import ContatoForm, ReservaForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# View inicio, que é a primeira a ser acessada pelo usuário
def inicio(request):
    return render(request, 'inicio.html')



# View contato
def contato(request):
    # Definir sucesso, para indicar se o envio da mensagem foi correto ou não
    sucesso = False

    if request.method == 'GET': # Se método da requisição é GET
        formulario = ContatoForm()
    # Método POST
    else:
        formulario = ContatoForm(request.POST)
        if formulario.is_valid(): # Verificar se form é válido
            sucesso = True
            formulario.save() # Salvar no banco de dados
    
    # Outra forma de verificar se é Get ou Post
    '''
    formulario = ContatoForm(request.POST or None)
    if formulario.is_valid():
        sucesso = True
        formulario.save()
    '''
    
    contexto = { # Definir o contexto da view contato
        'telefone': '(99) 99999.9999',
        'responsavel': 'Maria da Silva Pereira',
        'formulario': formulario,
        'sucesso': sucesso
    }

    # Renderizar a página
    return render(request, 'contato.html', contexto)



# View para reserva de banho do pet
def reserva(request):
    # Sucesso no envio da mensagem
    sucesso = False
    
    if request.method == 'GET': # Se método da requisição é GET
        formulario = ReservaForm()
    # Método POST
    else:
        formulario = ReservaForm(request.POST)
        if formulario.is_valid(): # Verificar se form é válido
            sucesso = True
            formulario.save() # Salvar no banco de dados

    contexto = { # Criar contexto da view de reserva
        'sucesso': sucesso,
        'formulario': formulario
    }

    return render(request, 'reserva.html', contexto)


# View de login de usuário
def login_usuario(request):
    if request.method == 'GET':
        formulario = AuthenticationForm()
        return render(request, 'login.html', {'formulario': formulario})
    
    else:
        nome_usuario = request.POST['username']
        senha = request.POST['password']
        usuario = authenticate(request, username=nome_usuario, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        else:
            formulario = AuthenticationForm()
            return render(
                request, 'login.html', {'formulario': formulario, 'erro': 'Usuário ou senha inválidos!'}
            )
        

# View de logout
def logout_usuario(request):
    logout(request)
    return redirect('inicio')


# View de cadastro de novo usuário
def novo_usuario(request):
    if request.method == 'GET':
        formulario = UserCreationForm()
        return render(request, 'novo_usuario.html', {'formulario': formulario})
    
    else:
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')