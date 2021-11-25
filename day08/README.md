EX is a Django app to conduct Web-based EX. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Create and start docker conteiners with gunicorn and nginx.

   ``docker-compose -f docker-compose.prod.yml up -d --build``
    
   Run ``pdocker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`` to create the ex models.
    
   Run ``pdocker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`` to collects the static files into STATIC_ROOT.
   
   Visit http://localhost:1337/ to participate in the poll.

2. Create and start docker conteiners with server django

    ``docker-compose up -d --build``
   
    Start the development server and visit http://127.0.0.1:8000/admin/
    to create a ex (you'll need the create superuser).
