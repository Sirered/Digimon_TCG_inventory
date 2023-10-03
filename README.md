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

   HTML (Hyper Text Markup Language) is a markup language that utilises tags (like `<h1> </h1>`), which is mainly used to format data aimed to make it readable and appealing to users. It wraps content with tags to define how the content should be formatted (e.g. h1 is the tag used to make giant headers). 

   XML (Extended markup language) is also a markup language that utlises tags that wrap around content, however instead of being used to define the formatting of content, XML is purely used to send and recieve data. It is equipped to do so by having a structure and rules that require information such as the type of the content to be specified. This is incredibly helpful when working with databases, since the XML structure works hand in hand with database structure, so when you input a data point in XML, since the type of each statistic/attribute in the data is defined by tags, the database knows where each part of the data needs to be stored. For example in XML if you want to send data about a ship named Bessie, in XML that would be represented ad <ship><name>Bessie</name></ship> in which when sent to the database, it will know that the data given is about a ship with the name of Bessie and store it accordingly. 

   JSON (Java Script Object Notatiuon) serves the same purpose as XML, where they are used to structure data to be sent and recieved, however they differ in how this is done. XML, like all markup language, define content/data in a tree manner, whereas JSON defines data in a key: value pair approach, similar to dictionaries. Due to how similar JSON's format is compared to modern programming languages such as Java, this form of data transmission/record has a much easier time interacting with those modern languages, thus better for modern web applications. Other than it being a lot more readable for humans and it's interaction with modern applications, JSON has other benefits such as having better schema support, server sparsing, easy manipulation and generally quicker than XML.
   
   Though keep in mind that XML is still used, mostly because XML's structure is a lot stricter, which means it is better than JSON when it comes to dealing with large and varied data, as it is a lot easier for machines to read the data and detect errors in XML, though JSON tends to still be the popular option as it is easier to read for humans, and is structured in a way that is familiar to programmers

   Overall HTML is used to define how to format content in a very user friendly way, while XML and JSON are used for data transmission and recording, structured similarly to how data is stored in the database, only having differences on how they fulfill that role. HTML is good for the frontend data presentation, whereas XML or JSON (chosen depending on your needs and familarity) is used to transmit data from and to the database

______________________

## Explain how you implemented the checklist above step-by-step.

* **Create a form input to add a model object to the previous app.**
   First, I made a file called forms.py in the main application directory. In that file I defined a subclass of the ModelForm class(that is provided by Django), named ItemForm. Within the ItemForm class is the inner class Meta, in which we define the model used for the form (which is the Item model made last week), as well as the fields that will be asked (which is all the attribvutes of the Item class other than Date Added, which by default is the date that the form was answered on).
  
  Afterwards I went to the views.py and imported the Item and ItemForm class from main.models and main.forms (found in the main application) and the HTTPResponse and serializers from django.http and django.core (provided by Django). Then I added the create_item function, where if it is called and there has been a POST request, with valid entries, the request will be saved and call the show_main function, returning the user to the main page, otherwise it will render the create_item.html template with an empty ItemForm as it's context. Next, I created the create_item.html that will be called by the create_item function, which presents the user with each field of the Item model (other than date added) and a text bow to fill in the data of the item. The template will also provide a button with the text "Add Item" which when pressed will submit the item and it's data, to the create_item function which will save the form to the database.

  Lastly, I added the a path in the urls.py file in the main application directory that calls the create_item function by adding `path('create-item', create_item, name='create_item'),` to the urlpatterns list.  Afterwards in the main.html I added a button with the text "Add New Item" on it, that sends the user to the create_item page, via the new url path.

* **Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.**

   Firstly I made changes in the show_main function in the views.py file, by adding an id parmater which by default is 1. I then added a line that accesses all Item objects and store it in the variable items (`items = Item.objects.all()`), as well as a line that gets an object from the Item objects list according to the id inputted and store it in a variable named id_item(`id_item = Item.objects.get(id=id)`). After that, I removed all variables other than my name and class in the context dictionary and replaced them with the lines `'item': id_item` and `'items': items`. To accomodate these changes, I editted the main.html template so that all instances of `{{variable}}` other than my name and class are changed to `{{item.variable}}`, which will make it display the value of that variable/attribute of the item that is curretly being viewed (according to the id taken from the show_main function). At the end I also added added a table which lists all items that have been stored in the database, only presenting the name, code, price, amount in stock and Date Added for each item.
  
  In the urls.py file I added a path in urlpatterns: `path('<int:id>/', show_main, name='show_main'),`, which will reroute paths that is just an integer to the show_main function, and will use the integer as the input for the id parameter for the show_main function. With that, people can just typr the id of an item on the URL to view the full information of the item of that id. In the main.html template I wrapped the name of the items in the table with `<a>` tags, with the `href "/{{item.id}}"`, so that if users click on the name of an item in the table, it will return the page with the full information of the item that was clicked.

  After that I added a show_xml function in views.py which when called, will recieve a request, store all Item objects in a variable called data (`data = Item.objects.all()`) then return an HTTP response that translates and formats that data to XML by using serialisers (`return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")`) to the user. I also a show_json function that serves a similar purpose as show_xml, but the data is translated to JSON format instead of XML (it uses the same method as show_xml, just replace every instance of xml in the HTTPResponse function call to json).

   Lastly, I added a show_xml_by_id and show_json_by_id function which, when called will recieve a request and an integer (storing that integer as a parameter called id), gets the data of the item with that id (`data = Item.objects.filter(pk = id)`) then returns an HTTP response with the data of that item in xml or json(done the same way as their non-id counterparts)

* **Create URL routing for each of the views added in point 2.**

  In the urls.py file in the main application add paths for each of the newly added functions in the urlpatterns list like so:
  
  `path('xml/', show_xml, name= 'show_xml'),`
  
  `path('json/', show_json, name = 'show_json'),`
  
  `path('xml/<int:id>/', show_xml_by_id, name= 'show_xml_by_id'),`
  
  `path('json/<int:id>/', show_json_by_id, name= 'show_json_by_id')`
  
  This will reroute '/xml/' and '/json/' path to the show_xml and show_json function respectively and if they add an integer to the end, it will reroute to the show_xml_by_id or show_json_by_id function with the integer added to the end as the input for the id parameter of those functions.

______________________________________

## Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.

* **HTML VIEW**

<img src="/assets/PBP_Assignment3_html1.png">
<img src="/assets/PBP_Assignment3_html2.png">
<img src="/assets/PBP_Assignment3_html3.png">

* **XML VIEW**

<img src="/assets/PBP_Assignment3_xml1.png">
<img src="/assets/PBP_Assignment3_xml2.png">

* **JSON VIEW**

<img src="/assets/PBP_Assignment3_json1.png">
<img src="/assets/PBP_Assignment3_json2.png">

* **XML BY ID VIEW**

<img src="/assets/PBP_Assignment3_xmlID.png">

* **JSON BY ID VIEW**

<img src="/assets/PBP_Assignment3_jsonID.png">

# PBP Assignment04

## What is UserCreationForm in Django? Explain its advantages and disadvantages.

   UserCreationForm is a built-in module provided by Django, used to allow people to register to your website, thus creating a user account, which the user will have to login with to access resources that are only accessible to that user or admins/superusers. It does this by inheriting attrivutes and methods from the ModelForm class, however instead of you having to make a model for that modelform and fill out the fields asked yourself, it will instead make an object of the User class (that is a built-in model from Django), which will represent the account of the newly registered user. The fields  of this class is the username (which will be the username of the User object created), password1 (which will be the password associated with the new User object) and password2 (which will be used to verify that password1 is indeed the password the new user wants for their account.

   A giant advantage to UserCreationForm is its easy implementation, as it gives you a default template and since it's a subclass of ModelForm and implements the User class it does all the work of figuring out how to store the data onto the database and ensures that the registration will work with the rest of the modules on Django, which is a lot better than developers fumbling around to make their own registration form in which the worst case scenario is that the implementation lacks security for malicious actors to capitalise on (or just doesn't work). A disadvantage one might come accross is that the default template is very lacklustre and bare, though that issue can be somewhat rectified by making a subclass of the UserCreationForm class and having any new fields be introduced in the subclass, while retaining the important functions of the UserCreationForm, but there still might be specifications where starting from scratch would be a lot less of a hassle. 

________________________________

## What is the difference between authentication and authorization in Django application? Why are both important?

   Authentication refers to the process of verifying who someone is, ensuring that whoever is trying to claim to be someone or trying to log into an account is indeed the person being claimed or is indeed someone who is allowed to use this account (like how both parents are allowed to access the school account of their child). This is normally done by having the claimer to present/submit something that only the person they are claiming to be should have or know (such as password, ID card, biometrics[like fingerprint scans]). On the other hand, authorisation is the process of deciding what a user should be able to do and what they can access. Examples of authorisation include: deciding if a user has rights to edit content, deciding if a user is allowed to view certain information (such as the private information of other users), deciding if a user can create items in the database etc.

   Both authentication and authorisation is essential for security. If authorisation is weak, malicious actors can deface the website, access private or sensitive information, infect the server or other user's computers etc. If you have strong authorisation, but weak authentication, infiltrators can masquerade as other users or admins and be able to access information or execute actions that only the user being masqueraded can access/do, but others shouldn't, making authorisation useless if the authentication is easily bypassed. Hence, both authentication and authorisation is key to ensure that your web application is secure and isn't exploited

_________________________________

## What are cookies in website? How does Django use cookies to manage user session data?

   Internet cookies are small text files sent by the server to your browser and is stored in your browser folder either permanently or for a predetermined amount of time set by the website. These cookies normally contains unique information that identifies the user as well as any information that will be used in future accesses (such as user preferences [like light/dark mose]), and can be read and written to by the website to do functions that require information about previous requests.

   Django uses cookies to manage user session data by sending a session id that uniquely identifies the user and the current session to the browser as a cookie. The actual data is stored in the site database, to ensure data security. Django developers can use the session attribute of a request to write and read data of the current session (using the session id to access that data), thus managing the user session data.

__________________________________

## Are cookies secure to use? Is there potential risk to be aware of?

   Since cookies are in essence files sent from a website server and stored to a user's browser folder, there would undoubtably be security risks. A common example is the use of cookies by business analysts and advertisers to track a user's searching habits, thus infringing on the privacy of users without the user's knowledge nor consent. Even if the cookie isn't specifically meant to be used to infringe on the user's privacy (thus posing a security risk)m if implemented improperly without all security measures in place, attackers can use the use of cookies as a vulnerability. Some examples of cookie-based attacks.
   
   For example a website that uses unsecured cookies with no path nor domain are subject to cookie tossing attacks, where since there is no domain or path identified, if there are multiple cookies the website will choose one randomly to use, so if attackers 'tosses' fake cookies to the user and the website chooses to use that cookie, so once the user logs in, the hacker can hijack their session and use their account and access it's data. 

   CSRF (Cross-site request forgery) attacks refer to when users access a malicious website, in which the website accesses cookies used for reputable, innocent websites and embeds links in the cookies that when sent to the server can request the application to do an action (such as edit account info) without the user's consent, which could lead to loss or theft of information or services.

   If cookies sent are improperly encrypted (thus it isn't encrypted or it is easy to decrypt) attackers can capture the cookies during transmission and read the informationm stored in them, which could be very detrimental if login info or personal info is stored into those cookies

   There are still many more ways bad actors can use cookies to execute their schemes, such as cross site scripting, cookie overflow attack, session fixation etc. So unless you really trust the website and are confident that the cookies are properly implemented andhas up to date security measures, one might consider disallowing cookies from that website to ensure your security.

____________________________________

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

   * **Implement registration, login, and logout functions to allow users to access the previous application.**

   Firstly I imported redirect (from django.shortcuts); UserCreationForm (from django.contrib.auth.forms); messages (from django.contrib); authenticate, login and logout (from django.contrib.auth) and login_required (from django.contrib.auth.decorators) to views.py

   Then I made a register function that made a form (using the UserCreationForm class as the template), then requests input from the user, where if there has been no input from the user yet, will render register.html with the created form as context, where the user can input their registration details, otherwise if the form is filled and valid, the information will be saved to the server and the user will be redirected to the login page, with a message informing the user of the successful registration.

   Afterwards I made the register.html in the templates folder of the main application directory in which the form (which is defined in the regiter function) is represented as a table, with fields in which the user can input their registration details. Since we are using the UserCreationForm class as our template for our form, the fields that the user are asked to fill out is their username, their desired password, and confirmation that the password inputted is correct.

   To allow users to login I made my login_user function in views.py in which the user is asked for their username and password, which will be checked using the authenticate function (provided by Django). If upon authentication, it finds a user with that username and the password is indeed correct, it will log into the user's account and redirect the user to the main page (which we had made in previous Assignments). Otherwise, it will send an error message to the user stating that the username or password was incorrect and rerenders login.html.

   Then, I made the login.html template in the templates folder of the main application directory in which a Username and password is asked, with appropriate text fields to input that data, as well as a button underneath with the text login on it which will run the login_user function with the data inputted in the text fields as the username and password that will be authenticated. There is also a section underneath the button in which the messages that are made by successful registration and unsuccessful login will be displayed.

   To allow users to logout, I made a logout_user function, which will call the logout function provided by Django and redirects the user to the login page. Then I made a button in main.html found to the right of the 'Add New Item' button, that when clicked will call the logout_user function.

   To make it so the main page can only be accessed by users that have logged in I added the @login_required decorator, provided by Django, onto my show_main function, with the parameter of login_url as 'login' so if the user isn't logged in, the decorator will redirect the user to the login page  

   Lastly, in the urls.py file in the main application directory I imported all of the functions made for this assignment and added the following paths in the url_patterns list to define the url paths and which functions they call 

```
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```

   * **Create two user accounts with three dummy data entries for each account using the model previously created in the application.**

   I just registered 2 different accounts and made 3 items for one of them (but that's done after the next step. We only have to make 3 for one of them, because the other one will get the items made during previous Assignments, which I had 3 of)

   Proof:
   
   <img src="/assets/PBP_Assignment4_Account1.png">
   <img src="/assets/PBP_Assignment4_Account1.png">

   * **Connect Item model with User and display the information of the logged-in user, such as their username**

   In my models.py I imported the User class from django.contrib.auth.models. Then in my Item class/model I added a new attribute named user as a foreign key like so : `user = models.ForeignKey(User, on_delete=models.CASCADE)`, this linked the Item class to the User class, via the user foreign key, thus now every item has a User associated with it. 

   To actually facilitate the linkage of items to users in future item creation we have to change the create_item function in views.py, so that before the form is comitted to the database, it is first saved as an item variable and is assigned a user, the user being the person currently logged in to the website.

   Now that we have decided that our items will now be linked to user accounts, we must also show that in the main page. To do this I changed the show_main page so that the items list will filter according to th current user (so it will only show items linked to the current user) and changed the value of the 'name' key in the context dictionary to the username of the user (so now instead of displaying my name, it will display the user's name). 

   Lastly, to make the model change go into effect we run python manage.py makemigrations. IT IS IMPERATIVE THAT THERE IS AT LEAST 1 USER REGISTERED ON THE WEBSITE AT THIS STAGE. Since we had items previously that aren't linked to a user, it will throw an error. To resolve it I chose the option to change the user value of the previously created items, and set it to one (thus now those items are linked to the user with the id of 1, which would be the first user created. After that is resolved run python manage.py migrate to finalise the changes.

   * **Apply cookies, such as last login, on the main application page.**

   Firstly I imported datetime to views.py. After that I edited the login_user function so that instead of instantly returning the HttpResponseRedirect to main upon successful login, I first saved it as a response variable and set a cookie on that response named 'last_login', which holde the value of the current date and time, like so `response.set_cookie('last_login', str(datetime.datetime.now()))`, after which we can return the response. This makes it so that upon login it will record the time of login into a cookie stored by the user's browser under the name of last_login.

   I then added a new key value pair into the context dictionary like so: `'last_login': request.COOKIES['last_login'],`, which takes the cookie created upon login and sets the value of a variable called last_login as the value taken from the cookie. Then in main.html I added a line before the 'Add New Item' and 'Logout' buttons with the content "Last login session: {{ last_login }}" This will display the last_login value that was taken from the cookie onto the main page.

   Lastly, to delete the cookie upon logout I edited the logout_user function so that it doesn't instantly return the HttpResponseRedirect anymore, instead just saving it into a variable named response. Then we run the .delete_cookie method with the parameter 'last_login' on the response object, which will delete the cookie named last_login. After doing that, we can return response.

# PBP Assignment05

## Explain the purpose of some CSS element selector and when to use it.

   * **Element Selector**

   This selector applies a style on all elements that utilises the same html tag. For example if you want all of your titles with the tag of `h5` to all be blue, then you would use the element selector to define that all h5 tags will be blue. This allows developers to set a consistent style for a certain type of content throughout the entire website (or section that uses that style sheet), without having to think about adding a class nor id, serving as a sort of base line style that can be easily overwritten by more specific selectors

   * **ID Selector**

   The most specified selector, where we can define an ID in the style sheet, along with the style of that certain ID that will be used with the element that has that id. So you can define the the #background id to have a certain colour, thus allowing the developer to set the colour along with any other styles of the background to the relevant element by just adding id = "background" to the tag. As it is the most specified selector, it overrides all other selectors, thus allowing you to define properties/styles unique to only one element in a certain page. There's also the requirement that an element with an id should not shore the same id as another element, which ensures that the style is being used uniquely where it should, as well as it being easy to identify by both humans and other programs, allowing programmers to understand the use or identity of a certain element, and allow programs to search for a certain identity if it requires it. The reason why one might use the id selector in a style sheet rather than defining the style on the element itself, despite the fact that the id can only apply to one element on a webpage, is because it is a lot more readable using css than just a line of text, as well as the fact that the css can be used by multiple html templates, thus despite the fact that on any given webpage the id must be unique, the id can actually be reused on multiple webpages throughout the website, to define an element that is used througjhout the website (like a navbar that directs you to all parts of the website).

   * **Class Selector**

   Similar to the ID Selector, we can define a class in the style sheet, along with the style of that class that will be used by the element(s) that has that class. The difference with id however is that the class doesn't have to be unique, thus multiple elements within the webpage can have that style, which is useful for repeated types of elements (like when you have multiple cards representing multiple items) allowing easy reusability, by just declaring that the element is of a certain class in their tag. It is also more flexible than the element selector as the use of classes doesn't change all of the elements that need to use that tag, for example it allows you to define a class of images that are smaller and have different dimensions (maybe for cards) while not changing the images that don't have that class that need to remain normal size within the same webpage. Furthermore, one element can have multiple classes, so if it needs to implement certain attributes of multiple classes for the style of the element, one can do so, by just adding them all to the string for classes, separating each class with a space.

   Overall, selectors are used for reusability of styles, as well as allowing us to separate the styles from the templates, which helps with code readability (to a certain extent [having multiple classes does diminish readability]), so it is in our best interest to utilise such to allow for simpler, convenient and consistent implementation.
