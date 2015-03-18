# django-dequorum
A simple web forum Django application

# Environment setup
python3 environment setup. You can use *either* virtualenv *or* virtualenv with virtualenvwrapper installed.

* [virtualenv](https://pypi.python.org/pypi/virtualenv)

    Create new virtual environments directory, e.g. `venvs`
    ```
    ~$ mkdir venvs
    ~$ cd venvs/
    ~/venvs$ 
    ```

    Create new virtual environment
    ```
    ~/venvs$ virtualenv -p `which python3` melb-django
    ```

    To start working on `django-python3` virtualenv
    ```
    ~/venvs$ cd melb-django/
    ~/venvs/melb-django$ source bin/activate
    ```
 
    To stop working on `django-python3` virtualenv

    ```
    (django-python3) ~/venvs/melb-django$ deactivate
    ```
 
* virtualenv with ([virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper/) installed

    ``` 
    ~$ mkvirtualenv -p `which python3` django-python3
    ```

    To start working on `django-python3` virtualenv

    ```
    ~$ workon django-python3
    (django-python3) ~$
    ```
    
    To stop working on `django-python3` virtualenv

    ```
    (django-python3) ~$ deactivate
    ```

Notes: 

* [virtualenv doc](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
* [virtualenvwrapper doc](https://virtualenvwrapper.readthedocs.org/en/latest/index.html)
* `(django-python3)` prompt change at your terminal indicating you're on `django-python3` virtualenv.

# Installation

1. Create new working directory

    ```
    (django-python3) ~$ mkdir melb-django
    (django-python3) ~$ cd melb-django/
    (django-python3) ~/melb-django$ 
    ```

2. Clone the git repository
 
    ```
    (django-python3) ~/melb-django$ git clone https://github.com/funkybob/django-dequorum.git
    (django-python3) ~/melb-django$ ls
    django-dequorum
    ```

3. pip install requirements

    ```
    (django-python3) ~/melb-django$ cd django-dequorum/
    (django-python3) ~/melb-django/django-dequorum$ pip install -r requirements.txt
    ```    
 
4. Test Django installation

    ```
    (django-python3) ~/melb-django$ python3 -c "import django; print (django.get_version())"
    1.7.6
    ```
 
5. Setup Django project

    ```
    (django-python3) ~/melb-django$ django-admin startproject proj 
    (django-python3) ~/melb-django/proj$ ls
    django-dequorum  proj
    ```

## dequorum app setup

1. Add `dequorum` folder as symbolic link 

    ```
    (django-python3) ~/melb-django/proj$ ls
    proj  manage.py
    (django-python3) ~/melb-django/proj$ ln -s ../django-dequorum/dequorum/ .
    (django-python3) ~/melb-django/proj$ ls
    dequorum  proj  manage.py
    ```

2. Add `dequorum` app to `INSTALLED_APPS`

    ```
    (django-python3) ~/melb-django/$ cd proj/proj/
    (django-python3) ~/melb-django/proj/proj$ vim settings.py
    ... 
    INSTALLED_APPS = (
        ...
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'dequorum',
    )
    ...
    ```

3. Add `dequorum.urls` to your url tree

    ```
    (django-python3) ~/melb-django/$ cd proj/proj/
    (django-python3) ~/melb-django/proj/proj$ vim urls.py
    ...
    urlpatterns = patterns('',
        ... 
        url(r'^dequorum/', include('dequorum.urls')),
    )
    ...
    ```

## Using the provided accounts app

1. Add `accounts` folder as symbolic link 

    ```
    (django-python3) ~/melb-django/proj$ ls
    proj  manage.py
    (django-python3) ~/melb-django/proj$ ln -s ../django-dequorum/accounts/ .
    (django-python3) ~/melb-django/proj$ ls
    accounts dequorum  proj  manage.py
    ```


2. Add `accounts` app to `INSTALLED_APPS`
   If you want to use the provided login/logout templates you must put `accounts` before `django.contrib.auth` in `INSTALLED_APPS`.

    ```
    (django-python3) ~/melb-django$ cd proj/proj
    (django-python3) ~/melb-django/proj/proj$ vim settings.py
    ... 
    INSTALLED_APPS = (
        ...
        'accounts',
        'django.contrib.auth',
        ...
    )
    ...
    ```

3. Set `AUTH_USER_MODEL` 

    ```
    (django-python3) ~/melb-django$ cd proj/proj
    (django-python3) ~/melb-django/proj/proj$ vim settings.py
    ...
    AUTH_USER_MODEL = 'accounts.User'
    ...
    ```

4. Add `accounts.urls` to your url tree, ideally as:

    ```
    (django-python3) ~/melb-django$ cd proj/proj
    (django-python3) ~/melb-django/proj/proj$ vim urls.py
    ...
    urlpatterns = patterns('',
        ... 
        url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    )
    ...
    ```

Related blog post [http://musings.tinbrain.net/blog/2014/sep/21/registration-django-easy-way/](http://musings.tinbrain.net/blog/2014/sep/21/registration-django-easy-way/)
    
# Run the app

1. Run `syncdb` and create `createsuperuser`

    ```
    (django-python3) ~/melb-django/proj$ ./manage.py syncdb
    Operations to perform:
    Apply all migrations: sessions, contenttypes, admin, auth, accounts, dequorum

    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying accounts.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying dequorum.0001_initial... OK
    Applying dequorum.0002_auto_20150129_1019... OK
    Applying sessions.0001_initial... OK

    You have installed Django's auth system, and don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Email: 
    Password: 
    Password (again): 
    Superuser created successfully.
    ```

2. Run the server 

    ```
    (django-python3) ~/melb-django/$ ./manage.py runserver
    ```

3. Open the browser

    ```
    http://localhost:8000/dequorum/
    ```

    To login
    ```
    http://localhost:8000/accounts/login/
    ``` 

    If you successfully logged in, you will be redirected to `/accounts/profile` with 404 error. _to fix_

    To post new thread (you need to login first)
    ```
    http://localhost:8000/dequorum/add/
    ```

# To contribute

1. Fork the repository

2. How to keep your forked repository updated

    Your current remote repository.
    ```
    (django-python3) ~/melb-django/django-dequorum$ git remote -v
    origin  https://github.com/funkybob/django-dequorum.git (fetch)
    origin  https://github.com/funkybob/django-dequorum.git (push)
    ```   

    You need to add another remote repository.
    ```   
    (django-python3) ~/melb-django/django-dequorum$ git remote add hack https://github.com/$github_username/django-dequorum.git 
    (django-python3) ~/melb-django/django-dequorum$ git remote -v
    origin  https://github.com/funkybob/django-dequorum.git (fetch)
    origin  https://github.com/funkybob/django-dequorum.git (push)
    hack    https://github.com/za/django-dequorum.git (fetch)
    hack    https://github.com/za/django-dequorum.git (push)
    ``` 

    replace `$github_username` with your github username. 

3. See the [github issues](https://github.com/funkybob/django-dequorum/issues) 

4. Make changes and commit at your hack repo. 

    ```
    (django-python3) ~/melb-django/django-dequorum$ git add .
    (django-python3) ~/melb-django/django-dequorum$ git commit -m "contribute to issue #99"
    (django-python3) ~/melb-django/django-dequorum$ git push hack master
    ``` 

5. Make a pull request
