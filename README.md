# StarLight

Starlight is an online platform for personalized esoteric services! Starlight offers a variety of services, including tarot readings, rune interpretation, and astrological chart creation available conveniently and affordably directly on the website. Users can register and schedule consultations online with ease, ensuring a personalized and seamless experience.

![Starlight website shown on a range of devices](/static/images/docs/responsive.png)  

## Demo
The live demo is available [here](https://starlight-consultations-2b1105ac431c.herokuapp.com/)!

## Contents

* [User Experience](#user-experience)
  * [Website Overview](#website-overview)
  * [User base](#user-base)
  * [Website Goals](#website-goals)
  * [Flowchart](#flowchart)
  * [ERD](#erd)

* [User Stories](#user-stories)
  * [Epics and User Stories](#epics-and-user-stories)
  * [Agile development](#agile-development)

* [Design](#design)
  * [Color Palette](#color-palette)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
    
* [Features](#features)
  * [General Features on Page](#features)
  * [Features and resources to be added in the future](#features-and-resources-to-be-added-in-the-future)
  * [Accessibility](#accessibility)

* [Testing](#testing)
  * [User Story Test](#user-story-test)
  * [Tested Browsers and Devices](#tested-browsers-and-devices)
  * [Manual Testing](#manual-testing)
  * [Validator Testing](#validator-testing)
  * [Bugs](#bugs)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment](#deployment)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)


## User Experience

### Website overview 

Starlight is a fictional website I created to offer online consultations for Tarot, Runes, and Astrological Charts. It was developed with the intention of providing an engaging and informative experience for users interested in divination and esoteric exploration. Every aspect of the site, from design to content, has been planned to ensure easy and intuitive navigation.

### User base

Individuals interested in Tarot, Runes, and Astrological Chart consultations, seeking guidance and insights on personal, spiritual, and emotional matters. This may also encompass those wishing to explore alternative methods of self-discovery and personal growth, as well as individuals seeking online support to share spiritual experiences and obtain consultation services.

### Website Goals  

The goal of the Starlight platform is to provide a comprehensive and user-friendly experience for individuals seeking guidance in Tarot, Runes, and Astrology. The website aims to:

Users:

* Facilitate navigation to discover available consultations with experienced practitioners.
* Enable easy scheduling of consultations with consultants based on preferred dates and times.
* Offer informative resources to deepen understanding of divination practices and spiritual exploration.
* Enhance user experience through intuitive design and functionality for a pleasant browsing experience.

Administrators:

* Maintain an efficient and updated scheduling system.
* Facilitate communication between users and consultants.
* Ensure the security of user data.
* Enable regular updates to the "About" page, providing detailed information about the services offered and the platform's philosophy.

### Flowchart

In the planning stage, I drafted a basic structure that depicted the desired functionality and interaction for the project.

As development progressed, I identified elements that needed to be included and others that required a different order of operation. These changes were gradually incorporated into the initial outline. The outline was conceived using the Lucidchart tool.

![Starlight Flowchart](/static/images/docs/flow.png)

### ERD

In order to provide a clear visual representation of the database structure, an Entity-Relationship Diagram (ERD) was developed using a Database Designer tool.

![Starlight ERD](/static/images/docs/erd.jpg)


## User Stories

### Epics and User Stories
During the project development, the creation of epics, user stories, acceptance criteria, and tasks was crucial in guiding and successfully concluding the project. These elements provided a clear and detailed framework for planning and executing activities, ensuring alignment with the project's objectives and expectations. Among them were:

#### EPIC 1: Set Up
 The 'Set up' epic encompasses the activities required to establish the initial development environment of the project, including installing tools, configuring version control systems, and organizing the project structure.

  * User Story: Early deployment

As a developer, I can deploy an initial version of the application on Heroku so that I can verify the functionality of the initial setup and continue testing the application during development.

  * User Story: Setting Up Initial Django Project Structure

As a developer, I can establish the foundational structure of a Django project for a reservation website so that I can ensure smooth progression in both development and deployment.

  * User Story: Database Integration 

As a developer I can establish database connectivity and media storage so that user data is successfully stored.

#### EPIC 2: Admin Dashboard

The Admin Dashboard epic aims to create a  interface for administrators to manage various aspects of the website or application efficiently. This includes functionalities such as user management, content moderation and configuration. 

  * User Story: Website Administration Control

As an administrator, I can manage users, content, and settings on the website so that I can ensure a consistent and high-quality experience for end users.

  * User Story: Administrative Interface

As a developer, I can develop an intuitive administrative interface for administrators to efficiently manage users, content, and settings so that the website can be effectively controlled and maintained.

#### EPIC 3: About Page

The About Page epic aims to improve the "About" section of the website, providing users with a more informative and engaging experience. This includes updating the page content, enhancing its visual design, and ensuring that it clearly conveys the company's message and values.

  * User Story: View About Page 

As a site user, I can access the "About" page to obtain information about the company, team, or project so that I can learn more about its background and objectives.

  * User Story: Manage About Page Content

As an administrator, I can edit and update the content of the "About" page as needed so that I can keep it up-to-date with the latest information.

#### EPIC 4: Booking System

The Booking System epic addresses the implementation of a system that allows users to make reservations for services offered on the website, while providing administrators with the necessary tools to efficiently manage these bookings. This involves creating intuitive interfaces for users to make reservations, as well as an administrative panel for administrators to manage all bookings.

  * User Story: Make Online Booking

As a user, I can to be able to make an online booking to schedule a consultation with one of the services offered on the website so that I can easily arrange an appointment at my convenience.

  * User Story: Manage Bookings

As an administrator, I can access the admin dashboard to manage bookings, ensuring efficient organization and oversight of all scheduled appointments, so that I can effectively coordinate and optimize the booking process.


#### EPIC 5: User Authentication

The User Authentication epic deals with implementing a system for user registration, login, and logout on the website. This enables users to create accounts, log in to access exclusive features, and log out when they wish to exit. The goal is to ensure the security of user accounts and provide a seamless and secure user experience.

  * User Story: Register Account

As a user, I can register an account so that I can access additional services on the website.

  * User Story: User Login

As a user, I can to be able to log in to my account so that I can access personalized features and services on the website.

  * User Story: User Logout

As a user, I can to be able to log out of my account so that I can securely end my session on the website.

#### EPIC 6: Accessibility

The Accessibility epic aims to ensure that the website is accessible to all users, regardless of their abilities or needs. This involves implementing features and practices that make the site easy to use and understand for all users. 


  * User Story: Website Accessibility

As a user, I can navigate the website with ease and access all content so that I can have an inclusive browsing experience and access information effectively.


  * User Story: Accessible Features

As a developer, I can implement accessible features on the website to ensure a positive user experience for all users, so that everyone can access and effectively use the website.


#### EPIC 7: Project Documentation

The Project Documentation epic aims to create comprehensive documentation that clearly explains the purpose, functionality, and usage of the project. This includes crafting a README.md file to provide detailed information about the project. 

  * User Story: README Documentation

As a developer, I can create a README.md file to document and present the project, ensuring that everyone can easily understand the purpose, functionality, and usage of the project.


#### EPIC 8: Project Testing

This epic focuses on comprehensive testing procedures to ensure the reliability, functionality, and usability of the project. It involves documenting testing procedures, conducting backend and frontend tests, evaluating compatibility, and gathering user feedback for UI improvements. The goal is to ensure high-quality and usability of the software before deployment.

  * User Story: Testing Procedures

As a developer, I can thoroughly test the project so that I can ensure its quality and usability.


### Agile development

Throughout the project development, I adopted an agile methodology, utilizing Kanban to manage my activities and projects. Kanban provided a clear view of the workflow, allowing me to track task progress visually and in real time. I organized my project on GitHub, using a Kanban board to divide tasks into columns such as "To Do," "In Progress," and "Done."



![Starlight Agile development](/static/images/docs/agile.png)


For more details on the project management process, you can access the link [here](https://github.com/users/BrunaRihl/projects/6).



## Design

### Color palette

The choice of colors for the website was carefully planned, with shades of purple and lilac being selected for their association with spirituality, intuition, and calmness. These colors were chosen to create a pleasant and engaging atmosphere for users, conveying a sense of serenity and sophistication while reflecting the brand's identity and value proposition. Additionally, the strategic use of contrast was taken into account to facilitate website navigation and readability, ensuring a more intuitive and accessible experience for all visitors.

![Starlight website color palette](/static/images/docs/palette.png)

### Typography 

Google Fonts was utilized to incorporate the selected font styles into the website. 

I selected 'Montserrat Alternates' for the body text due to its clean and contemporary appearance, enhancing readability across various content sections. As for the logo, I chose 'Mystery Quest' to evoke a sense of mystery and intrigue, aligning with the mystical theme of the website while adding a unique touch to the brand identity.

![Starlight fonts](/static/images/docs/fonts.png)  

### Imagery 

The selected images for the website aim to immerse users in the realm of consultations offered by the consultants. I ensured they were of good resolution, seamlessly integrating with the colors and theme of the site. The goal was to provide a visually engaging and cohesive experience, connecting users to the spiritual environment of the consultations while facilitating understanding of the services available for booking through the platform.

### Wireframes

I developed a simple wireframe, aiming to ensure a consistent experience across mobile devices and computers.

I made some adjustments in relation to what I had planned for positioning and added some buttons to enhance functionality and user experience, aiming to ensure the website is accessible and enjoyable on any platform.

#### Desktop
<details>
  <summary>Home
</summary>

![Starlight wireframe](/static/images/docs/home-desk.webp)  

</details>
<details>
  <summary>About
</summary>

![Starlight wireframe](/static/images/docs/about-desk.webp)  

</details>

</details>
<details>
  <summary>Booking
</summary>

![Starlight wireframe](/static/images/docs/book-desk.webp)  

</details>


#### Mobile
<details>
  <summary>Home
</summary>

![Starlight wireframe](/static/images/docs/home-mob.webp)  

</details>
<details>
  <summary>About
</summary>

![Starlight wireframe](/static/images/docs/about-mob.webp)  

</details>

</details>
<details>
  <summary>Booking
</summary>

![Starlight wireframe](/static/images/docs/book-mob.webp)  

</details>

## Features

The website comprises three primary pages: a welcoming home page, an informative about page, and a convenient booking page.

### Navigation bar 

* All pages feature a responsive navigation bar at the top of the screen.

![Starlight nav](/static/images/docs/nav-not-log.webp)  

* In the top-left corner, the site's logo is displayed, allowing users to return to the homepage with a single click.
* Navigation adaptation on smaller screens such as tablets and smartphones is automatic. These features were implemented using the Bootstrap framework, ensuring smooth and responsive navigation. On mobile devices, the navigation bar is transformed into a hamburger menu to optimize the user experience.

![Starlight nav](/static/images/docs/nav-mob.png)  

* The menu provides links to the main pages of the site, including Home, About, Booking, Register, and Login/Logout.
* To assist users in navigating the site, a visual effect has been added to highlight menu items when the mouse cursor hovers over them.
* The "Booking" option is displayed only for logged-in users, remaining hidden for non-authenticated users.

![Starlight nav](/static/images/docs/nav-login.webp)  

* Additionally, when the superuser is logged in, an additional option is provided in the menu, allowing direct access to the administrative control panel.

![Starlight nav](/static/images/docs/nav-admin.webp)  

#### Authentication Status

A functionality has been implemented on the website that displays a message below the navigation bar, informing whether the user is logged in or not. This message allows users to easily identify their authentication status while browsing the site.

* Logged in:

![Starlight auth](/static/images/docs/auth-log.webp)

* Not logged in:

![Starlight auth](/static/images/docs/auth-not-log.webp)


### Sign Up Page

- On the registration page, new users can start their journey on Starlight by creating a personalized account. Here, users provide essential information such as name, email address (optional), and password to establish their identity in the system.

![Starlight sign up](/static/images/docs/signup.webp)

- During the registration process, each user is prompted to choose a unique username, ensuring uniqueness among all accounts. Additionally, the system checks if the provided email address has not already been registered.

![Starlight sign up](/static/images/docs/signup-error.webp)

### Login Page
- On the login page, registered users can access their existing accounts on Starlight. Using a simple form, users input their credentials, including username and password, to sign into the system. Once authenticated, users have immediate access to the site's personalized features, allowing them to explore and utilize the available functionalities.

![Starlight sign up](/static/images/docs/login.webp)

### Logout Page

-  The logout page provides users with a convenient way to end their sessions on Starlight. By clicking the "Logout" button, users are logged out of their accounts, ensuring the privacy and security of their information. Upon logout completion, users are redirected to a confirmation page and then to the homepage, providing a seamless and secure experience.

![Starlight logout](/static/images/docs/signout.webp)

#### Notification messages

Starlight displays warning messages at crucial moments of user interaction with the platform. Upon successfully completing registration, logging in, or logging out, clear and informative messages are displayed on the screen to confirm the actions taken. These messages provide immediate feedback to the user, ensuring an intuitive and transparent user experience.

![Starlight notifications](/static/images/docs/signout-mess.webp)

![Starlight notifications](/static/images/docs/login-mess.webp)

### Home Page 

### Favicon

A website features a custom favicon that has been added to the browser's header. The favicon showcases a moon and a star, matching the theme and colors of the site, providing a unique visual identity for it.

![StarLight - favicon](/static/images/docs/favicon-docs.webp)


#### Header: 

* The main image showcases hands manipulating a tarot card deck, aligning with the central theme of the site about tarot readings, rune consultations, and interpretations of astral maps.
* The overlaid message provides a brief introduction to the website's concept, while the high resolution and vibrant colors ensure an inviting presentation to visitors.

![Starlight - image hero](/static/images/docs/header.webp)

#### Sections: 

* Below the main image, users will find the "Our Team" section.

  * This section highlights the services offered by the site, such as tarot readings, rune consultations, and interpretations of astrological charts.

  * Using Bootstrap cards, each service is presented concisely, providing an overview of what the site offers to users.

![Starlight Our Team](/static/images/docs/our-team.webp)


* Additionally, there's a "Book Now" section, where users can schedule consultations directly through the site.

  * If the user is logged in, a "Book Now" button is displayed, allowing them to proceed with scheduling.

![Starlight book now](/static/images/docs/book-sect-login.webp)

  * If the user is not logged in, a "Login First" button is shown, prompting them to log in before booking an appointment.


![Starlight book now](/static/images/docs/book-sect.webp)


### About page: 

The "About" page provides a detailed insight into the purpose and services available on the site. 

#### Key Highlights:
  * Flexible Content: The administrator can easily update the content of the "About Us" page using the Django admin panel.

  * The featured image on the "About" page is customizable using Cloudinary. This allows the page administrator to easily upload and edit the image to reflect the identity of their company or brand.

![Starlight about](/static/images/docs/about-page.webp)

  * Update Information: The date of the last update is displayed on the page so that visitors know when the content was last revised.

  * If the user is logged in, a "Book Now" button is displayed, if the user is not logged in, a "Login First" button is shown.


![Starlight about](/static/images/docs/about-not-log.webp)

![Starlight about](/static/images/docs/about-log.webp)


### Booking page:

The Booking section offers users the opportunity to schedule appointments with consultants. This feature is accessible from the navigation bar and is only displayed when the user is logged in. Upon accessing the Appointment page, users are presented with a simple form to schedule their appointments.

![Starlight booking page](/static/images/docs/book-form.webp)

#### Key Features:

* Service Selection: Users can select the desired service, such as tarot reading, rune consultation, or interpretation of astral maps, through a dropdown menu.

* Date and Time Scheduling: A calendar interface allows users to choose the date of the appointment. Dates prior to the current day are disabled to prevent scheduling appointments in the past. The available appointment times are from 9:00 AM to 5:00 PM.

* Optional Message Addition: Users have the option to include an additional message or specific request in the designated field.

* Appointment Confirmation: After filling out all the necessary details, users can save the appointment by clicking the "Save" button.

![Starlight booking page](/static/images/docs/book-save.png)

* Conflicting Times: Upon submission of the appointment scheduling form, if the selected time slot is already booked by another user, a message will be displayed informing the user that the chosen time slot is not available.

![Starlight booking page](/static/images/docs/booking-err.webp)

* Viewing and Management: Below the scheduling form, a table displays all scheduled appointments, including date, time, and selected service. Users can delete or edit their appointments using the corresponding buttons next to each entry.

![Starlight booking page](/static/images/docs/bookings.webp)

* Appointment Deletion and update: Users have the ability to remove or update appointments from their schedule, and before deletion is finalized, a confirmation is requested to ensure that the user truly wants to remove the appointment.

![Starlight booking page](/static/images/docs/edit-book.webp)

![Starlight booking page](/static/images/docs/delete-book.webp)

* Informative Messages: When users perform actions such as updating, creating, or deleting appointments, informative messages are displayed on the appointment list page, confirming the success of the operation or providing feedback in case of errors.

![Starlight booking page](/static/images/docs/book-save.png)

![Starlight booking page](/static/images/docs/delete-mess.webp)

![Starlight booking page](/static/images/docs/edit-mess.webp)


### The footer: 

* All pages of the website have a footer at the bottom of the page. 

* The social media icons have been included, allowing users to access the community's social platforms and stay connected and updated. 

* Clicking on these icons will open the links in new tabs for ease of navigation.  

![Starlight footer](/static/images/docs/footer.webp)  


### 404 Page:

A custom 404 error page was developed to properly handle situations where users accessed non-existent pages or encountered broken links. This page provides clear navigation options to assist users in returning to the main site after encountering broken links or non-existent pages.

![Starlight 404](/static/images/docs/404-page.webp)  


### Features and resources to be added in the future  

* Implement a rating and commenting system to allow users to rate and leave comments on the consultations or services received, providing valuable feedback to the consultants and helping other users make informed decisions.

* Integrate an email or SMS notification system to remind users of scheduled appointments, provide updates on new content or special offers, and keep users engaged with the site.

* Expand the site to include an educational content section, offering articles, videos, and resources on tarot, runes, astrology, and other related areas, helping users deepen their knowledge and understanding, and encouraging them to return to the site more frequently.

### Accessibility

From the project's inception, the game website's design has been planned with a focus on accessibility. Special attention has been given to ensuring good color contrast, an easily understandable structure, and intuitive navigation, establishing a solid foundation for the user experience.

### LightHouse 

The accessibility, performance, best practices, and SEO (Search Engine Optimization) of the website were analyzed using the LightHouse tool available in Google Chrome's DevTools. Additionally, I ensured that all pages achieved 100% accessibility.

![Starlight 404](/static/images/docs/light-mob.png)  


## Testing 

### User Story Test: 

| User Story | Test Scenario | Test Steps | Expected Result | Actual Result |
|------------|---------------|------------|-----------------|---------------|
**`EPIC 1`**
| Early deployment | Verify the deployment process | 1. Deploy the initial version of the application on Heroku. 2. Access the deployed application. | The application is successfully deployed and accessible on Heroku. | Pass |
| Setting Up Initial Django Project Structure | Ensure the correct setup of Django project structure | 1. Create a new Django project with proper structure. 2. Verify the project structure. | The Django project is properly configured with the required structure. | Pass |
| Database Integration | Test database connectivity and media storage | 1. Perform database operations (e.g., CRUD) and file uploads. 2. Check if data is stored correctly in the database and files are uploaded and accessible. | Data is successfully stored in the database, and files are uploaded and accessible. | Pass |
**`EPIC 2`**
| Website Administration Control | Manage users, content, and settings | 1. Log in as an administrator. 2. Access the administrative interface. 3. Perform user management, content moderation, and configuration tasks. | Administrators can efficiently manage users, content, and settings. | Pass |
| Administrative Interface | Test the usability of the administrative interface | 1. Navigate through the administrative interface. 2. Perform common tasks such as user management and content editing. | The administrative interface is intuitive and efficient to use. | Pass |
**`EPIC 3`**
| View About Page | Access the "About" page | 1. Navigate to the "About" page. 2. Check if relevant information is displayed. | The "About" page displays relevant information about the company, team, services. | Pass |
| Manage About Page Content | Edit and update the content of the "About" page | 1. Log in as an administrator. 2. Access the administrative interface. 3. Edit the content of the "About" page. | The content of the "About" page is successfully edited and updated. | Pass |
**`EPIC 4`**
| Make Online Booking | Make a booking for a service offered on the website | 1. Navigate to the booking section of the website. 2. Select a service and schedule a consultation. | The booking is successfully made for the selected service. 3. Manage bookings (view, edit, delete)| Pass |
| Manage Bookings | Access the admin dashboard to manage bookings | 1. Log in as an administrator. 2. Access the admin dashboard. | Administrators can efficiently manage bookings from the admin dashboard. | Pass |
**`EPIC 5`**
| Register Account | Create a new user account | 1. Navigate to the registration page. 2. Fill out the registration form and submit. | A new user account is successfully created. | Pass |
| User Login | Log in to the user account | 1. Navigate to the login page. 2. Enter valid credentials and log in. | The user is successfully logged in to their account. | Pass |
| User Logout | Log out of the user account | 1. Click on the logout button. | The user is successfully logged out of their account. | Pass |
**`EPIC 6`**
| Website Accessibility | Ensure accessibility features are implemented |1. Utilize Google DevTools to analyze the website's accessibility. 2. Navigate through the website to confirm usability and accessibility for users. | The website is accessible and usable for users. | Pass |
| Accessible Features | Test the implementation of accessible features | 1. Verify the implementation of accessible features (e.g., alt text for images, contrast colors..). | Accessible features are implemented correctly and enhance user experience. | Pass |
**`EPIC 7`**
| README Documentation | Check the README.md file | 1. Read the README.md file. 2. Verify if it contains comprehensive information about the project. | The README.md file provides detailed information about the project's purpose, functionality, and usage. | Pass |
**`EPIC 8`**
| Testing Procedures | Verify testing procedures | 1. Follow the documented testing procedures. 2. Perform backend and frontend tests. 3. Gather user feedback for UI improvements. | Testing procedures are thorough and ensure the quality and usability of the software. | Pass |

### Tested Browsers and Devices: 

* Web Browsers: 

  * Google Chrome;

  * Microsoft Edge; 
 
  * Safari; 

  * Mozilla Firefox.


* Mobile Devices: 

  * iPhone Xr;

  * iPhone 12 Pro; (Google Chrome Inspector) 

  * Samsung Galaxy S20 Ultra. (Google Chrome Inspector) 


* Tablet: 

  * Ipad Air 4, 10.9-inch screen;

  * Nest Hub. (Google Chrome Inspector) 

 
* Laptop: 

  * Macbook Air, 13-inch screen;

  * Asus TUF F15, 15.6-inch screen. 


### Manual Testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **`Navbar`** |
| StarLight Logo | When clicked the user will be redirected to the home page. | Clicked Logo | Redirected to the home page. | Pass |
| Menu-hover | When hovering over the menu items, the text should appear in bold to indicate action.| Hover over menu | text appear in bold. | Pass |
| Navbar links | When clicked the user will be redirected to the correct page.| Clicked link | Redirected to the correct page. | Pass |
| Smaller Screens | The navbar should be displayed in hamburger style on smaller screens to conserve space. | Resized the screen to check the navbar behavior on smaller sizes. | The navbar switched to hamburger style when the screen was resized to a smaller size. | Pass |
| User is Logged In | When the user is logged in, a new menu for booking and the logout option should appear, while the register and login options should disappear. | Logged in with a user account and observed the changes in the navbar. | The booking menu and logout option appeared, and the register and login options disappeared after logging in. | Pass |
| Fixed navbar | The navbar should remain fixed at the top of the page while scrolling through the site content. | Scrolled through the site content and observed the navbar behavior. | The navbar remained fixed at the top of the page while scrolling. | Pass |
| Authentication Status Display | The website displays a message below the navigation bar indicating whether the user is logged in or not. | Verified the message display below the navigation bar while logged in and logged out. | Message displayed correctly indicating the authentication status. | Pass |
| **`Register`** |
| User Registration | After submitting valid data for registration, the user should be prompted to confirm their password, ensuring accuracy. The username must be unique and not already in use, and the optional email field must be in a valid format. | Entered valid registration data and verified the password confirmation request, uniqueness of the username, and valid email format. | The password confirmation request appeared, the unique username was accepted, and the valid email format was enforced. | Pass |
| Registration Redirection | Upon successful registration, the user should be redirected to the home page and receive a notification confirming that they are logged in. | Successfully registered a new account and observed redirection to the home page with a logged-in notification. | Redirected to the home page and received a logged-in notification after successful registration. | Pass |
| Registration with Invalid Data | If the user attempts to register an account with invalid data, such as duplicate information or an incorrect password, the registration will not be completed, and an error message will be displayed in the form. | Attempted registration with duplicate data or incorrect password. | Received error message in the form. | Pass |
| **`Login`** |
| User Login | After entering valid credentials and submitting the login form, the user should be redirected to the homepage and receive a confirmation message indicating successful login. | Entered valid credentials and submitted the login form. | Redirected to the homepage and received confirmation message indicating successful login. | Pass |
| Authenticated User Menus | When logged in, exclusive menus for authenticated users should appear, and the option to schedule an appointment becomes available. | Logged in with valid credentials and observed the appearance of exclusive menus. | Exclusive menus appeared, and appointment scheduling option became available. | Pass |
| **`Log Out`** |
| User Logout | After clicking on the logout, the user should be redirected to a confirmation page. | Clicked on the logout. | Redirected to the confirmation page. | Pass |
| User Logout Redirect | After confirming the logout, the user should be redirected to the home page. | Confirmed logout. | Redirected to the home page after logout confirmation. | Pass |
| **`Booking`** |
| User able to select the service | User should be able to select the desired service when booking a consultation | Selected the desired service on the booking page | Service selected successfully | Pass |
| Select the date | User should be able to choose the desired date for the consultation | Selected a date on the booking page | Date was successfully selected | Pass |
| Select the time | User should be able to choose the preferred time for the consultation | Chose a time slot on the booking page | Time was successfully selected | Pass |
| Book consultation | User should be able to schedule a consultation by selecting a date and time | Attempted to book a consultation on the booking page | Consultation was successfully scheduled | Pass |
| User cannot book in a past date | User should receive an alert when attempting to schedule an appointment for a past date | Tried to book a consultation for a past date on the booking page | Alert message appeared indicating that booking for past dates is not allowed | Pass |
| Unavailable booking slot | When attempting to book a consultation on a date and time that is already booked, the user should receive an alert indicating that the consultant is not available for that date or time. | Attempted to book a consultation on a date and time that is already booked | Alert displayed indicating that the consultant is not available for that date or time | Pass |
| Edit booking | User should have the option to edit their existing bookings | Accessed the edit option for a booked consultation | Booking details were successfully edited | Pass |
| Delete booking | User should be able to remove their bookings if needed | Attempted to delete a booked consultation | Booking was successfully deleted | Pass |
| Save booking in booking page | User's bookings should be saved and displayed on the booking page | Scheduled a consultation and checked if it appeared on the booking page | Booking was saved and appeared on the booking page | Pass |
| **`Home`** |
| Button: Non-Logged-in User | "Login First" message appears, indicating the user needs to log in first to book. | Clicked "Login First" Button | Redirected to the login page. | Pass |
| Button: Logged-in User | "Book Now" button appears, allowing the user to book appointments. | Clicked "Book Now" Button | Redirected to the booking page. | Pass |
| Button: hover | When the mouse hovers over the button, it should change color to indicate action. | Hovered over the button and observed the color change. | The button changed color when hovered over, indicating action. | Pass |
| **`About`** |
| Text Loading  | The text on the "About" page should match the content entered in the admin panel. | Compared displayed text with admin panel content. | Text matched admin panel content. | Pass |
| Image Upload             | The administrator can successfully upload the image through the administration panel.                 | Verification of the image upload process in the administration panel.     | The correct image is displayed on the website.    | Pass |
| Updated Date    | Creation date of the text displayed at the bottom of the page. | Checked if the displayed date matches the creation date of the text. | Date displayed matched the creation date of the text. | Pass |
| Button: Non-Logged-in User | "Login First" message appears, indicating the user needs to log in first to book. | Clicked "Login First" Button | Redirected to the login page. | Pass |
| Button: Logged-in User | "Book Now" button appears, allowing the user to book appointments. | Clicked "Book Now" Button | Redirected to the booking page. | Pass | 
| Button: hover | When the mouse hovers over the button, it should change color to indicate action. | Hovered over the button and observed the color change. | The button changed color when hovered over, indicating action. | Pass |
| **`Admin`** |
| Login to Django Panel | The admin should be able to log in to the Django panel using the provided credentials. | Logged in to the Django panel using admin credentials | Successfully accessed the Django panel | Pass |
| Add, Edit, and Delete Services | The admin should be able to add, edit, and delete services from the website. | Added, edited, and deleted services from the admin panel | Successfully managed services | Pass |
| Edit and Delete Bookings | The admin should be able to edit and delete bookings from the admin panel. | Edited and deleted bookings from the admin panel | Successfully managed bookings | Pass |
| Add, Edit, and Delete Content of About Page | The admin should be able to add, edit, and delete content on the About page from the admin panel. | Added, edited, and deleted content on the About page from the admin panel | Successfully managed About page content | Pass |
| New Menu in Navbar| When logged in as an admin, a new menu should appear in the navbar allowing direct access to the admin control panel, redirecting the admin to the panel. | Logged in as an admin and observed the appearance of a new menu in the navbar | New menu appeared in the navbar, providing access to the admin control panel | Pass |
| **`Notification messages`** |
| Notification messages | Clear and informative messages are displayed upon registration, login, logout, adding, editing, or deleting bookings. | Perform registration, login, logout, adding, editing, or deleting bookings. Verify if clear and informative messages are displayed on the screen confirming the actions taken. | Messages displayed successfully. | Pass      |
| **`Footer`** |
| Icon-clicked | Clicking on social network icons in the footer opens new windows directing users to the respective social networks.| Clicked social networks Icons | Opens the pages in a new window. | Pass |


### Validator Testing  

  * Python

To ensure compliance with coding best practices, I installed Flake8 in my development environment. Flake8 assisted me in identifying and rectifying style and formatting issues throughout the project's source code.

Additionally, I utilized the PEP8 validator to identify and correct any remaining issues in my code. The identified errors were primarily related to improper use of whitespace and exceeding line length. All of these issues were addressed comprehensively, ensuring adherence to coding best practices.

![Pep8 - Python](/static/images/docs/python-check.webp)

  * CSS:  

No errors were found during the validation process using the official Jigsaw validator.


![Jigsaw validator - Css](/static/images/docs/jigsaw-valid.webp)


  * HTML:  

To ensure the validity and compliance of my web pages with web standards, I used the W3C validator. This tool helped me identify and correct any errors highlighted in my pages.

![W3C validator - html](/static/images/docs/html-check.webp)


The corrections were implemented in accordance with the validator's suggestions.

#### Unit Test 

I used unit tests to ensure the proper functioning of different parts of the application. The unit tests were implemented using Python's unittest module.

![unittest - python](/static/images/docs/unittest.png)

### Bugs

#### Solved Bugs
#### Inconsistent Favicon Display

  * Bug Description: 

While developing a website with Django, I noticed that the favicon defined in the `base.html` file was only being displayed on the homepage (index). However, on other pages, such as about and booking page, the favicon was not appearing.

  * Action Taken:

Upon further investigation, I found that the issue was related to the relative path of the favicon specified in the `base.html` file. To ensure that the favicon is loaded on all pages of the site, regardless of the current URL, I adopted the following approach:

In the `base.html` file, I updated the `<link>` tag to reference the favicon using the absolute path relative to the project's root directory, using Django's `{% static %}` tag:

```html
<link rel="icon" type="image/ico" sizes="32x32" href="{% static 'images/favicon.ico' %}" />
```
![bug - 1](/static/images/docs/bug3-2.png)

![Solved bug - 1](/static/images/docs/bug3.png)



#### Replace Date Mask with Current Date on Booking

  * Bug Description:

A bug was identified where the date mask was not being set correctly on the booking form, causing issues with selecting the date.

  * Action Taken:

This issue has been fixed by replacing the date mask with the current date on the booking form.
This fix ensures that users can now select the date accurately without any errors.

![bug 2 solved](/static/images/docs/bug1.png)

#### Overlay Text Box Misalignment

  * Bug Description: 
  
I identified an issue where the text box was becoming misaligned over the main image of the site, depending on the screen size. When the menu was opened, it would shift out of place.


  * Action Taken: 
  
The problem has been fixed by adding various media query configurations and testing across different screen sizes. This fix ensures that the text box now remains properly aligned over the main image at all screen resolutions.

![bug 3 solved](/static/images/docs/bug2.png)


#### Unsolved Bugs

No unfixed bugs.

## Technologies Used
### Languages

* Python 3, Html, Css, JavaScript.

### Frameworks, Libraries & Programs

Visual Studio Code (VS Code): Utilized as a source code editor.

[Django](https://www.djangoproject.com/): Used as a web framework for building the application.

[Bootstrap](https://getbootstrap.com/): Utilized for responsive and mobile-first front-end web development.

[Cloudinary](https://cloudinary.com/): Used for image management, including image upload, storage, and manipulation.

[ElephantSQL](https://www.elephantsql.com/): Utilized for managing PostgreSQL databases in the cloud.

[Google Fonts](https://fonts.google.com/): Imported to integrate font styles into the website. 

[Font Awesome](https://fontawesome.com/): Incorporated to easily add icons across the website.

[Lucidchart](https://lucid.app/): employed in the planning phase for crafting flowcharts

[Heroku Platform](https://dashboard.heroku.com/apps): for deploying the application in a live environment.

Google Dev Tools: Leveraged for debugging and testing features, as well as resolving issues related to responsiveness and styling. 

[Pep8 online](https://pep8ci.herokuapp.com/): Used to identify issues in my Python code.

[The W3C Markup Validation Service](https://validator.w3.org/): Used to validate the accuracy and validity of HTML code.

[The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/): Employed to validate the correctness and compliance of CSS code.

[GitHub](https://github.com/): Used to save and store the website files.


#### Python Libraries and Modules

* **os:** Used for interacting with the operating system, including file system operations and environment variables.

* **sys:** Provides access to interpreter variables and functions for interacting with the Python interpreter.

* **pathlib:** Allows for easy and platform-independent manipulation of file paths, representing files and directories in the file system.

* **datetime**: Used for date and time manipulation.

* **cloudinary.models.CloudinaryField**: Utilized to integrate Cloudinary directly into Django models, facilitating storage and retrieval of images associated with these models.

## Deployment

<details>
  <summary> Deploying Your Project on Heroku</summary>

* To get your project up and running on Heroku, follow these steps:

1. **Create a List of Dependencies:**
   - In the terminal, run the command `pip3 freeze > requirements.txt` to generate a list of dependencies needed for Heroku deployment.

2. **Heroku Account Setup:**
   - Log in to your Heroku account or create a new one if needed.

3. **Create a New App:**
   - Click on "New" in the top-right corner of your Heroku Dashboard, and select "Create new app" from the dropdown menu.
   - Enter a unique app name and choose a region (EU or USA) closest to you.
   - Click on "Create App".

4. **Config Var**:
   - In your new app’s settings tab, ensure the Config Var DISABLE_COLLECTSTATIC key has a value of 1.

5. **Update Your Code for Deployment**:
   - Use pip3 to install gunicorn and freeze it to the requirements.txt file.
   - In the Procfile, add a command using gunicorn and your project wsgi file to start the webserver.
     ```bash
     web: gunicorn <your project>.wsgi
     ```
   - In thensettings.py file, set the DEBUG constant to False and append the '.herokuapp.com' hostname to the ALLOWED_HOSTS list.
     ```python
     DEBUG = False
     ALLOWED_HOSTS = ['.herokuapp.com']
     ```

6. **Connect to GitHub:**
   - Go to the "Deploy" tab and select "GitHub" as the deployment method.
   - Click "Connect to GitHub" and search for your repository name.
   - Click "Connect" to link the repository to Heroku.
  - In your new app’s resources tab delete any Postgres database Add-on.

7. **Deploy the App:**
   - Scroll down to "Manual deploy" and click "Deploy Branch". This allows you to view the build logs as the app is being constructed.
   - After the initial deployment, you can enable "Enable Automatic Deploys" to keep the app up-to-date with your GitHub repository.

8. **Finalize Deployment:**
   - Wait for the app to build. Once ready, you will see the "App was successfully deployed" message and a 'View' button to take you to your deployed link.


You can access the live project by clicking [here](https://starlight-consultations-2b1105ac431c.herokuapp.com/).

</details>

<details>
  <summary>Forking the Repository</summary>
Forking the repository allows you to create a copy of the original repository in your GitHub profile. This enables you to view and edit the code without affecting the original repository.

**Steps:**

1. In the "starlight-consultations" repository, click on "Fork" in the top right corner.
2. Confirm the creation of the fork.

</details>

<details>
  <summary>Cloning the Repository</summary>
Cloning a repository means obtaining a local copy to work on in your own development environment.

**Steps:**

1. In the repository, click on "Code" above the file list.
2. Copy the URL.
3. Open Git Bash.
4. Navigate to the directory where you want to clone the repository.
5. Type `git clone` followed by the URL and press "enter".

</details>

<details>
  <summary>Setting up ElephantSQL PostgreSQL Database
</summary>

Steps to create an instance of a cloud-based PostgreSQL database using ElephantSQL and connect it to our Django project.

**Steps**

1. **Create PostgreSQL Instance:**
   - Log into your ElephantSQL dashboard.
   - Click on "Create New Instance".
   - Set up your plan
   - Select a data center near you.
   - Click "Review".
   - Verify your details and click "Create instance".

2. **Copy Database URL:**
   - Click on "DETAILS" and copy the URL.

   
3. **Create `env.py` File:**
   - Create a file named `env.py` at the top level of your project.
   - Add the following code to `env.py`, replacing `<your-database-URL>` with the URL copied from ElephantSQL:
     ```python
     import os

     os.environ.setdefault(
         "DATABASE_URL", "<your-database-URL>"
     )
     ```

4. **Update `.gitignore` File:**
   - Open `.gitignore` file and add `env.py` to prevent secret data from being pushed to GitHub.

5. **Install Database Packages:**
   - Install the required packages to connect to your PostgreSQL database:

6. **Update `settings.py`:**
   - Import required packages in `settings.py`:
     ```python
     import os
     import dj_database_url

     if os.path.isfile('env.py'):
         import env
     ```
   - Connect to the environment variable `DATABASE_URL`:
     ```python
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
     ```

7. **Migrate Database Tables:**
   - Run migrations to create database tables

8. **Create Superuser:**
    - Create a superuser for admin access to the database:
      ```bash
      python manage.py createsuperuser
      ```
    - Follow the prompts to choose a username, email, and password.

9. **Deploy the Project:**
    - Change DEBUG value to False in `settings.py`.
    - Push your updated code to GitHub.
    - Go to the Heroku dashboard and deploy your project.

10. **Connect Heroku to PostgreSQL Database:**
    - Go to the Heroku app's Settings tab and click "Reveal Config Vars".
    - Add a new config var with a key of `DATABASE_URL` and the value of the ElephantSQL URL.

</details>

<details>
  <summary>Setting up Cloudinary</summary>

To ensure proper image management in your Django application, it's essential to set up Cloudinary.

**Steps:**

1. Install the required Python packages to connect to the Cloudinary API

2. Access the Cloudinary dashboard and log in or create a new account.

3. In the Cloudinary dashboard, copy the Cloudinary URL.

4. Open the `env.py` file in your project and set the value of the `CLOUDINARY_URL` constant to the URL copied from the Cloudinary dashboard.

5. Open the `settings.py` file and add the required apps to the `INSTALLED_APPS` list.

6. In `models.py`, import `CloudinaryField` from `cloudinary.models`.

7. Add a new field `featured_image` to the model.

8. Run migrations to create a new migrations file and apply the changes to the database schema.

9. In the Heroku dashboard, add a key:value pair for `CLOUDINARY_URL` in the config vars.

</details>

## Credits

### Code

While working on the development of my Django project, there were occasions where I needed to conduct research that covered topics beyond the scope of the course or even required thorough revision. Below, I am sharing the links to the consulted sources:

* [Scrum & Kanban - Theme, Epic, Story, Task](https://scrumandkanban.co.uk/theme-epic-story-task/)

* [Djangoproject - Built-in template tags and filters](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#ref-templates-builtins-filters)

* [Djangoproject - QuerySet API reference](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#first)

* [Django-allauth - Quickstart](https://docs.allauth.org/en/latest/installation/quickstart.html)

* [Djangoproject - Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/)

* [Bootstrap - Spacing](https://getbootstrap.com/docs/5.0/utilities/spacing/#margin-and-padding)

* [Bootstrap - Introduction](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

* [w3schools - HTTP Request Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)

* [Stackoverflow - Django won't refresh staticfiles](https://stackoverflow.com/questions/27911070/django-wont-refresh-staticfiles)

* [Fontawesome - Accessibility](https://fontawesome.com/docs/web/dig-deeper/accessibility)

* [README Example](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md): To write the README file, I followed the structure and table format (testing section) from the readme-examples repository by Kera Cudmore.

* The foundation of the project was established using the CI I Think Therefore I Blog project example as a starting point.

### Content

I created  the content for my application.

* [Energetic Tarot](https://energetictarot.co.uk/what-are-esoteric-practices/) and ChatGPT: used to assist in write the content about esotericism on the website.

### Media

[Favicon.io](https://favicon.io/favicon-converter/): utilized to convert the star image from the logo into a favicon.

[CloudConvert](https://cloudconvert.com/png-to-webp): utilized for image format conversion.

[Adobe Express](https://www.adobe.com/br/express/feature/image/resize): utilized for image manipulation and resizing.

MS Paint: used to edit the images. 

[Balsamiq](https://balsamiq.com/): utilized for wireframing purposes.

[Coolors](https://coolors.co/f08080-f4978e-f8ad9d-fbc4ab-ffdab9): utilized to create the color palette. 

[Unsplash](https://unsplash.com/) and [Freepik](https://br.freepik.com/): used to source images for the website. 

[Am I Responsive?](https://ui.dev/amiresponsive) and [Morckup Generator](https://techsini.com/multi-mockup/index.php): utilized to view the website's appearance and responsiveness across a range of devices.


### Acknowledgments

I would like to extend my sincere gratitude to the individuals who offered their assistance and support throughout the entirety of this project:

Jubril Akolade, my mentor, for his guidance and constructive feedback.

Laura Mayock, the Cohort Facilitator at Code Institute, for consistently steering our studies in the most effective direction.

My friends Ivan Frezza and Bruna Andelieri, providing valuable insights and clarifying uncertainties about my code. Thank you for always supporting me.

My husband Jasser, for always believing in my abilities, for continuously motivating me, and for his unwavering support.

My family and friends for standing by my side throughout this journey. All the support meant a lot to me, and I couldn't have done it without them.