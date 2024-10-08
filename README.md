# Tasko
## Menu de Navegação
1. [Introdução](#rápida-introdução-)
2. [Configurações](#configurando-o-ambiente-)
   - [Clonando o repositório](#clonando-o-repositório-)
   - [Instalando (e configurando) o Python](#instalando-e-configurando-o-python-)
   - [Baixando dependências](#baixando-as-dependências-)
   - [Configurando o DB](#configurando-o-banco-de-dados-)
3. [Uso](#usando-o-tasko-)

## Rápida introdução &#x1F9D0;
Este repositório foi criado para abrigar a aplicação web ***Tasko***, desenvolvida para o projeto WebPython da disciplina de Tópicos Especiais em Software. O ***Tasko*** é um sistema de gestão de tarefas, ou seja, tem como principal objetivo fornecer uma estrutura e interface com a qual o usuário possa interagir e **criar**, **visualizar**, **alterar** e **remover** tarefas. Cada tarefa será composta por apenas 3 elementos: um **título**, **uma descrição** e um **status**.

Os dois primeiros elementos serão definidos livremente pelo usuário, enquanto o status terá o papel de indicar a progressão da tarefa. O status poderá assumir dois valores: **"Em andamento"**  e **"Concluída"**.

As duas próximas seções abordarão como configurar e instalar todos os recursos necessários para que o sistema funcione corretamente, além de uma leve e básica introdução ao seu processo de instalação, funcionamento e, principalmente, o seu uso.

## Configurando o ambiente &#x1F527;
O ***Tasko*** faz extensivo uso das ferramentas do framework [Django](https://www.djangoproject.com/), escrito na linguagem de programação [Python](https://www.python.org/), portanto, para que não tenha problemas no funcionamento do sistema será necessária a presença do Python e, conjuntamente, o seu gerenciador de pacotes (pip), pelo qual será feita a instalação do pacote com os utilitários do Django e suas dependências, ambos presentes na sua máquina. A instalação do pacote Django pode ser feita tanto localmente isolada (via um ambiente virtual) como globalmente, deixamos ao seu critério essa escolha.

### Clonando o repositório &#x1F47B;
Pode começar a instalação de fato abrindo algum shell que tenha ao seu dispor para uso, caso esteja usando a plataforma Windows, indicamos fortemente o uso do **PowerShell**, caso esteja fazendo uso de uma plataforma Linux, sugerimos o **Bash** (shell padrão em muitas das distribuições) ou o **Zsh** e digitando, no diretório/pasta onde deseja ter o projeto, o seguinte comando:

```
git clone https://github.com/briansantoss/Tasko.git
```

### Instalando e configurando o Python &#x1F40D;
Não tente rodar nada ainda, não temos o Django, que, como anteriormente referido, é indispensável para o bom funcionamento do ***Tasko***. Feito isso, estamos habilitados a partir para a instalação do Python, segue o link para download abaixo:

- <a href="https://www.python.org/downloads/" target="_blank">Instalação Python e pip</a>

### Baixando as dependências &#x1F4BE;
Após a instalação e a configuração estiver completa, faremos uso do `requirements.txt`, um arquivo de texto simples onde se encontram todas as dependências do projeto, ele vai automatizar a instalação delas, para isso, basta passarmos-o ao pip, para isso, vá ao seu terminal, acesse novamente o diretório onde o projeto foi clonado e rode o seguinte comando:

> No Windows:

```
py -m pip install -r requirements.txt
```

> No Linux:

```
python -m pip install -r requirements.txt
```

### Configurando o banco de dados &#x1F4E6;
Antes de irmos aos finalmente e poder executar o Tasko na sua máquina será necessária a configuração do banco de dados, mas não se preocupe, apenas dois comandos serão requeridos, eles serão responsáveis por criar o banco de dados e as tabelas de fato:

> No Windows:
```
py manage.py makemigrations
py manage.py migrate
```

> No Linux:
```
python manage.py makemigrations
python manage.py migrate
```

Prontinho! Você está agora habilitado a executar o ***Tasko***, aproveite!:

> No Windows:
```
py manage.py runserver
```

> No Linux:

```
python manage.py runserver
```

## Usando o Tasko &#x1F973;
