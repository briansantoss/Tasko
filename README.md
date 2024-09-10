# Tasko

## Rápida introdução &#x1F9D0;
Este repositório foi criado para abrigar a aplicação web ***Tasko***, desenvolvida para o projeto WebPython da disciplina de Tópicos Especiais em Software. O ****Tasko**** é um sistema de gestão de tarefas, ou seja, tem como principal objetivo fornecer uma estrutura e interface com a qual o usuário possa interagir e **criar**, **visualizar**, **alterar** e **remover** tarefas. Cada tarefa será composta por apenas 3 elementos: um **título**, **uma descrição** e um **status**.

Os dois primeiros elementos serão definidos livremente pelo usuário, enquanto o status terá o papel de indicar a progressão da tarefa. O status poderá assumir dois valores: **"Em andamento"**  e **"Concluída"**.

As duas próximas seções abordarão como configurar e instalar todos os recursos necessários para que o sistema funcione corretamente, além de uma leve e básica introdução ao seu processo de instalação, funcionamento e, principalmente, o seu uso.

## Configurando o ambiente &#x1F527;
O ***Tasko*** faz extensivouso das ferramentas do framework [Django](https://www.djangoproject.com/), escrito na linguagem de programação [Python](https://www.python.org/), portanto, para que não tenha problemas no funcionamento do sistema será necessária a presença do Python e, conjuntamente, o seu gerenciador de pacotes (pip), pelo qual será feita a instalação do pacote com os utilitários do Django e suas dependências, ambos presentes na sua máquina. A instalação do pacote Django pode ser feita tanto localmente isolada (via um ambiente virtual) como globalmente, deixamos ao seu critério essa escolha.

Pode começar a instalação abrindo algum shell que tenha ao seu dispor para uso, caso esteja usando a plataforma Windows, indicamos fortemente o uso do **PowerShell**, caso esteja fazendo uso de uma plataforma Linux, sugirimos o **Bash** (shell padrão em muitas das distribuições) ou o **Zsh** e digitando, no diretório/pasta onde deseja ter o projeto, o seguinte comando.

`git clone`

- <a href="https://www.python.org/downloads/" target="_blank">Instalação Python e pip</a>

Após a instalação e a configuração estiver completa, vá ao seu terminal, acesse 

