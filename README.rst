docdir
======

|build status|_

.. |build status| image:: https://travis-ci.org/DocDir/docdir.svg
.. _build status: http://travis-ci.org/DocDir/docdir

Prelim Stuff (For Ubuntu):
--------------------------

First Install pip For python3 (https://pip.pypa.io/en/latest/installing.html):

.. code-block:: bash
   
   sudo apt-get install python3-pip

Then Install Django 1.8.3 (https://docs.djangoproject.com/en/1.8/topics/install/):

.. code-block:: bash
   
   sudo pip3 install Django

Check if SQLite is installed:

.. code-block:: bash

   which sqlite3

If it wasn't, install it:

.. code-block:: bash

   sudo apt-get install sqlite3 libsqlite3-dev

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
