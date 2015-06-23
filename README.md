# Backend do Projeto Biciguia

O backend serve para funções que necessitem de uma comunicação com o servidor. Por enquanto, ele somente recebe o feedback dos usuários e mostra via uma interface de admin ou via um POST request.

O backend é feito em Python e Django, para o Banco de Dados utilizamos SQLite + Spatialite. 
 

## Instalação

É um projeto em Python, então, embora não seja necessário, é recomendado criar um Virtualenv. [Instruções aqui](http://docs.python-guide.org/en/latest/dev/virtualenvs/). 

Instale as dependências:
```shell
pip install -r requirements.txt
```

Para o banco de dados, o SQLite costuma vir por padrão em tudo quanto é canto. O Spatialite, não. Para instalar o Spatialite no Ubuntu, basta:
```shell
sudo apt-get install spatialite-bin
``` 
Com o banco de dados instalado, rode as migrações para popular o banco de dados:
```
python manage.py migrate
```
Crie um usuário admin:

```
python manage.py createsuperuser
```
E finalmente rode em modo debug:
```
python manage.py runserver
```

Se você quiser rodar o servidor em produção, recomendamos usar o [Gunicorn](http://gunicorn.org/). Como esse backend não tem arquivos estáticos, não é necessário usar o nginx junto (mas se você puder usar, melhor. O nginx serve como load balancer e isso é bem útil)

## API Endpoints:

### /reclamacao/ - POST

Aceita um JSON contendo os seguintes campos:

```
texto: 'Texto de feedback'
endereco_origem: 'Endereço de origem'
endereco_destino: 'Endereço de destino'
ponto_origem: 'Coordenada de origem em formato {lat, lon}'
ponto_destino: 'Coordenada de destino em formato {lat, lon}'
rota_tracada: 'Rota traçada pelo aplicativo, enviada como linestring'
```
Exemplo: 
```
{
        "texto": "blablabla",
        "endereco_origem": "bla",
        "endereco_destino": "bla",
        "ponto_origem": {
          "type": "Point",
          "coordinates": [
            -46.72717094421386,
            -23.547031868098472
          ]
        },
        "ponto_destino": {
          "type": "Point",
          "coordinates": [
            -46.72717094421386,
            -23.547031868098472
          ]
        },
        "rota_tracada": {
          "type": "LineString",
          "coordinates": [
            [
              -46.72639846801758,
              -23.53939932020045
            ],
            [
              -46.723480224609375,
              -23.539910793443664
            ],
            [
              -46.72262191772461,
              -23.53723537293223
            ],
            [
              -46.726698875427246,
              -23.535976332684992
            ]
          ]
        }
```

### /reclamacao/ - GET

Esse é mais simples. Você manda uma request sem nada e recebe de volta a lsita de reclamações. 
