# Milestone 3 Project – Recipe Remedy

Recipe Remedy is a demonstration of my learnings and knowledge of all the Code Academy Full Stack Developer Course modules learnt so far. This includes HTML, CSS, JavaScript, Python, Flask, MongoDB, Heroku, and Materialize.

Recipe Remedy is a fully responsive, self-built, database-backed, Flask web application. It has been designed and built with the user’s wants and needs first, whilst ensuring the site has user friendly and interactive design expectations.

You can view the live website here: [Recipe Remedy]( https://ms3recipe-mongo.herokuapp.com/

Using the philosophy of the CRUD model the website has been created to provide an online recipe blog which can be added to by a community of users, all users have to do is to sign up. Users are able to store, view, edit and delete their recipes. As well as create an account that will be recognised when they log back in. Users of the site can also view recipes without registering. However they will not have the function to add, edit or delete any existing recipes.

The target audience of the website are families who want to add their recipes, families who want to look for inspiration for meal times, people who are looking to expand their culinary knowledge and skills, anyone is welcome. 

Recipe Remedy has been a challenge for myself to compile ideas, designs, integrate structure from database to the user as well as get used to a fully automated library such as materialize. I can see and fully appreciate now the length of work that goes into a fully responsive and live site to ensure users can interact, add and edit their knowledge to a site for future projects.

You can view the live website here: [Recipe Remedy]( https://ms3recipe-mongo.herokuapp.com/ /)

## Contents
1. [**UX**](#UX)
    -  [**User Stories**](#user-stories)
2. [**Wireframes**](#wireframes)
3. [**Scope**](#scope)
4. [**Features**](#existing-website-features)
    -  [**Features To Add In The Future**](#features-to-add-in-the-future)
5. [**Design**](#design)
6. [**Technologies Used**](#technologies-used)
7. [**Tools Used**](#tools-used)
8. [**Testing**](#testing)
    -  [**User Story Testing**](#user-stories-testing)
9. [**Deployment**](#deployment)
    -  [**Deploying to Heroku**](#deploying-website-to-heroku)
    -  [**Clone & Run Locally**](#to-create-a-clone-of-the-reciperemedy-repository-and-run-locally)
10. [**Secret Key & Key Variables**](#secret-key-&-key-variables)
11. [**Design**](#design)
12. [**Credits**](#credits)
13. [**Acknowledgements**](#acknowledgements)


## UX
The site owner in spite of the pandemic situation thought it would be a great idea to create a sense of community and a way of broadening knowledge and horizons within food and cooking. With Recipe Remedy a user could come for quick meal ideas, inspiration for something new to try, or a project to maybe cook something ambitious.

The website already has some recipes from the site owner for others to share and follow. Also this gives an existing example of what the format looks like and enables users to have recipes readily available while the website is still new, also encourage other users to create a free account and share recipes of their own.

The website makes creating, reading, updating, and deleting recipes easy and simple for external users, with the function to share recipes to social media which can be found at the footer of the site.

## User Stories

## New External User Goals:
* As a new user I want to be able to view recipes
* As a new user I want to be able to register to the website and post my own recipes and to search for existing recipes.

## Frequent User Goals:
* As a frequent user I want to be able to continue to share my own recipes to the website in an easy way.
* As a frequent user I want to be able to find new recipes to cook from other users and see which users posted them.
* As a frequent user I want to be able to share recipes that I like to my social network pages

## Returning External User Goals:
* As a returning user I want to be able to edit/update my posted recipes
* As a returning user I want to be able to delete my posted recipes

## Site Owner User Goals:
* As the site owner I want to push my limits of my current skills as a developer whilst still creating a site that’s useful and beneficial for users.


## Wireframes
Using the user stories above, I put together the wireframes for Recipe Remedy using [Balsamiq](https://balsamiq.com/). The wireframes covered desktop, tablet and mobile formats. 

Due to the register function items on the NavBar changed depending on whether a user is logged in or not, additional wireframes were created to show what a registered and non-registered user would look like. When a user is registered they have full functions of the site such as add recipe, profile, and log out. 

[You can view all of the wireframes here](static/readme_docs/wireframes.jpg)

Below are is the homepage wireframes for desktop, mobile and tablet, with both navigation views for a registered in user, and non-registered user.

![Homepage Wireframes Desktop](static/readme_docs/wireframes_desktop.jpg)
![Homepage Wireframes Device](static/readme_docs/wireframes_device.jpg)

## Changes to Wireframes:
During creation the wireframes have changed dramatically. I did not realise the extent of work and knowledge I would need to create all the original functions I intended to have on the site. Originally I intended to have a live scroll through of various recipes that were popular on the site on the landing page, as well as a view my recipes button on the profile page. This was so registered users could go to their profile page once logged in and then view all their recipes they added with the click of a button.

I had also had a lot of about text on the landing page and had filled it with different cards. I found that although this is a typical layout of a recipe site, it did not fit with my design and aesthetic I wanted for the site. I wanted a site that looked quite simple, clean and accessible to all ages and users. I realised children might want to cook with parents so opted for a paired back, simplistic design that incorporated brighter colours and did not appear as intimidating with loads of text and cards on the site. 

I decided that the site needed a search function, This was so users could find recipes based on ingredients or recipe names to search for key words and then have recipes displayed with matches to these.

Added an image on Find a Recipe page: I feel images are important on websites in general, especially on food sites where it can be appealing to users, to one see what the finished product could look like, as well as use images as a way to engage with Instagram culture and get into maybe pulling in some internet traffic. If users engage with the lets give this recipe a go and then take their own pictures of the recipe and upload them with their own unique twists. Using hashtags from Instagram it could be another fun way in which the website could interact with another social media tool to help raise awareness to Recipe Remedy and pull in new users.
  
Adding form helpers: I decided to add form helper information to the following pages: ‘Add Recipe’ and ‘Edit Recipe.’ Initially, the helpers were to provide the user-specific instructions on how to upload a recipe to the website so that it would be formatted correctly (each item must be on a new line). Registering I realised I had put quite a secure password builder into the system and when family were testing they didn’t realise they needed a password with a captialised character as well as a unique character. So I found it useful to add these helpers for users to register.

## Scope
* Users can find recipes to cook themselves
* Users can register to the website
* User can submit their own recipes to the website
* Users can edit and delete their recipes from the website
* Users can search for recipes and search for foods they maybe fancy eating, or want to try cooking with.

## Existing Website Features

**Navigation Bar:** the navigation bar allows users to navigate to the relevant sections on the website, including register / login /log out, add own recipes, find a recipe and user profile page where they can see their displayed username as well as links to home page and add recipe. 

**Register:** The Register section allows users to register for the website so they can upload and edit/delete their own recipes. In the register section, users fill out a simple form for a username and password which they then use each time they need to login.

**Login:** Users can log into their accounts by using the simple username and password form and the details which they created their account with. Once logged in, users can add, edit and delete their recipes, as well as search for recipes by other users.

**Delete button:** Logged in users will be able to delete their own posted recipes by clicking on the delete button in the Full Recipe page. They will not be able to delete recipes posted by other users. I have also added a pop up modal, asking the user to confirm they want to delete their recipe. This is some defensive programming to ensure users don’t delete recipes by accident.

**Edit Recipe button:** Signed in users will be able to edit their own posted recipes by clicking on the edit button. They will not be able to edit recipes posted by other users. 

**Social sharing buttons:** Users will be able to share recipes they like to their social media channels via the social sharing buttons provided. Users will be able to share any recipe, even if they did not post the recipe. These social media buttons can be found at the footer of any page on the site.

**Order recipes by most recently added to see new ones at the top :** The view recipe page is ordered by newest posted recipe at the top. This makes it easier for returning users to see new content.

**Search functionality:** I decided to add a search function as this is essential and common practice on most sites. It also assists the user experience of the site. Users are able to type a search a full recipe name or word into the search bar and results would be displayed where the Recipe Name or Recipe Ingredients matched. Users can type partial words as well such as ‘ris’ for ‘risotto’ or ‘flour’ for ingredients in the recipe and a match will be made.

**The ability for a user to upload a photo to go with their recipe:** Users can add images to their posted recipe via the Add Recipe and Edit Recipe form by including a URL to the image. In any instance a user cannot provide a URL I have used some programming to ensure a default image will be displayed. This adds to the coherency of the site, as well as give users a chance to add an image at a later date if they wished to do so. The default image gives an idea of formatting to users as well.

**Security features:** The website uses [Werkzeug's](https://werkzeug.palletsprojects.com/en/1.0.x/) standard built in password hashing method for its log in security features to make the security authentication more secure. Werkzeug hashes the password  entered by the user (converts the password into another string) and then it is salted (additional data added). This makes the password very tough to crack. This was brought to my attention via the codeinstitute mini project videos and further research was compiled at another site which is referenced later.

**Flash messages:** Flash messages will appear on the website at the top of the page, under the main navigation. These appear for successful and non-successful registration, successful log in and out, successfully edited, deleted, and added recipes.

### Features to Add in The Future
Unfortunately my skill level did not allow me to fully realise all my ambition for this project. I am very happy with what I have achieved. However there are some functions to the site I would like to apply for the future. 

**Save/favourite recipes:** Signed in users would have the ability to save their favourite recipes so they can easily come back to them in the future, and time and time again. This would also tie in with the social media aspects I talked about before. In the future the site could evolve into a Instagram based site. In which users could just upload an image with the recipe attached and then other users who have registered and created account can interact with this to either save this with a like or uploads their own content and interact with other users for tips and hints.

**Have recipes that have been created by user to show up on their profile so users can see in one concise place what they have added to the site. This would be useful in case they wanted to see what their recipes were readily and easily. For now users will have to use the search function to do this.




## Schema Design
After researching and planning the elements of the website and the items needed to be stored in and retrieved from the database, I decided to have 2 collections:

**users:** for register and login this contains the Object ID, username and password.

**recipes:** containing the elements required for CRUD (create, read, update and delete). The values for the recipes collection are added into the database and pulled from the database by users in the sections ‘view Recipe’, ‘Add Recipe’, ‘Edit Recipe’ and 'Search Results' and also to delete a recipe from the database.


The keys for each collection were decided as follows:

### users:
**_id:** to be able to find the user by assigning a unique id

**username:** the username in which the user would like to recognised as when posting and editing recipes to the site.

**Password:** The password the user wants to be able to log into the website


### recipes:
**_id:** Unique identifier for the recipe

**cusine_type:** string in which users can add cuisine type which the recipe belongs to.

**recipe_name:** the name of the recipe user gives the recipe.

**ingredients:** ingredients of the recipe that user shares.

**method:** text describing the method to cook the recipe.

**image_url:** a url to be supplied by the user to add an image to their recipe

**created_by:** this records the name of the user which entered the recipe into the website

**date_added:** this records the date and time of when the recipe was entered

### categories: the category items are pre-set by the website owner and can only be changed by the website owner.
**_id:** the unique identifier for each category item 

	
I decided to use MongoDB to store the details entered into the database as it has been easy to use and has great capabilities to link up to the terminal. It also allowed a clear, easy and concise way to set up a simple relational database that was non SQL based.


## Technologies Used
I used a number of languages, frameworks and libraries to build this website. These include;

* [HTML](https://html.com/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) 
* [JavaScript](https://www.javascript.com/) 
* [JavaQuery](https://jquery.com/)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Materialize](https://materializecss.com/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
* [GitHub](https://github.com/)
* [GitPod](https://www.gitpod.io/)
* [MongoDB](https://www.mongodb.com/)
* [Heroku](https://www.heroku.com/)
* [Google fonts](https://googlefonts.com/)

## Tools Used
* [Balsamiq](https://balsamiq.com/) - Used to create my wireframes, showing the positioning of elements on varying screen sizes.
* [W3C HTML Validator](https://validator.w3.org/) - I used this tool to check the validity of my HTML code.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - I used this tool to check the validity of my CSS code.
* [Autoprefixed](https://autoprefixer.github.io/) - I used this tool to check the prefixes of my CSS code.
* [PEP8](http://pep8online.com/) - I used this tool to check that my app.py file meets the PEP8 requirements.


## Testing

**PEP8 Compliance:**
I used the website [PEP8](http://pep8online.com/) to check my app.py files complied with the PEP8 requirements. 


1st test: passed with no errors. 
This was due to the help of code institute mini project guide of how Pep 8 works and a pre warning of what to look out for, as well as constructing lines of code.


**W3C CSS Validator**
I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to check the validity of my CSS code.
* 1st test: Spacing errors. No errors to limit coding or clashes.

**W3C HTML Validator**
I used the [W3C HTML Validator](https://validator.w3.org) to check the validity of my HTML code on all 11 pages.
* base.html
    *Error: Bad value {{ url_for('log_in') }} for attribute href on element a: Illegal character in path segment: { is not allowed. This showed for every page that had a url for tag.
* index.html
    * Passed with no errors
* add_recipe.html
    * Passed with no errors
* edit_recipe.html
    * No errors
* recipe.html (Find a Recipe page)
    * Passed with no errors
* search.html
    * Error displayed: IO Error: HTTP resource not retrievable. The HTTP status from the remote server was: 500.
    * I think this error is because the page usually displays the results of a search, but checking this url in the HTML checker will display an error as it is unable to check the page on its own and does not have the search result information.
* register.html
    * Passed with no errors
* login.html
    * Passed with no errors
* logout.html
    * Passed with no errors
* full_recipe.html
    * Passed with no errors
* profile.html
    * No errors

## User Stories Testing:
**New External User Goals:**
*As a new user, I want to be able to view recipes to cook*
* There are 2 Call To Actions to direct a new (and also returning) user to view all the website recipes. The first and main Call To Action is in the navigation header under ‘All Recipes.’ This link is visible to all users, as well as users who are logged in, a permanent feature. Underneath that there is also a recipe of the month card beneath the landing page about text, which leads users to recipes page as well if they click on that.

*As a new user, I want to be able to register for the website and post my own recipes*
* Thanks to ‘Register’ on the main navigation bar, forwarding a user to the register function is very clear. Also on the login page. There is a prompt to link new users to register for an account if they don’t already have one.
* With the register button in the main navigation, the user will be able to click on this button no matter there they are currently on the site.

**Frequent User Goals:**
*As a frequent user, I want to be able to share my own recipes to the website and with the community in an easy way*
* Once logged in using one of the options above, an ‘Add Recipe’ item will appear in the main navigation. The add recipe function will also appear as a button on the landing page next to all recipes button. It will also appear on profile which is a new function only given to registered users. The Add Recipe page is a simple form-based page which the user can fill out to be able to add their own recipes.
* The form also includes some additional instructions for the user to follow when uploading their recipes to assist them with the form.

*As a frequent user, I want to find new recipes to cook*
* Recipes on the ‘view Recipe’ page have been organised to display the newest recipes first, making it easy for a returning visitor to be able to view new recipes, rather than need to look for them.
* •	A search function is also available to the user on this page so that they can add in a key word or phrase, and have all results matching that keyword or phrase returned. If there are no results found, a message will appear to the user stating this and directing them back to the all recipe/search page. The engine searches for the word or phrase in the Recipe Name and Recipe Ingredients field. This allows users to be able to search for a wider range of fields to access certain recipes or ingredients they wish to look for.

*As a frequent user, I want to be able to share recipes that I like to my social network pages*
* Social share buttons have been added to the footer of every page. This allows the website user to share that particular recipe to social pages.

**Returning External User Goals:**
*As a returning user, I want to be able to edit/update my posted recipes*
* Users can edit their own recipes easily. Once on the ‘View Recipe’ or ‘Full Recipe’ page, the user will be able to see an ‘Edit Recipe’ button, beneath the ‘full Recipe’ button or on the full recipe page above the delete button in the snippet card. This will take them to a full Edit Recipe form which exactly the same as the Add Recipe page. The only difference is that the fields are already input with pre-existing data that users can edit accordingly. This saves users typing out the whole thing again. Users can replace the information in the form, then update the recipe to the database and also to the site.
* Users will only be able to see an ‘Edit Recipe’ button once they are logged in and it will only be displayed on for recipes they added to the website from their usernames.

*As a returning user, I want to be able to delete my posted recipes*
* Within the view Recipe and full recipe page there is a delete button at the bottom of all the button functions that says ‘Delete Recipe.’
* Once clicked, the recipe will not be immediately deleted, instead a modal will pop up to confirm to the user do they want to delete their recipe. Upon clicking yes, the recipe is removed from the website, as well as the database.

**Site Owner:**

[View the full testing document here](static/readme_docs/full_testing_document.pdf)


## Deployment

### Deploying Website To Heroku
By deploying Recipe Remedy to Heroku, I was able to run my Python app and view a live version of the website which updated with each push I made. This link is also shareable to other users to be able to test the site.

1. In the terminal, I created a requirements.txt and Procfile using the following commands:
    1. pip3 freeze –local > requirements.txt
    1. echo web: python app.py > Procfile (be sure to create this file with a capital P)
1. Commit the new files to GitHub
1. Within my Heroku.com account I create a new App called metablog and chose the region closes to me, Europe.
1. Within the deploy sections which opened automatically after creating the app, I selected the Deployment Method of Connecting to GitHub via the logo. 
1. Beneath this I typed the GitHub repository name metablog and hit search. When the correct repository was found I clicked the ‘connect’ button.
1. Next, I clicked on ‘Settings’, then in Config Vars, I clicked ‘Reveal config Vars’. I filled out the Config Vars with the following information:

Config Vars | Config Vars
------------ | -------------
IP | To be added by user
PORT | To be added by user
SECRET_KEY | To be added by user
MONGO_URI | To be added by user
MONGO_DBNAME | To be added by user

7. In Deploy, I clicked ‘Enable Automatic Deploys’ and deployed from the Master branch.
8.	Follow this I then clicked ‘Deploy Branch’ and the app was deployed successfully at the URL metablog.herokuapp.com

### To Create a Clone of the Recipe Remedy Repository and Run Locally
Cloning the repository makes a copy of the repository which you download and store on your machine locally.

To make a clone of Recipe Remedy, follow the following steps:
1. Visit the main repository of Recipe Remedy[here](https://github.com/Michaelstanden/ms3recipe-remedy)
1. Above all the repository files and folders, you will find two Green buttons. Click on the one displaying ‘Clone’ with a downward arrow and a download icon.
1. With the ‘HTTPS’ method selected, click the ‘copy’ button next to the URL. Here you will find the link you will need to copy. The link to copy recipe remedy is: https://michaelstanden.github.io/ms3recipe-remedy/
1. Open the working directory where you want the repository to be cloned to, and in the terminal use the command and hit enter: 
        git clone https://michaelstanden.github.io/ms3recipe-remedy/
1. All the files will now be cloned into your chosen workspace.
1. Add a env.py file with the following details:
	    Import os
	    os.environ.setdefault("IP", "To be added by user")
        os.environ.setdefault("PORT", "To be added by user")
        os.environ.setdefault("SECRET_KEY", "To be added by user")
        os.environ.setdefault("MONGO_URI", "To be added by user")
        os.environ.setdefault("MONGO_DBNAME", "To be added by user")

Do not commit this page.

1. Create a file named  .gitignore  with the contents simply .env.py

1. To install the modules required on the requirements.txt file, run the command:
	pip3 install -r requirements.txt

1. You can run the code using the command:
	python3 app.py


## Secret Key & Key Variables
Secret keys should not be pushed to GitHub, or shared with anyone. To avoid this happening, I included my Secret Key and key variables in a file which is stored locally.

The file env.py includes these key variables and secret key. 

To stop this file being pushed to GitHub when commits are made and pushed, I created a .gitignore file which included the file name within it. Every time commits are made and pushed, the env.py file is ignored.


## Design

**Colours:**
I wanted to keep the colour pallet vivid with bright colours, using a striking an vibrant landing page hero image to set the tone and a sky blue background for all the pages to lift off the white tones of the recipe cards. I also researched that reds are associated in psychology with food and hunger so I have used all the buttons and navigations in red to highlight this in my food related website.


**Fonts:**
Both fonts I chose were from Google fonts.

Playfair Display: I liked this font as it is rustic looking but still easy to read. It is also when researching a popular similar font type to use on recipe and food websites.

Piazolla. This is to break up some of the generic text on the site and make it different to the headings and other texts.

Open Sans: Pairs nicely with Playfair when looking on googlefonts suggestions. It also highlights the headings text I needed it for. 

## Credits

**Images:** All homepage images are google images. Images used within recipe submissions have been submitted via me and testers using URL links to external sources and are not owned by me or Recipe Remedy.


**Recipes:** All recipes added by users, and myself Michael Standen. 


## Acknowledgements

Special Thank you to my fantastic mentor ANTONIO RODRIGUEZ for helping me with my ideas and for reading through my code with a fine tooth comb whilst pushing me to my limits on the project and better myself as a coder.

A huge thank you to fellow student and slack member DANTE HEALY for reviewing my website in great detail in private chat channel and making some suggestions for improving the website as well as flaws they saw.


I would also like to say many many thanks to the Tutors who helped me solve the late night frustration of bugs. These include Tim_ci, Johann Alberts. You have allowed me to sleep at night. 


