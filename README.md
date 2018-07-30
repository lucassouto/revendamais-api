# Django API RevendaMais

## Rodando localmente

Assumindo que você está usando [Python](https://www.python.org/) 3.6.x ou superior e o gerendiador de dendências [pip](https://pypi.org/project/pip/) siga os passos para executar o projeto localmente.


Crie o banco de dados revendamais_api:

```sql
CREATE USER "django_revendamais";
CREATE DATABASE "revendamais_api";
GRANT ALL PRIVILEGES ON DATABASE "revendamais_api" TO "django_revendamais";
ALTER USER "django_revendamais" CREATEDB;
```

Instale virtualenv:

```bash
pip3 install virtualenv
```

Crie e ative um novo enviroment Python:

```bash
virtualenv env
source env/bin/activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements/local.txt
```

Configure as variáveis de ambiente:

```bash
SECRET_KEY="x7c**8y&oc#0s5^5biu*8d)lyr$xl^t0rxi=4!+v*ipkr%ey*v"
DATABASE_URL="postgres://django_revendamais@localhost:5432/revendamais_api"
DEBUG="True"
API_KEY="s0Ib0hCIhWpzrzHiMYKg4ysfD"
API_SECRET="5KtKazHyxKunlgDQfTZqGzV6BxokKetVykEe8aU1ZPDtJk7Cr0"
ACCESS_TOKEN="2511567800-2QXairBlcmyEl90ob4jbkuLlzLMnxFHtYWca7oD"
ACCESS_TOKEN_SECRET="049GKUQFHxm2l4SDmjyWee4rJLmIpRioPVtAacUmvUlbt"
FILE_WOEID="woeids.json"

```

Rode as migrações do banco de dados:

```bash
./manage.py migrate
```

Start a aplicação:

```bash
./manage.py runserver
```


## Opcional:

Rode o [Tox](https://tox.readthedocs.io/en/latest/) para os testes e checagem de código:

```bash
tox
```