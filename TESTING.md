# _Test Menu_

- [Test Menu](#test-menu)
- [Functional Testing](#functional-testing)
    - [Authentication](#authentication)
    - [Products](#products)
    - [Starters](#starters)
    - [Starter Dishes](#starter-dishes)
    - [Main Courses](#main-courses)
    - [Main Course Dishes](#main-course-dishes)
    - [Sauces](#sauces)
    - [Sides](#sides)
    - [Desserts](#desserts)
    - [Dessert Sauces](#dessert-sauces)
    - [Dessert Dishes](#dessert-dishes)
    - [Menus](#menus)
    - [Navigation](#navigation)
    - [Footer](#footer)
- [Bugs](#structure-plane)
- [Validation](#features)
    - [PEP8 Valadator](#implemented-features)
    - [W3 Valadator](#site-features)
    - [Lighthouse Report](#home-page)
- [Responsiveness](#header)
## _Functional Testing_

### _Authentication_

Description:

Ensure a user can sign up to the website

Steps:

1. Navigate to [sizzle-and-steak](https://sizzle-and-steak.herokuapp.com) and click Register
2. Enter email, username and password 
3. Click Sign up

Expected:

An email is recieved with a link to sign up, upon clicking the link, registration is successful

Actual: 

An email is recieved with a link to sign up, upon clicking the link, registration is successful

<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Navigate to [sizzle-and-steak](https://sizzle-and-steak.herokuapp.com)
2. Enter login detailscreated in previous test case
3. Click login

Expected:

User is successfully logged in and redirected to the home page

Actual:

User is successfully logged in and redirected to the home page

<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click confirm on the confirm logout page

Expected:

User is logged out

Actual:

User is logged out

### _Products_

Description:

Ensure a new booking can be created.

Steps:

1. Navigate to [page](https://sizzle-and-steak.herokuapp.com/booking/createbooking/) - Login if prompted.
2. Enter the following:
    - Name: Gareth
    - No Of Guests: 3
    - Date: Any future date
    - Time: Any drop down field
3. Click Create

Expected:

Form successfully submits and a toast is shown to alert the user of successful booking.

Actual:

Form successfully submits and a toast is shown to alert the user of successful booking.

<hr> 

Description:

Ensure a booking can be edited.

Steps:

1. Navigate to [page](https://sizzle-and-steak.herokuapp.com/booking/managebookings/) - Login if prompted.
2. Enter the following:
    - Name: Gareth
    - No Of Guests: 5
    - Date: Any future date
    - Time: Any drop down field
3. Click Create

Expected:

Form successfully submits and a toast is shown to alert the user of updated booking.

Actual:

Form successfully submits and a toast is shown to alert the user of updated booking.

<hr>

Description:

Ensure user can successfully delete a booking.

Steps:
1. Login as a user with a booking or create a new booking
2. Click the Manage Booking nav link
3. Click the delete button on a booking
4. Click the confirm button on the delete page

Expected:

Booking is successfully deleted

Actual:

Booking is successfully deleted

<hr>
### _Desserts_

Description:

Ensure a new menu item can be added

Steps:

1. Navigate to the create menu item page from the menu drop down nav item
2. Enter the following details:
    - Name: Test Menu
    - Type: Starter
    - Description: Test Item
    - Price: 15.00
    - Checkbox: Contains Nuts

3. Click Create

Expected:

New menu item is sucessfully added and can be added to a new menu

Actual:

New menu item is sucessfully added and can be added to a new menu

<hr>

Description:

Ensure a new menu can be created

Steps:

1. Sign in as a staff user
2. Select the Create Menu item in the Menu drop down nav bar
3. Enter the follow details:
    - Name: Test Menu
    - Starters: Chicken Veg Soup
    - Mains: Chicken Supreme
    - Deserts: Choclate Cake
    - Drinks: Coke
    - Sides: Chips
4. Click Create

Expected:

New menu is created and can be viewed on the View Menus page

Actual:

New menu is created and can be viewed on the View Menus page

<hr>

Description:

Ensure a menu can be updated

Steps:

1. Navigate to the manage mennus page from the menus drop down nav link
2. Click edit on a menu
3. Update a menu item and submit the form

Expected:

Menu has been updated and a toast message displayed to the user it was updated

Actual: 

Menu has been updated and a toast message displayed to the user it was updated

<hr>

Description:

Ensure a menu can be deleted

Steps:

1. Navigate to the manage menus page from the menus drop down nav link
2. Click the delete button on a menu
3. On the delete confirmation page click confirm

Expected:

Menu has been deleted and cannot be seen on the menus page

Actual:

Menu has been deleted and cannot be seen on the menus page

<hr>

### _Starters_

### _Starter Dishes_

### _Main Courses_

### _Main Course Dishes_

### _Sides_

### _Sauces_

### _Desserts_

Description:

Ensure a new menu item can be added

Steps:

1. Navigate to the create menu item page from the menu drop down nav item
2. Enter the following details:
    - Name: Test Menu
    - Type: Starter
    - Description: Test Item
    - Price: 15.00
    - Checkbox: Contains Nuts

3. Click Create

Expected:

New menu item is sucessfully added and can be added to a new menu

Actual:

New menu item is sucessfully added and can be added to a new menu

<hr>

Description:

Ensure a new menu can be created

Steps:

1. Sign in as a staff user
2. Select the Create Menu item in the Menu drop down nav bar
3. Enter the follow details:
    - Name: Test Menu
    - Starters: Chicken Veg Soup
    - Mains: Chicken Supreme
    - Deserts: Choclate Cake
    - Drinks: Coke
    - Sides: Chips
4. Click Create

Expected:

New menu is created and can be viewed on the View Menus page

Actual:

New menu is created and can be viewed on the View Menus page

<hr>

Description:

Ensure a menu can be updated

Steps:

1. Navigate to the manage mennus page from the menus drop down nav link
2. Click edit on a menu
3. Update a menu item and submit the form

Expected:

Menu has been updated and a toast message displayed to the user it was updated

Actual: 

Menu has been updated and a toast message displayed to the user it was updated

<hr>

Description:

Ensure a menu can be deleted

Steps:

1. Navigate to the manage menus page from the menus drop down nav link
2. Click the delete button on a menu
3. On the delete confirmation page click confirm

Expected:

Menu has been deleted and cannot be seen on the menus page

Actual:

Menu has been deleted and cannot be seen on the menus page

<hr>

### _Dessert Sauces_

### _Dessert Dishes_

### _Menus_

### _Footer_

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook icon opened facebook in a new tab and the twitter icon opened twitter in a new tab. These behaved as expected.

## Negative Testing

Tests were performed on the create booking to ensure that:

1. A customer cannot book a date in the past
2. A customer cannot book if no tables are available for the amount of guests
3. A customer cannot edit a booking with an increased guest size if no tables have capacity
4. Forms cannot be submitted when required fields are empty




## _Bugs_
    After Testing the site there does not appeart to be any faults with the functions of the site main features.
    whit that in mind the only minor bug that can be seen at pressent is the messages outputed to the user after updating items with out redirecting are only shown when the page is reloaded.
    
## _Validation_

### PEP8 Valadator
    All file passed through the [Code Institute PEP8](https://pep8ci.herokuapp.com/) Validator after removing a few white spaces and Shortening a few line lenghts.

![PEP8 Validation](docs/testing/pep8-validation.png)

### W3 Valadator
    The site passed through W3 Valadator with just a few minor errors on carousel ids as they had same name, so after remaning them it passed.

![W3 Validation](docs/testing/w3-validation.png)

### Lighthouse Report

Lighthouse report has shownn areas to be improved. with the over all scores are not bad the best practice are being brought down by 
![Lighthouse v1](docs/testing/light-house-v2.PNG)

## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [sizzle-and-steak](https://sizzle-and-steak.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
-  Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen:

Oukitel C21 Pro
TCL 30 Pro
iPhone SE