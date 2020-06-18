# COMPANY-CLASSIFICATION


## Sobre

Uma API Web Python, que gera um ranking de empresas de acordo com o indice da mesma que é calculado pela quantidade de notas fiscais e débitos adicionados por arquivo através de upload em uma pagina web.

## Pré-requisitos e como rodar

1. Download:
    * [Python 3.8+](https://www.python.org/downloads/)
    * [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows)
    * [Tutorial de instalação](https://www.devmedia.com.br/instalacao-do-python/40643)
    
1. Clonar o repositório:
    * [Company-Classification](https://github.com/VictorSimao/COMPANY-CLASSIFICATION.git)
    
1. Abrir o projeto pelo PyCharm previamente instalado e configurado com o interpreter.

1. Instalar as dependências do projeto pelo terminal do pycharm :
    ```
     pip install --user pipenv
    ```
    ```
     pipenv install
    ```
    
1. Comando para rodar o projeto:
    ```
    pipenv run flask run
    ```
1. Acessa preferenficalmente pelo Google Chrome a URL:
    http://localhost:5000/
<img src="">


## Homepage

No primeiro acesso vai gerar uma pagina com 10 empresas previamente cadastradas e com score padrão de 50.
<img src="">

## Atualizando o Score

1. Selecione uma empresa.
<img src="">

1. Selecione um dois arquivo que se encontra na pasta do projeto (company-classification/archive/reports):
<img src="">

By Victor Simão :beers:	 [Mande um oi!](https://www.linkedin.com/in/victordiogosimao/)
