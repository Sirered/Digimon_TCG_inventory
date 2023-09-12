# PBP Assignment02 

## How did I implement the tasks on the checklist?
* **Create a new Django project.**

   First I had to think of what I wanted to make for this assignment. One of the requirements for the project is that it must be an inventory management application. As an enthusiastic fan of card games, specifically the Digimon card game (recently), I decided to make my application a Digimon TCG inventory manager. With my plan set, I started by making a local directory (named `Digimon_TCG_inventory`) on my laptop and initiated git on it. I then made a Github repository online (with the same name) and connected it to the newly created local directory. This linkage allows me to push changes made on my laptop to the online repository, which will ultimately facilitate the application`s deployment.

   Additionally, I created and activated a virtual environment to isolate my project, preventing issues caused by external modules. Next using the python pip installer, I downloaded all modules required to make and run the django application. These dependencies were read from a txt file aptly named `requirements.txt`. Next, I executed the startproject command from the django-admin module (by running `django-admin startproject Digimon_TCG_inventory` on the command line). This created the project directory `Digimon_TCG_inventory` (not to be confused with the main directory also named `Digimon_TCG_inventory`). Within the project directory, I configured the `settings.py` to allow any host to access the web application by adding ` "*" ` to the `ALLOWED_HOSTS` list. You can check if the project has been created properly by running the command `python manage.py runserver` via shell and checking the link provided by the command line (or by going [here](http://localhost:8000)). 

* **Create an app with the name `main` on that project**

   To create the app named main for the project run the command `python manage.py startapp main` command in the `main directory` via shell, which made an application directory named `"main"`. Make sure to have the virtual environment active during this step. After creating the app, I reconfigured `settings.py` by adding `"main"` in the `INSTALLED_APPS` list, registering the created application.

* **Create a URL routing configuration to access the `main` app**

   To create a URL routing that will allow users of the project to access the main app I first had to import the `include` function from the `django.urls` module onto the `urls.py` file found in the project directory (not the application directory). Then within the urlpatterns list I added the element `path('main/', include('main.urls')),`. This makes it so the path `'main/'` will be directed to the route defined in the `urls.py` in the `"main"` application directory, which will be used to access the `main` app

* **Create a model on the main app with name Item and some mandatory attributes**

   In the `models.py` file found in the `"main"` application directory I created a class named `Item`, which is my created model. Within the `Item` class I added some class variables, which are the attributes of the model:
  1. `name`: A `CharField` that is the name of the item/card. 
  2. `category`: A `CharField` that is the name category of the item/card
  3. `release`: A `CharField` that is the initial release of the item/card
  4. `amount`: An `IntegerField` that is the amount of the item/card in stock/inventory/collection
  5. `price`: An `IntegerField` that is the price of the item/card
  6. `description`: A `TextField` that describes the item/card. Typically the card text of the card
  
     After making the model (and making any changes to a model) I ran the `python manage.py makemigrations` then the `python manage.py migrate` commands, so that Django can track the changes of the database schema, which the `models.py` file is in charge of

* **Create a function in `views.py` that returns an HTML template containing your application name, your name, and your class**

   First, I made a `templates` directory in the `"main"` application directory. Then in the newly created directory, I created an html file named `main.html`, where I created a basic html template that included the name of my application (Digimon TCG Inventory Manager), my own name (Galih Ibrahim Kurniawan), my class (PBP KKI), a notice that this is a work in progress and information about a card, with the information listed within the model made previously. Within the template, instead of actually writing information related to myself or the card, I had instead utilized variables using the format `{{ variable }}`. Then  in `views.py`, I created a function called `show_main`. In this function is a dictionary called `context` which defines the actual values that replace the variables found in the html template, as well as the line `return render(request, 'main.html', context)`, which accepts the HTTP request from the user and render the `main.html` template, utilizing the `context` dictionary to replace any variables.

* **Create a routing in `urls.py` to map the function in `views.py` to an URL**

   In the `urls.py` file found in the `"main"` application directory I add the path `path('', show_main, name='show_main'),` to the `urlpatterns` list which creates a path that calls the `show_main` function that was made in the previous section when the `/main/` path is called from the project URL. To test that the urls exist and the `/main/` page is rendered properly, I copied the code found on Tutorial 1, Unit Tests section and pasted them to `tests.py` and ran the `python manage.py tests` command. 

* **Deploy your app to Adaptable so it can be accessed through the internet.**

  Lastly, after all changes have been made and the result from testing (using the command `python manage.py runserver` and `python manage.py tests`) is satisfied I do the 4 git mantras:`pull`,`add`,`commit`,`push` to the github repository. I then Signed in to Adaptable.io utilizing my Github account and made an app, utilizing the `Digimon_TCG_inventory` Github repository. For this project I used the settings: `Python App Template` as the deployment template, `PostgreSQL` as the database type, Python 3.11 as my Python version, `python manage.py migrate && gunicorn Digimon_TCG_inventory.wsgi` as the Start command, `digimontcg-inventory-manager` as the application name and the `HTTP Listener on Port` option checked. With my settings configured correctly I deployed my app.
________________________

## What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?

   A virtual environment is a tool that helps store packages and dependencies that are being utilized by your project(such as Django), separating them from your other installed Python packages, creating a clean, isolated environment for your project. Most Python programmers recommend utilizing the virtual environment to avoid problems occuring that could occur from clashing packages used in different projects being installed in the same global directory. One problem that can be mitigated by using virtual environments is the inability to have multiple versions of the same package in the same directory, caused by the fact that both versions would have the same name and the fact that directories must have unique files/package names within. With the use of virtual environments, this issue won't occur, since the version of the package for a specific project would be stored in the environment, not the global Python site-package folder, thus separating where the versions are installed, preventing the issue altogether. This scenario is actually quite common for web developers, especially if they get clients with older websites, which might use older versions of the Django package, which would clash with the newest Django package that utilize to make new Web apps. It also helps that by utilizing virtual environments, you are specifying the packages you intend to utilize, so you won't have any problems dealing with packages unrelated with your current project.


   In general, we **can** create a Django web app without a virtual environment, because you can just stick to the default where packages are installed in the global Python site-packages directory and they'll still work, but it is generally safer to just use a virtual environment, to prevent headache-inducing clashes and unforeseen consequences from haphazard installations. In fact, I had trouble doing Tutorial 0, because I had failed to activate the virtual environment (`env\Scripts\activate.bat` doesn't work for me, I need to use `env\Scripts\activate` without the `.bat`) and when I tried to download all of my packages, I was responded with a flood of error messages (probably caused by the fact that I have different versions of required packages already installed), which made it so when I tried to run some version specific commands I was met with errors stating that no such command exists.
___________________________

## 
