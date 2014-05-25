consent-management
==================


Install:
```
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py IC10_data_import
    npm install -g grunt-cli
    npm install -g bower
    npm install
    bower install
    grunt
```

Run server:
```
    python manage.py runserver 8080
```

Frontend:
```
    http://localhost:8000/static/index.html
```

Access Django admin:
    localhost:8080/admin

User API:

    localhost:8080/api-1/
    localhost:8080/api-1/procedures
    localhost:8080/api-1/procedures/1
    localhost:8080/api-1/procedures/?q=awef
    
