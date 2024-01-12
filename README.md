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
 
 * 

 * 

 * 

## _Implemented Features_

 * 

 * 

 * 

 * 
  
## _Features to be Implemented_

 * .

# _Design_
 
 * This flow chart shows how the game responds within the different sections.

 * This flow chart will Help through the testing to determine whether the game responds as it should.

 ![Flow Chart](documents/readme-images/flow-chart.png)

# _Bugs_

 * Through testing there are no current known bugs within the game
 
 _Testing_


# _Validation_

 * This game passes through the [Code Institute PEP8](https://pep8ci.herokuapp.com/) Validator with no errors.

![Validation](documents/readme-images/validation.png)

# _Technologies_

 * Python/ Django programming language to produce the backend functionallity.

 * HTML and CSS is used for the Frontend UI
 
 * Bootstarp 5.3.2 is used with in the Frontend UI
  
 * [ElephantSQL](https://www.elephantsql.com/) is used to the database storage.

 * [Cloudinary](https://cloudinary.com/) is used For the static file and image storage

 * [LucidChart](https://www.lucidchart.com/pages/) used to create the flow chart showing the website functionality and flow.

 * [GitHub](https://www.github.com) was used to hold the website repository files.

 * [Gitpod](https://www.gitpod.io) was used for the coding environment.

 * [Heroku](https://www.heroku.com) was used to deploy the website to the web.


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