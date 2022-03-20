# Interns-Backend
Backend application for custom data collection app

# Folders and Files

1.  #### Data_Collection_API
This is the main project directory.This folder contains the settings.py, urls.py, wsgi.py, asgi.py and __init__.py files.   

> __init__.py ==> Python file that allows Python packages to be imported from directories where it's present.

> asgi.py ==> Asynchronous Server Gateway Interface(ASGI)  contains ASGI configuration properties for the Django project. ASGI is the recommended approach to deploy Django applications asynchronously on production.

> settings.py ==> Contains the configuration settings for the Django project.

> urls.py ==> Contains URL patterns for the Django project.

> wsgi.py ==> Web Server Gateway Interface(WSGI) contains WSGI configuration properties for the Django project. WSGI is the recommended approach to deploy Django applications on production

2. #### surveyapi
This is the main RESTAPI application folder. It contains a migration folder, __init__.py file, admin.py file, apps.py file, models.py file, serializers.py file, tests.py file, urls.py file and views.py file.

> migrations ==> This folder contains the migrated data from the app to the backend database (postgres). 

> admin.py ==> The admin.py file is used to display the models in the Django admin panel. 

> apps.py ==> This file is created to help include any application configuration for the app.

> models.py ==> Th models.py file contains classes that represents table or collection in the database and where every attribute of the class is a field of the table or collection.

> serializers.py ==> This file contains serializers for the models. Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

> tests.py ==> This file will contain test classes for the surveyapi appllication. 

> urls.py ==> This file contains url routing information for the surveyapi app. 

> views.py ==> This file contains viewsets for the api.  Views are Python functions or classes that receive a web request and return a web response.

3. #### .gitignore

This file ignores specified files from being committed to git.

4. #### .travis.yml

This file specifies the programming language used, the desired building and testing environment (including dependencies which must be installed before the software can be built and tested), and various other parameters.

5. #### manage.py 

Runs project specific tasks. Just as django-admin is used to execute system wide Django tasks, manage.py is used to execute project specific tasks.

6. #### requirements.txt

This file contains necessary python packages and dependencies to be installed for the api.

7. #### Procfile

This file is used to explicitly declare your application's process types and entry points.


## Future work

1. API Permissions & Authentication
2. Tests 
3. More logic in viewsets
4. API Schema and Documentation Generation
5. Image uploading & storage