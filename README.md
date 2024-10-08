# api_medilab
Para o funcionamento da aplicação, vamos começar iniciando o serviço de banco de dados, neste projeto estaremos utilizando o Postgres. Para utilização desse serviço estaremos utilizando o Docker, na pasta Container/Postgres - Medilab/, para iniciar o docker utilizamos o comando:  
```
      docker-compose up -d 
```

Nesta aplicação utilizamos no container a biblioteca do prisma para a criação das Tabelas de dados, [Documentação-Prisma](https://www.prisma.io/docs/getting-started/quickstart).
Pode conferir também o Repositório do Front-end no link a seguir: [Repositorio-Fron-end](https://github.com/schandon/medilab_av) 


## Configuração de Aplicação
Para não precisar instalar as bibliotecas na sua maquina, iremos utilizar a virtualização, como isso iremos seguir um conjunto de passos.
  * Passo 1:
    * Executar o código para criar a pasta do ambiente
 ```
      python -m venv env
```
  * Passo 2:
    * Entrar na modo virtualizado, executando o código
```
      env\Scripts\activate
```
##### OBS.
  * Passo 2.1:
    * Em caso de erro na criação do ambiente virtualizado, utilizaremos o comando a seguir, caso não de erro ao utilizar o Passo 02, ignore o Passo. 
```
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
``` 

* Passo 3:
  Para baixar tudo que for necessário para rodar a aplicação utilize: 
 ```
      pip install -r requirements.txt 
```

## Iniciando o Back-end
Para inicializar utilizaremo o comando:
 ```
      npm start
```

## Populando a Base
Utilize a Rota POST - `/pacientes` - Adiciona via arquivo ".Json", selecionando o arquivo data.json, que assim você irá popular a banco de dados e estara pronto para fazer a utilização da aplicação.

## Rotas Criadas
* GET - `/pacientes` - Busca todos os Pacientes cadastrados.
* GET - `/pacientes/<ID>` - Busca Pacientes especifico.
* POST - `/pacientes` - Adiciona via arquivo ".Json".
* POST - `/paciente` - Adiciona via corpo em formato Json.
* PUT - `/pacientes/<ID>` - Atualizar Paciente Cadastrado passando o ID.
* DELETE - `/pacientes/<ID>` - Delete um Paciente cadastrado passando o ID.

  **OBS: Arquivo do insonmina acompanha a aplicação como nome de Medilab_Insominia.json
