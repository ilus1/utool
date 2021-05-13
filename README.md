# utool

# Links
 ## Acesso ao site
 [http://utool.eba-zxrzr6yx.sa-east-1.elasticbeanstalk.com/](http://utool.eba-zxrzr6yx.sa-east-1.elasticbeanstalk.com/)

## Links úteis

Apresentação do projeto: [https://youtu.be/U_NnZSgAMYQ](https://youtu.be/U_NnZSgAMYQ)

# Sobre o projeto 
É uma página web para a comunidade do Distrito Federal e entorno, que serve como intermediário entre proprietário de ferramentas (manuais e/ou elétricas) e pessoas que procuram alugar ou emprestar. Para suprir demandas de pequenas reformas em apartamentos, mudanças ou até mesmo construções completas, o sistema aceitará hospedagens desde chaves de fenda, furadeira e aparador de grama, até betoneiras ou geradores de energia elétrica. 
## Sobre o Ártemis 
Quem somos nós? Paulo Henrique e Fernando Miranda estudantes da UnB do curso de Engenharia de Software na Universidade de Brasília, nos deparamos com a necessidade de um meio facilitador de empréstimo de ferramentas, a partir daí, idealizamos e desenvolvemos este.

# Como rodar o projeto

- No terminal, execute o comando:
```
git clone https://github.com/ilus1/utool.git
```
- Na pasta do repositório crie um ambiente virtual:
```
python3 -m venv "venv_name"
```
- Na pasta do repositório:
```
pip3 install -r requirements.txt
```
- Não esqueça de rodar as migrations:
```
python3 manage.py migrate
```
- Para botar colocar o site no ar em host local:

```
python3 manage.py runserver

e para acessar: http://localhost:8000/
```

- E para rodar os testes, na pasta do repositório execute:
```
pytest
```




