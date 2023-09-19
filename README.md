# PBP Assignment02 

You can access my deployed Django Project [here](https://digimontcg-inventory-manager.adaptable.app/main/)


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

   In the `urls.py` file found in the `"main"` application directory I add the path `path('', show_main, name='show_main'),` to the `urlpatterns` list which creates a path that calls the `show_main` function that was made in the previous section when the `/main/` path is called from the project URL. To test that the urls exist and the `/main/` page is rendered properly, I copied the code found on Tutorial 1, Unit Tests section, as well as 2 more simple tests, testing the information contained is correct, and pasted them to `tests.py` and ran the `python manage.py tests` command. 

* **Deploy your app to Adaptable so it can be accessed through the internet.**

  Lastly, after all changes have been made and the result from testing (using the command `python manage.py runserver` and `python manage.py tests`) is satisfied I do the 4 git mantras:`pull`,`add`,`commit`,`push` to the github repository. I then Signed in to Adaptable.io utilizing my Github account and made an app, utilizing the `Digimon_TCG_inventory` Github repository. For this project I used the settings: `Python App Template` as the deployment template, `PostgreSQL` as the database type, Python 3.11 as my Python version, `python manage.py migrate && gunicorn Digimon_TCG_inventory.wsgi` as the Start command, `digimontcg-inventory-manager` as the application name and the `HTTP Listener on Port` option checked. With my settings configured correctly I deployed my app.

________________________

## Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).

<img src="/assets/PBP_Assignment2_Flowchart.png">

________________________

## What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?

   A virtual environment is a tool that helps store packages and dependencies that are being utilized by your project(such as Django), separating them from your other installed Python packages, creating a clean, isolated environment for your project. Most Python programmers recommend utilizing the virtual environment to avoid problems occuring that could occur from clashing packages used in different projects being installed in the same global directory. One problem that can be mitigated by using virtual environments is the inability to have multiple versions of the same package in the same directory, caused by the fact that both versions would have the same name and the fact that directories must have unique files/package names within. With the use of virtual environments, this issue won't occur, since the version of the package for a specific project would be stored in the environment, not the global Python site-package folder, thus separating where the versions are installed, preventing the issue altogether. This scenario is actually quite common for web developers, especially if they get clients with older websites, which might use older versions of the Django package, which would clash with the newest Django package that utilize to make new Web apps. It also helps that by utilizing virtual environments, you are specifying the packages you intend to utilize, so you won't have any problems dealing with packages unrelated with your current project.


   In general, we **can** create a Django web app without a virtual environment, because you can just stick to the default where packages are installed in the global Python site-packages directory and they'll still work, but it is generally safer to just use a virtual environment, to prevent headache-inducing clashes and unforeseen consequences from haphazard installations. In fact, I had trouble doing Tutorial 0, because I had failed to activate the virtual environment (`env\Scripts\activate.bat` doesn't work for me, I need to use `env\Scripts\activate` without the `.bat`) and when I tried to download all of my packages, I was responded with a flood of error messages (probably caused by the fact that I have different versions of required packages already installed), which made it so when I tried to run some version specific commands I was met with errors stating that no such command exists.
___________________________

## What is MVC, MVT, and MVVM? Explain the differences between the three

   MVT, MVC and MVVM are all software design patterns utilised to structure how to implement UI components, event handling, data management and the communication between these different aspects to create a website. Although all 3 of them fulfill a similar role, they are different in how that role is executed. In this section I will explain what each of these design patterns mean, detailing the differences as we go along.

* **MVT**

     MVT stands for `Model View Template`, which are the 3 components that make up a web interface and it's applications. The specific purposes of these 3 components are as follows:

     **Model:** Acts as an interface for your data, defining the logical structures behind the web-application by extracting data from a database, translating that data using the models defined within your application, which will then be used by the View component to present that data to the user
  
     **View:**  Executes the business logic when an HTTP Request is accepted by: extracting information from the Models component, rendering the relevant template according to the request, using the data extracted earlier then returns the result as an HTTP response

     **Template:** Is the component responsible for the presentation/look of the webpage/application, typically made as an html file. Within the templates you can have variables, which will be replaced with actual values taken from the Views component

* **MVC**

     MVC stands for `Model View Controller`, which are the 3 main components of this design pattern.

     **Model:** Similar to MVT, this is where the managing data, data storage logic and communication with the database is handled

     **View:** This is where data presentations and components related to data representation is defined, different to MVT where View only dealt with business logic and request handling. In MVT this role is handled by the Template. The View in MVC also communicates with the controller when particular events occur and requests the model for data when any changes occur.

     **Controller:** This is the component that deals with user interaction, by tracking user events, processes any user events as defined by the developer, sending commands to the Model and View to create appropriate view. This is the component that distinguishes MVC from the rest, as MVT handles the role of the Controller using it's entire framework and MVVM utilises a View Manager which interacts with the model and view, but doesn't outright control what and when they must perform changes.

* **MVVM**

    MVVM stands fo `Model View View Model`, which like the rest, are the 3 main components of this design pattern

  **Model:** Similar to the other 2, the Model in MVVM abstracts the data stored according to the needs of the user. However one major difference is the absence of any direct interaction between the View and Model (this is handled by the View-Model component)

  **View:** Similar to the rest, holds all of the information regarding UI and display, including capturing user events and informing the ModelView. The View itself doesn't actually process the user request, it only informs the View Model when it occurs.

   **Model-View** This is where the functions that processes the user requests and Read/Write the models are stored. It also serves as a link between the Model and the View.

Overall all 3 design patterns have similaritues in which all storage-based logic are stored in a component called model, some portion if not all UI elements is in the View component and there is some way linking the 2 components to provide the user with a webpage. Differences lie in how user requests are handled (MVT handles it in Views, MVC has the Controller component handle it and MVVM has Model-View handle it), how the UI is generated, as well as how connected the View and the Model, along with a few others.

# PBP Assignment03

## Difference between POST and GET method?

   Let's first discuss how POST and GET works. Whenever anyone submits a POST form, the data inputted on the form is bundled up and encoded, sent to the server, in which it eill be processed and returns a response to the user. On the other hand the GET method bundles the dubmitted data into a string which will be used to create a URL which contains the address to where the data will be sent as well as any relevant keys and values. 
   
   The main difference between POST and GET is their uses, specifically the fact that posts should be used if you want users to submit data and/or make changes to the system/server, whereas get should be used to make requests/queries that don't make any system changes, and are just used to fetch data, such as fetching the result from a function, an http request, search etc. This is because in general post is much secure, especially when dealing with larger amounts of data, due to the fact that hackers can exploit the GET method by mimicking valid form requests, while the data from a POST request is encoded and validated by Django's protection mechanisms, such as the CSRF protection. Furthermore, GET is not recommended for the submission of sensitive info, as the submitted data will be visible as a URL in your taskbar, and easily accessible via search history and server logs.

_______________________

## What are the main differences between XML, JSON, and HTML in the context of data delivery? Why is JSON often used in data exchange between modern web applications?

   HTML (Hyper Text Markup Language) is a markup language that utilises tags (like <h1> </h1>), which is mainly used to format data aimed to make it readable and appealing to users. It wraps content with tags to define how the content should be formatted (e.g. h1 is the tag used to make giant headers). 

   XML (Extended markup language) is also a markup language that utlises tags that wrap around content, however instead of being used to define the formatting of content, XML is purely used to send and recieve data. It is equipped to do so by having a structure and rules that require information such as the type of the content to be specified. This is incredibly helpful when working with databases, since the XML structure works hand in hand with database structure, so when you input a data point in XML, since the type of each statistic/attribute in the data is defined by tags, the database knows where each part of the data needs to be stored. For example in XML if you want to send data about a ship named Bessie, in XML that would be represented ad <ship><name>Bessie</name></ship> in which when sent to the database, it will know that the data given is about a ship with the name of Bessie and store it accordingly. 

   JSON (Java Script Object Notatiuon) serves the same purpose as XML, where they are used to structure data to be sent and recieved, however they differ in how this is done. XML, like all markup language, define content/data in a tree manner, whereas JSON defines data in a key: value pair approach, similar to dictionaries. Due to how similar JSON's format is compared to modern programming languages such as Java, this form of data transmission/record has a much easier time interacting with those modern languages, thus better for modern web applications. Other than it being a lot more readable for humans and it's interaction with modern applications, JSON has other benefits such as having better schema support, server sparsing, easy manipulation and generally quicker than XML.
   
   Though keep in mind that XML is still used, mostly because XML's structure is a lot stricter, which means it is better than JSON when it comes to dealing with large and varied data, as it is a lot easier for machines to read the data and detect errors in XML, though JSON tends to still be the popular option as it is easier to read for humans, and is structured in a way that is familiar to programmers

   Overall HTML is used to define how to format content in a very user friendly way, while XML and JSON are used for data transmission and recording, structured similarly to how data is stored in the database, only having differences on how they fulfill that role. HTML is good for the frontend data presentation, whereas XML or JSON (chosen depending on your needs and familarity) is used to transmit data from and to the database

______________________
