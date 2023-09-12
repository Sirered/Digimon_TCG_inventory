# PBP Assignment02 

## How did I implement the tasks on the checklist?
* ***Create a new Django project.***

   First I had to think of what I wanted to make for this assignment. One of the requirements for the project is that it must be an inventory management application. As a giant fan of card games and recently being
   interested in the Digimon card game, I decided to make my application a Digimon TCG inventory manager. With my plan set, I started by making a local directory (named `Digimon_TCG_inventory`) on my laptop and
   initiated git on it. I then made a Github repository online (with the same name) and connected it to the newly created local directory, thus allowing me to push changes made on my laptop to the online repository,
   which will be utilised to deploy the application. I then setup and activated a virtual environment to isolate my project, preventing other modules outside the project from causing any problems. Next using the
   python pip installer, I downloaded all modules required to make and run the django application, by reading the requirements from a txt file (appropriately named `requirement.txt`). Lastly to finally create the
   project I configured the `settings.py` file to allow access from any host for testing purposes and executing the startproject command from the django-admin module (by running `django-admin startproject
   Digimon_TCG_inventory` on command line).
