[![Alt text](https://api.travis-ci.org/nhshackday14/consent-management.svg?branch=master)](https://travis-ci.org/nhshackday14/consent-management)

ProCL
=====
http://procl.co.uk/

ProCL is a tool designed to help clinicians when completing consent forms for medical and surgical procedures. It acts as a reminder for the benefits, risks, and other details that are necessary when completing Consent Form 1 in UK NHS hospitals.

More info at: http://procl.co.uk/#/about

Install
=======

System dependencies:
* Python 2.7
* Node.js

```
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    npm install -g grunt-cli
    npm install -g bower
    npm install
    bower install
```

Tests
=====

    ./tests.sh


Run server
==========

    python manage.py runserver 8080

* App: http://localhost:8080
* Admin: http://localhost:8080/admin


API
===

* http://localhost:8080/api-1/
* http://localhost:8080/api-1/procedures
* http://localhost:8080/api-1/procedures/1
* http://localhost:8080/api-1/procedures/?q=awef

