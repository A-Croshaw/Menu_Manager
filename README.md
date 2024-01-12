# _Menu Manager_

![Giff-Image](documents/readme-images/game-gif.gif)

[_Click here to view live deployment_](https://menu-manager-32aec1a9f4d5.herokuapp.com)


# _Content Menu_

- [Menu Manager](#menu_manager)
- [_Content Menu_](#content-menu)
- [_Features_](#features)
  - [_Elements_](#game-elements)
  - [_Data Storage_](#data-storage)
  - [_Implemented Features_](#implemented-features)
  - [_Features to be Implemented_](#features-to-be-implemented)
- [_Design_](#design)
- [_Bugs_](#bugs)
-[_Testing & Validation_](#testing-&-validation)
  - [_Testing_](#testing)
  - [_Validation_](#validation)
- [_Technologies_](#technologies)
- [_Deployment_](#deployment)
  - [_1 - Version Control_](#1---version-control)
  - [_2 - Page Deployment_](#2---page-deployment)
  - [_3 - Cloning Repository_](#3---cloning-repository)
- [_Credits_](#credits)

# _Features_

## __
    


## _Elements_

### _1 



## _Data Storage_
 
 * The site data is stored on [ElephantSQL](https://www.elephantsql.com/) which is a ProsgreSQL based database.

 * Background image and the Static files are storded on [Cloudinary](https://cloudinary.com/).

## _Implemented Features_

 * 

 * **Favicon**
    * A favicon was implemented to Show the user that They still are pressent on site
    * This also provides an image in the tabs to allow the user to easily identify the website if they have multiple tabs open.

 * **403 Error**
  - A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content or actions.
  - This covers the actions of adding, updating and deleting of content for all users except those how are admin users.

 * **404 Error**
  - A 404 error page has been implemented to provide feedback to the user if they try to open a page that does not exist.

 * **500 Error**
  - A 500 error page has been implemented to provide feedback to the user that the server has encounted a problem.
  
## _Features to be Implemented_

 * Add Allergen Choices to the menu dishes
 * Add Costings to the recipes that then can generate 70% gdp for dishes and the menus.
 * Hide features on buttons as others sho during the adding og ingredients and steps on the recipe pages, also the elements, sauce and sides ont the dish pages.

# _Design_
 
 * This flow chart shows how the game responds within the different sections.

 * This flow chart will Help through the testing to determine whether the game responds as it should.

 ![Flow Chart](documents/readme-images/flow-chart.png)

# _Bugs_

 * Through testing there are no current known bugs within the game
 
# Testing & Validation

## Testing

  * Case testing with results can be found here in the [TESTING.md](TESTING.md) file. (This is separate to reduce the readme file size)

## _Validation_

 * This game passes through the [Code Institute PEP8](https://pep8ci.herokuapp.com/) Validator with no errors.

![Validation](documents/readme-images/validation.png)

# _Technologies_

 * **Python/ Django**
  - Python is the main proggraming language whilst using the django framework.
 * **HTML**
  - Used to for main website language.
 * **CSS**
  - For the styling for the website.
 * **Bootstarp 5.3.2**
  - Is used With in the site for different styling and for responsiveness.
 * **[UXWing](uxwing.com)**
  - Used for difrerent icons through out the site.
 * **Git**
  - Used to commit and push through out the development.
 * **[balsamiq](https://balsamiq.com/)**
  - wireframes were created using balsamiq.
 * **[TinyPNG](https://tinypng.com/)**
  - Was used to compress the background image 
 * **[cloudconvert](https://cloudconvert.com/webp-converter,)**
  - Was used to change image files to webp.
 * **[ElephantSQL](https://www.elephantsql.com/)**
  - Was Used as the main database storage.
 * **[Cloudinary](https://cloudinary.com/)**
  - Was used For the storage of static file and images.
 * **[favicon](https://favicon.io/favicon-generator/)**
  - Favicon.io was used to generate the favicon.
 * **[LucidChart](https://www.lucidchart.com/pages/)**
  - Was used to create the flow chart showing the website functionality and flow.
 * **[GitHub](https://www.github.com)**
  - Is the main repository site files.
 * **[Gitpod](https://www.gitpod.io)**
  - Was the main the coding environment.
 * **[Heroku](https://www.heroku.com)**
  - Is used to deploy the website to the web.


# _Deployment_

## _1 - Version Control_

 Verion controle was maintained using GIT within GitPod to push code to the GitHub repository

 * From the Gitpod terminal use "git add ." which tells git you would like to make changes/updates to the files.

 * Then use "git commit -m " with a comment, this will commit the changes and update the files.

 * Then using the "git push" command this will push the committed changes to your GitHub repository.

## _2 - Page Deployment_

 * Go to Heroku and log in

 * click "New" to create a new app from the dashboard

 * Choose app name and select your region, press "Create app".

 * Go to "Settings" and navigate to Config Vars.

 * Add Config Vars. 
    * This app used 4 confid vars 
        * for the clouninary (KEY: CLOUNDINARY_URL / VALUE: *****)
        * for the database (KEY: DATABASE_URL / VALUE: ****** )
        * KEY: SECRET_KEY / VALUE:*******
        * KEY: PORT / VALUE = 8000.
 
 * Now go to the Deploy tab.
 
 * Scroll Down to Deployment Method and select GitHub.
 
 * Select repository to be deployed and connect to Heroku.
 
 * Now Scroll down to depoly : 
    * Option 1 is selecting Automatic deploys (Will Update Automaticly when every git push to the repository).
    * Option 2 is selecting Manual deploy (Needs to be redeployed after every change manually via Heroku deploy tab).

 Visit the live deployment [HERE](https://menu-manager-32aec1a9f4d5.herokuapp.com).

## _3 - Cloning Repository_

 * To clone the repository for download or use within your GitHub head-over to this [link](https://github.com/git-guides/git-clone) 

# _Credits_

  * I used [python.org](https://www.python.org/) for References for the Pyhton code and functionality

 * I used [w3schools](https://www.w3schools.com/python/default.asp) for References for the Pyhton code and functionality

 * I used [stackoverflow](https://stackoverflow.com/) for References for the Pyhton code and functionality

 * I Used [Django Docs](https://docs.djangoproject.com/en/5.0/) to the reference for the django code and functionality