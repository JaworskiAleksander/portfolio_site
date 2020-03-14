+ All projects should have a virtual environment dedicated just for that project, including plugins and add-ons
+ virtual envs should be located right next to the project folder, so that it's easy to know why it's thert
+ in order to install virtual env, type this
    ```bash
    pip3 install virtualenv     # install virtual environment plugin
    virtualenv my_venv          # create virtual env for this project
    source my_venv/bin/activate   # activate your newly found god powers!
    ```
+ install all we need

+ migrations should be included in your project ... makes sense
    https://stackoverflow.com/questions/28035119/should-i-be-adding-the-django-migration-files-in-the-gitignore-file

+ postgres DB running under the hood

//
### Setting up virtual environment
```bash
    virtualenv -p /usr/bin/python3 portfolio_env
    source /portfolio_env/bin/activate
    pip3 install psycopg2
    pip3 install Django
    pip3 install pillow
```

### setting up postgresql
```bash
    sudo apt-get update
    sudo apt-get install postgresql
    sudo -u postgresql psql
```
Once logged in psql shell, type this
```psql
    /password postgres
    <your_migthy_password>
    # create a database for each new project you make
    # or just use containers and set volumes accordingly -v "$(pwd)/project/data:/var/lib/postgres/data"
    # and don't forget to add this in volume: section too!

    CREATE DATABASE portfoliodb;
```

### applying migrations to new db
```bash
    python3 manage.py migrate
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
```

### creating superuser
`python3 manage.py createsuperuser`

### Working with models
+ create model class
+ register model in settings.
+ migrate all data into postgresql
+ add to the admin page