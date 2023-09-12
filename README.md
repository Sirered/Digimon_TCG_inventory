# PBP Assignment02 

## How did I implement the tasks on the checklist?
* ***Create a new Django project.***

   First I had to think of what I wanted to make for this assignment. One of the requirements for the project is that it must be an inventory management application. As an enthusiastic fan of card games, specifically the Digimon card game (recently), I decided to make my application a Digimon TCG inventory manager. With my plan set, I started by making a local directory (named `Digimon_TCG_inventory`) on my laptop and initiated git on it. I then made a Github repository online (with the same name) and connected it to the newly created local directory. This linkage allows me to push changes made on my laptop to the online repository, which will ultimately facilitate the application`s deployment.

   Additionally, I created and activated a virtual environment to isolate my project, preventing issues caused by external modules. Next using the python pip installer, I downloaded all modules required to make and run the django application. These dependencies were read from a txt file aptly named `requirements.txt`. Lastly to create the project, I executed the startproject command from the django-admin module (by running `django-admin startproject Digimon_TCG_inventory` on command line) then within the project directory created, configured the `settings.py` to allow any host to access the web application by adding `"*"` to the `ALLOWED_HOSTS` list. You can check if the project has been created properly by running the command `python manage.py runserver` via shell and checking the link provided by the command line (or by going [here](http://localhost:8000)). 

* ***Create an app with the name `main` on that project***

   To create the app named main for the project run the command `python manage.py startapp main` command via shell. Make sure to have the virtual environment active during this step. After creating the app, I reconfigured `settings.py` by adding `"main"` in the `INSTALLED_APPS` list, registering the created application
