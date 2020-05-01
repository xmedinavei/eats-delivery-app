# eats-delivery


eats-delivery is a personal project, it's a REST API of restaurants delivery made using Django and Django REST frameworks as a tools for its development.

# Programing skills used in the project

  - Python
  - Django
  - Django REST framework
  - API REST
  - sqlite3


> The sqlite3 db is used only
> for programing purposes,
> not for production.

## URL paths
All urls path are on the eatsapp/urls.py documentation. Besides, they are on every views module documentation too.

## Installation

eats-delivery requires [Django](https://www.djangoproject.com/download/) v3+ to run.

> Virtual environments are not required but are strongly suggested.

Go to the app directory and run your virtual environments.

```sh
$ cd source <venv_name>/bin/activate
$ cd eatsapp_project
$ pip install -r requirements.txt

$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

## Contributing

I'll be happily accepting pull requests from anyone.

This that are missing right now:

* [ ] Add tests
* [ ] Add Auth to other kind of Users
* [ ] Implement async and periodic tasks.
* [ ] A UI!

Suggestions are welcome!


## Contributors

- [Xavier Medina](https://github.com/xmedinavei) | <xmedinavei@gmail.com>
