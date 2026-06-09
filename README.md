# 🚗 Carros - Sistema de Gestão de Veículos

Projeto desenvolvido com Django para cadastro e gerenciamento de veículos.

## Funcionalidades

* Cadastro de marcas
* Cadastro de veículos
* Upload de imagens dos carros
* Controle de inventário
* Painel administrativo do Django
* Relacionamento entre marcas e veículos

## Tecnologias Utilizadas

* Python
* Django
* SQLite
* HTML
* CSS
* Bootstrap

## Estrutura do Projeto

### Marca

Cada veículo pertence a uma marca.

Campos:

* Nome

### Veículo

Campos:

* Modelo
* Marca
* Ano de fabricação
* Ano do modelo
* Placa
* Valor
* Foto
* Descrição

### Inventário

Controle automático de:

* Quantidade de carros
* Valor total do estoque

## Instalação

Clone o repositório:

```bash
git clone https://github.com/raizaramalho/Carros.git
```

Entre na pasta:

```bash
cd Carros
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

## Autor

Raiza Ramalho

GitHub:
https://github.com/raizaramalho
