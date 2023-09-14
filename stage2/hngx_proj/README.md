# HNGX API ENDPONT - STAGE TWO

# About
    This project has five(5) api endpoints that allow for CRUD functionality on a 
    given data item in a database, specifically a "person" data item which has fields
        - Name - Character Field
        - Date creatd - Datetime field
        - Date updated - Datetime field

## Frameworks and libraries 
    - Django
    - Django Rest Framework
    - Request library

## Database used 
    PostgreSQL

## PROJECT STRUCTURE
 - The [app] folder contains the app's logic and functionalities
 - The [hngx_proj] folder contains the project settings and configurations
 - The [diagrams] folder contains the UML diagrams and ER diagrams for the database

  - The [api_test.py] file is a script to test out the api endpoints
  - All the requirements for this project are provided in the [requirements.txt] file.

## HOW TO RUN APP
  - The [run.bat] file is used to start the project server.
  - You can also use "python manage.py runserver" to start the local development server
    after cloning this repo and installing the needed requirements.