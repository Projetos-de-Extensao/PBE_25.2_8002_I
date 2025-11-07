from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from rest_framework import viewsets

from .models import Proposta, Projeto, Coordenador, Professor, Empresa
from .serializers import PropostaSerializer, ProjetoSerializer, CoordenadorSerializer, ProfessorSerializer, EmpresaSerializer
from .forms import PropostaForm, EmpresaForm, ProfessorForm, CoordenadorForm


def escolher_tipo_cadastro(request):
    return render(request, 'escolher_cadastro.html')


@csrf_exempt
@transaction.atomic
def cadastro_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            nome_empresa = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            cnpj = form.cleaned_data['cnpj']
            
            
            if User.objects.filter(username=nome_empresa).exists():
                messages.error(request, 'Ja existe uma empresa com esse nome.')
                return render(request, 'cadastro_empresa.html', {'form': form})
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Esse e-mail ja esta cadastrado.')
                return render(request, 'cadastro_empresa.html', {'form': form})
            
            if Empresa.objects.filter(cnpj=cnpj).exists():
                messages.error(request, 'Esse CNPJ ja esta cadastrado.')
                return render(request, 'cadastro_empresa.html', {'form': form})
            
            usuario = User.objects.create_user(
                username=nome_empresa,
                email=email,
                password=form.cleaned_data['password']
            )
            
            empresa = form.save(commit=False)
            empresa.usuario = usuario
            empresa.save()
            
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('login')
    else:
        form = EmpresaForm()
    
    return render(request, 'cadastro_empresa.html', {'form': form})


@csrf_exempt
@transaction.atomic
def cadastro_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            matricula = form.cleaned_data['matricula']
            
            if User.objects.filter(username=matricula).exists():
                messages.error(request, 'Matricula ja cadastrada.')
                return render(request, 'cadastro_professor.html', {'form': form})
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Esse e-mail ja esta cadastrado.')
                return render(request, 'cadastro_professor.html', {'form': form})
            
            if Professor.objects.filter(matricula=matricula).exists():
                messages.error(request, 'Matricula ja cadastrada.')
                return render(request, 'cadastro_professor.html', {'form': form})
            
            usuario = User.objects.create_user(
                username=matricula,
                email=email,
                password=form.cleaned_data['password']
            )
            
            professor = form.save()
            
            messages.success(request, 'Professor cadastrado com sucesso!')
            return redirect('login')
    else:
        form = ProfessorForm()
    
    return render(request, 'cadastro_professor.html', {'form': form})


@csrf_exempt
@transaction.atomic
def cadastro_coordenador(request):
    if request.method == 'POST':
        form = CoordenadorForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            matricula = form.cleaned_data['matricula']
            
            if User.objects.filter(username=matricula).exists():
                messages.error(request, 'Matricula ja cadastrada.')
                return render(request, 'cadastro_coordenador.html', {'form': form})
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Esse e-mail ja esta cadastrado.')
                return render(request, 'cadastro_coordenador.html', {'form': form})
            
            if Coordenador.objects.filter(matricula=matricula).exists():
                messages.error(request, 'Matricula ja cadastrada.')
                return render(request, 'cadastro_coordenador.html', {'form': form})
            
            usuario = User.objects.create_user(
                username=matricula,
                email=email,
                password=form.cleaned_data['password']
            )
            
            coordenador = form.save()
            
            messages.success(request, 'Coordenador cadastrado com sucesso!')
            return redirect('login')
    else:
        form = CoordenadorForm()
    
    return render(request, 'cadastro_coordenador.html', {'form': form})


@csrf_exempt
@transaction.atomic
def cadastro(request):
    return redirect('escolher_cadastro')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        usuario = authenticate(request, username=username, password=senha)
        
        if usuario is not None:
            login(request, usuario)
            
            try:
                empresa = usuario.empresa
                messages.success(request, f'Bem-vindo, {empresa.nome}!')
                return redirect('dashboard')
            except Empresa.DoesNotExist:
                pass
            
            try:
                professor = Professor.objects.get(matricula=username)
                messages.success(request, f'Bem-vindo, Prof. {professor.nome}!')
                return redirect('dashboard_professor')
            except Professor.DoesNotExist:
                pass
            
            try:
                coordenador = Coordenador.objects.get(matricula=username)
                messages.success(request, f'Bem-vindo, Coord. {coordenador.nome}!')
                return redirect('dashboard_coordenador')
            except Coordenador.DoesNotExist:
                pass
            
            messages.warning(request, 'Perfil de usuario nao encontrado.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario ou senha incorretos.')
    
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Voce saiu com sucesso!')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    try:
        empresa = request.user.empresa
        propostas = Proposta.objects.filter(empresa=empresa)
        projetos = Projeto.objects.filter(proposta__empresa=empresa)
        
        context = {
            'empresa': empresa,
            'propostas': propostas,
            'total_propostas': propostas.count(),
            'projetos': projetos,
            'total_projetos': projetos.count()
        }
        return render(request, 'dashboard.html', context)
    except Empresa.DoesNotExist:
        messages.error(request, 'Empresa nao encontrada.')
        return redirect('login')


@login_required(login_url='login')
def dashboard_professor(request):
    try:
        professor = Professor.objects.get(matricula=request.user.username)
        projetos = Projeto.objects.filter(professor=professor)
        
        context = {
            'professor': professor,
            'projetos': projetos,
            'total_projetos': projetos.count()
        }
        return render(request, 'dashboard_professor.html', context)
    except Professor.DoesNotExist:
        messages.error(request, 'Professor nao encontrado.')
        return redirect('login')


@login_required(login_url='login')
def dashboard_coordenador(request):
    try:
        coordenador = Coordenador.objects.get(matricula=request.user.username)
        projetos = Projeto.objects.filter(coordenador=coordenador)
        todas_propostas = Proposta.objects.all().order_by('-id')
        
        context = {
            'coordenador': coordenador,
            'projetos': projetos,
            'total_projetos': projetos.count(),
            'propostas': todas_propostas,
            'total_propostas': todas_propostas.count()
        }
        return render(request, 'dashboard_coordenador.html', context)
    except Coordenador.DoesNotExist:
        messages.error(request, 'Coordenador nao encontrado.')
        return redirect('login')


@login_required(login_url='login')
def alterar_status_proposta(request, proposta_id):
    try:
        coordenador = Coordenador.objects.get(matricula=request.user.username)
    except Coordenador.DoesNotExist:
        messages.error(request, 'Apenas coordenadores podem alterar status de propostas.')
        return redirect('dashboard')
    
    try:
        proposta = Proposta.objects.get(id=proposta_id)
    except Proposta.DoesNotExist:
        messages.error(request, 'Proposta nao encontrada.')
        return redirect('dashboard_coordenador')
    
    if request.method == 'POST':
        novo_status = request.POST.get('status')
        if novo_status in ['Em análise', 'Aprovada', 'Recusada']:
            proposta.situação = novo_status
            proposta.save()
            messages.success(request, f'Status da proposta "{proposta.nomeSolucao}" alterado para "{novo_status}".')
        else:
            messages.error(request, 'Status invalido.')
        
        return redirect('dashboard_coordenador')
    
    context = {
        'proposta': proposta,
        'coordenador': coordenador
    }
    return render(request, 'alterar_status_proposta.html', context)


@login_required(login_url='login')
def designar_professor(request, proposta_id):
    try:
        coordenador = Coordenador.objects.get(matricula=request.user.username)
    except Coordenador.DoesNotExist:
        messages.error(request, 'Apenas coordenadores podem designar professores.')
        return redirect('dashboard')
    
    try:
        proposta = Proposta.objects.get(id=proposta_id)
    except Proposta.DoesNotExist:
        messages.error(request, 'Proposta nao encontrada.')
        return redirect('dashboard_coordenador')
    
    if proposta.situação != 'Aprovada':
        messages.error(request, 'Apenas propostas aprovadas podem ter professores designados.')
        return redirect('dashboard_coordenador')
    
    professores = Professor.objects.all()
    
    if request.method == 'POST':
        professor_id = request.POST.get('professor_id')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        
        if not professor_id:
            messages.error(request, 'Selecione um professor.')
            return render(request, 'designar_professor.html', {
                'proposta': proposta,
                'coordenador': coordenador,
                'professores': professores
            })
        
        try:
            professor = Professor.objects.get(id=professor_id)
            
            projeto = Projeto.objects.create(
                nome=proposta.nomeSolucao,
                descricao=proposta.objetivo,
                status='Em andamento',
                dataInicio=data_inicio,
                dataFim=data_fim,
                coordenador=coordenador,
                professor=professor,
                proposta=proposta
            )
            
            messages.success(request, f'Professor {professor.nome} designado com sucesso! Projeto "{projeto.nome}" criado.')
            return redirect('dashboard_coordenador')
            
        except Professor.DoesNotExist:
            messages.error(request, 'Professor nao encontrado.')
        except Exception as e:
            messages.error(request, f'Erro ao criar projeto: {str(e)}')
    
    context = {
        'proposta': proposta,
        'coordenador': coordenador,
        'professores': professores
    }
    return render(request, 'designar_professor.html', context)


@login_required(login_url='login')
def criar_proposta(request):
    try:
        empresa = request.user.empresa
    except Empresa.DoesNotExist:
        messages.error(request, 'Voce precisa estar vinculado a uma empresa para criar propostas.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = PropostaForm(request.POST)
        if form.is_valid():
            proposta = form.save(commit=False)
            proposta.empresa = empresa
            proposta.situação = 'Em análise'
            proposta.save()
            messages.success(request, 'Proposta criada com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulario.')
    else:
        form = PropostaForm()
    
    context = {
        'form': form,
        'empresa': empresa
    }
    return render(request, 'proposta.html', context)


class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

