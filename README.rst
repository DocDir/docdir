docdir
======

Web Application
---------------

The web application is written in `django <http://djangoproject.com/>`_, and is
Python 3 compatible. It can be controlled with the ``manage.py`` script, see:

.. code-block:: bash

   python manage.py help

Getting Started
---------------

First you'll have to migrate the database. Because the application uses `sqlite
<https://sqlite.org/>`_, the setup procedure is simple:

.. code-block:: bash

   python manage.py migrate

With database in hand, start the development server:

.. code-block:: bash

   python manage.py runserver

Navigate your browser to the server URL, by default ``http://127.0.0.1:8000/``.

To use the admin tools, located at the running server's ``/admin`` path, you
must create an admin account:

.. code:: bash

   python manage.py createsuperuser
