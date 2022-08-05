# DailyLetter
#### O Daily Letter é uma aplicação em Python, com a funcionalidade de enviar, todo dia no mesmo horario,  uma carta aleatoria para um destinatario desejado(atualmente ele só é compativel com remetentes Gmail). As mensagens são guardadas em um banco de dados MySql no Servidor e enviadas na hora escolhida. Para registrar novas mensagens há uma aplicação Cliente onde o usuário pode escrever e salvá-las. O app cliente, através do socket se comunica com o servidor na nuvem, ou no caso dessa build, entre o próprio localhost.

# App em execução

https://user-images.githubusercontent.com/110682904/183112501-ec55790f-fb01-4080-9ccc-2a02ec0a3b72.mp4

# Componentes e Arquitetura

#### O servidor é composto por 3 scripts: main.py, DB_Connect.py e Server_Socket.py. Já o Cliente é composto por 2: main.py, Server_Socket.py.

![Untitled-2](https://user-images.githubusercontent.com/110682904/183135637-695aecb9-6391-47ce-8efd-d4090b815d29.png)

##### Obs: O servidor foi feito para ser usado pela AWS ec2 Windows, mas acredito que funcione bem de outras formas.(O código aqui está feito para Localhost, caso deseja fazer uma build precisa definir um novo IP em main.py no '\DailyLetter - Servidor'

# Setup

## MySql

#### Baixe e installe o MySql:

##### https://dev.mysql.com/downloads/mysql/

##### Abra o MySql Command Line Client

##### Defina uma senha

##### Crie o Banco de Dados com o comando abaixo:

###### Create Database dailyletter

#### Conecte-se ao banco com o comando abaixo

###### Use dailyletter

##### Copie e cole o comando abaixo para criar a tabela:

###### CREATE TABLE MENSAGENS(IDMENSAGEM INT AUTO_INCREMENT PRIMARY KEY, MENSAGEM TEXT NOT NULL);

## Servidor

##### Inicialitze o Daily Letter Servidor.exe em '\DailyLetter - Servidor' e faça o setup como o programa pedir.

## Cliente

##### Inicialize o Dailly Letter em '\DailyLetter - Cliente' e deixe a sua mensagem.
