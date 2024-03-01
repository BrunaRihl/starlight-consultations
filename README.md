# StarLight

Starlight is an online platform for personalized esoteric services! Starlight offers a variety of services, including tarot readings, rune interpretation, and astrological chart creation available conveniently and affordably directly on the website. Users can register and schedule consultations online with ease, ensuring a personalized and seamless experience.

![Starlight website shown on a range of devices](/assets/images/docs/responsive.png)  

## Demo
The live demo is available [here]()!

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


### ERD


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

The Accessibility epic aims to ensure that the website is accessible to all users, regardless of their abilities or needs. This involves implementing features and practices that make the site easy to use and understand for all users, including those with visual, auditory, or motor impairments. 


  * User Story: Website Accessibility

As a user, I can navigate the website with ease and access all content so that I can have an inclusive browsing experience and access information effectively.


  * User Story: Accessible Features

As a developer, I can implement accessible features on the website to ensure a positive user experience for all users, so that everyone can access and effectively use the website.


#### EPIC 7: Project Documentation

The Project Documentation epic aims to create comprehensive documentation that clearly explains the purpose, functionality, and usage of the project. This includes crafting a README.md file to provide detailed information about the project, facilitating understanding and collaboration among users and contributors. 

  * User Story: README Documentation

As a developer, I can create a README.md file to document and present the project to users and collaborators so that they can easily understand the purpose, functionality, and usage of the project.

#### EPIC 8: Project Testing

This epic focuses on comprehensive testing procedures to ensure the reliability, functionality, and usability of the project. It involves documenting testing procedures, conducting backend and frontend tests, evaluating compatibility, and gathering user feedback for UI improvements. The goal is to ensure high-quality and usability of the software before deployment.

  * User Story: Testing Procedures

As a developer, I can thoroughly test the project so that I can ensure its quality and usability.


### Agile development

During the project development, I adopted an agile methodology, utilizing Kanban to manage my activities and projects. Kanban provided a clear view of the workflow, allowing me to track task progress visually and in real time. I organized my project on GitHub, using a Kanban board to divide tasks into columns such as "To Do," "In Progress," and "Done." 


![Starlight website color palette](/static/images/docs/agile.png)


For more details on the project management process, you can access the link [here](https://github.com/users/BrunaRihl/projects/6).



## Design

### Color palette

The choice of colors for the website was carefully planned, with shades of purple and lilac being selected for their association with spirituality, intuition, and calmness. These colors were chosen to create a pleasant and engaging atmosphere for users, conveying a sense of serenity and sophistication while reflecting the brand's identity and value proposition. Additionally, the strategic use of contrast was taken into account to facilitate website navigation and readability, ensuring a more intuitive and accessible experience for all visitors.

![Starlight website color palette](/static/images/docs/palette.png)

### Typography 

Google Fonts was utilized to incorporate the selected font styles into the website. 

I selected 'Montserrat Alternates' for the body text due to its clean and contemporary appearance, enhancing readability across various content sections. As for the logo, I chose 'Mystery Quest' to evoke a sense of mystery and intrigue, aligning with the mystical theme of the website while adding a unique touch to the brand identity.

![Starlight fonts choosen](/static/images/docs/fonts.png)  

### Imagery 

The selected images for the website aim to immerse users in the realm of consultations offered by the consultants. I ensured they were of good resolution, seamlessly integrating with the colors and theme of the site. The goal was to provide a visually engaging and cohesive experience, connecting users to the spiritual environment of the consultations while facilitating understanding of the services available for booking through the platform.

### Wireframes

## Features

The website comprises three primary pages: a welcoming home page, an informative about page, and a convenient booking page.

### Navigation bar 

* All pages feature a responsive navigation bar at the top of the screen.
* In the top-left corner, the site's logo is displayed, allowing users to return to the homepage with a single click.
* Navigation adaptation on smaller screens such as tablets and smartphones is automatic. These features were implemented using the Bootstrap framework, ensuring smooth and responsive navigation.
* On mobile devices, the navigation bar is transformed into a hamburger menu to optimize the user experience.
* The menu provides links to the main pages of the site, including Home, About, Booking, Register, and Login/Logout.
* To assist users in navigating the site, a visual effect has been added to highlight menu items when the mouse cursor hovers over them.
* The "Booking" option is displayed only for logged-in users, remaining hidden for non-authenticated users.
* Additionally, when the superuser is logged in, an additional option is provided in the menu, allowing direct access to the administrative control panel.

![Starlight nav bar](/assets/images/nav.jpg)

#### Authentication Status

A functionality has been implemented on the website that displays a message below the navigation bar, informing whether the user is logged in or not. This message allows users to easily identify their authentication status while browsing the site.


![Starlight auth](/assets/images/auth.jpg)


### Sign Up Page

- On the registration page, new users can start their journey on Starlight by creating a personalized account. Here, users provide essential information such as name, email address (optional), and password to establish their identity in the system. During the registration process, each user is prompted to choose a unique username, ensuring uniqueness among all accounts. Additionally, the system checks if the provided email address has not already been registered.


### Login Page
- On the login page, registered users can access their existing accounts on Starlight. Using a simple form, users input their credentials, including username and password, to sign into the system. Once authenticated, users have immediate access to the site's personalized features, allowing them to explore and utilize the available functionalities.

### Logout Page

-  The logout page provides users with a convenient way to end their sessions on Starlight. By clicking the "Logout" button, users are logged out of their accounts, ensuring the privacy and security of their information. Upon logout completion, users are redirected to a confirmation page and then to the homepage, providing a seamless and secure experience.

#### Notification messages

Starlight displays warning messages at crucial moments of user interaction with the platform. Upon successfully completing registration, logging in, or logging out, clear and informative messages are displayed on the screen to confirm the actions taken. These messages provide immediate feedback to the user, ensuring an intuitive and transparent user experience.

### Home Page 

### Favicon

A website features a custom favicon that has been added to the browser's header. The favicon showcases a moon and a star, matching the theme and colors of the site, providing a unique visual identity for it.

![StarLight - favicon](/assets/images/docs/favicon-zp.png)

#### Header: 

* The main image showcases hands manipulating a tarot card deck, aligning with the central theme of the site about tarot readings, rune consultations, and interpretations of astral maps.
* The overlaid message provides a brief introduction to the website's concept, while the high resolution and vibrant colors ensure an inviting presentation to visitors.

![Starlight - image hero](/assets/images/hero.jpg)

#### Sections: 

* Below the main image, users will find the "Our Team" section.

  * This section highlights the services offered by the site, such as tarot readings, rune consultations, and interpretations of astrological charts.

  * Using Bootstrap cards, each service is presented concisely, providing an overview of what the site offers to users.

![Starlight Our Team](/assets/images/about-choose.jpg)


* Additionally, there's a "Book Now" section, where users can schedule consultations directly through the site.

  * If the user is logged in, a "Book Now" button is displayed, allowing them to proceed with scheduling.

  * If the user is not logged in, a "Login First" button is shown, prompting them to log in before booking an appointment.


![Starlight book now](/assets/images/about-choose.jpg)


### About: 

The "About" page provides a detailed insight into the purpose and services available on the site. 

* Key Highlights:
  * Flexible Content: The administrator can easily update the content of the "About Us" page using the Django admin panel.

  * Update Information: The date of the last update is displayed on the page so that visitors know when the content was last revised.

  * If the user is logged in, a "Book Now" button is displayed, if the user is not logged in, a "Login First" button is shown.


![Starlight about](/assets/images/services.jpg)
![Starlight about](/assets/images/packages.jpg)


### Booking:

The Booking section offers users the opportunity to schedule appointments with consultants. This feature is accessible from the navigation bar and is only displayed when the user is logged in. Upon accessing the Appointment page, users are presented with a simple form to schedule their appointments.

#### Key Features:

* Service Selection: Users can select the desired service, such as tarot reading, rune consultation, or interpretation of astral maps, through a dropdown menu.

* Date and Time Scheduling: A calendar interface allows users to choose the date of the appointment. Dates prior to the current day are disabled to prevent scheduling appointments in the past. The available appointment times are from 9:00 AM to 5:00 PM.

* Optional Message Addition: Users have the option to include an additional message or specific request in the designated field.

* Appointment Confirmation: After filling out all the necessary details, users can save the appointment by clicking the "Save" button.

* Conflicting Times: Upon submission of the appointment scheduling form, if the selected time slot is already booked by another user, a message will be displayed informing the user that the chosen time slot is not available.

* Informative Messages: When users perform actions such as updating, creating, or deleting appointments, informative messages are displayed on the appointment list page, confirming the success of the operation or providing feedback in case of errors.

* Viewing and Management: Below the scheduling form, a table displays all scheduled appointments, including date, time, and selected service. Users can delete or edit their appointments using the corresponding buttons next to each entry.

* Appointment Deletion: Users have the ability to remove appointments from their schedule, and before deletion is finalized, a confirmation is requested to ensure that the user truly wants to remove the appointment.

![Starlight booking page](/assets/images/gallery.jpg)


### The footer: 

* All pages of the website have a footer at the bottom of the page. 

* The social media icons have been included, allowing users to access the community's social platforms and stay connected and updated. 

* Clicking on these icons will open the links in new tabs for ease of navigation.  

![Starlight footer](/assets/images/footer.jpg)  


### 404 Page:

Developed a custom 404 error page to properly handle situations where users accessed non-existent pages or encountered broken links. This page provides clear navigation options to assist users in returning to the main site.


### Features and resources to be added in the future  

* Implement a rating and commenting system to allow users to rate and leave comments on the consultations or services received, providing valuable feedback to the consultants and helping other users make informed decisions.

* Integrate an email or SMS notification system to remind users of scheduled appointments, provide updates on new content or special offers, and keep users engaged with the site.

* Expand the site to include an educational content section, offering articles, videos, and resources on tarot, runes, astrology, and other related areas, helping users deepen their knowledge and understanding, and encouraging them to return to the site more frequently.

### Accessibility

From the project's inception, the game website's design has been planned with a focus on accessibility. Special attention has been given to ensuring good color contrast, an easily understandable structure, and intuitive navigation, establishing a solid foundation for the user experience.


## Testing 

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
|  |  |  |  |  |
| StarLight Logo | When clicked the user will be redirected to the home page. | Clicked Logo | Redirected to the home page. | Pass |
| Menu-hover | When hovering over the menu items, the text should appear in bold to indicate action.| Hover over menu | text appear in bold. | Pass |
| Navbar links | When clicked the user will be redirected to the correct page.| Clicked link | Redirected to the correct page. | Pass |
| Smaller Screens | The navbar should be displayed in hamburger style on smaller screens to conserve space. | Resized the screen to check the navbar behavior on smaller sizes. | The navbar switched to hamburger style when the screen was resized to a smaller size. | Pass |
| User is Logged In | When the user is logged in, a new menu for booking and the logout option should appear, while the register and login options should disappear. | Logged in with a user account and observed the changes in the navbar. | The booking menu and logout option appeared, and the register and login options disappeared after logging in. | Pass |
| Fixed navbar | The navbar should remain fixed at the top of the page while scrolling through the site content. | Scrolled through the site content and observed the navbar behavior. | The navbar remained fixed at the top of the page while scrolling. | Pass |
| Authentication Status Display | The website displays a message below the navigation bar indicating whether the user is logged in or not. | Verified the message display below the navigation bar while logged in and logged out. | Message displayed correctly indicating the authentication status. | Pass |
| **`Register`** |
|  |  |  |  |  |
| User Registration | After submitting valid data for registration, the user should be prompted to confirm their password, ensuring accuracy. The username must be unique and not already in use, and the optional email field must be in a valid format. | Entered valid registration data and verified the password confirmation request, uniqueness of the username, and valid email format. | The password confirmation request appeared, the unique username was accepted, and the valid email format was enforced. | Pass |
| Registration Redirection | Upon successful registration, the user should be redirected to the home page and receive a notification confirming that they are logged in. | Successfully registered a new account and observed redirection to the home page with a logged-in notification. | Redirected to the home page and received a logged-in notification after successful registration. | Pass |
| Registration with Invalid Data | If the user attempts to register an account with invalid data, such as duplicate information or an incorrect password, the registration will not be completed, and an error message will be displayed in the form. | Attempted registration with duplicate data or incorrect password. | Received error message in the form. | Pass |
| **`Login`** |
|  |  |  |  |  |
| User Login | After entering valid credentials and submitting the login form, the user should be redirected to the homepage and receive a confirmation message indicating successful login. | Entered valid credentials and submitted the login form. | Redirected to the homepage and received confirmation message indicating successful login. | Pass |
| Authenticated User Menus | When logged in, exclusive menus for authenticated users should appear, and the option to schedule an appointment becomes available. | Logged in with valid credentials and observed the appearance of exclusive menus. | Exclusive menus appeared, and appointment scheduling option became available. | Pass |
| **`Log Out`** |
|  |  |  |  |  |
| User Logout | After clicking on the logout button, the user should be redirected to a confirmation page. | Clicked on the logout button and confirmed redirection to the confirmation page. | Redirected to the confirmation page. | Pass |
| User Logout Redirect | After confirming the logout, the user should be redirected to the home page. | Confirmed logout and checked for redirection to the home page. | Redirected to the home page after logout confirmation. | Pass |
| **`Booking`** |
|  |  |  |  |  |
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
|  |  |  |  |  |
| Button: Non-Logged-in User | "Login First" message appears, indicating the user needs to log in first to book. | Clicked "Book Now" Button | Redirected to the login page. | Pass |
| Button: Logged-in User | "Book Now" button appears, allowing the user to book appointments. | Clicked "Book Now" Button | Redirected to the booking page. | Pass |
| Button: hover | When the mouse hovers over the button, it should change color to indicate action. | Hovered over the button and observed the color change. | The button changed color when hovered over, indicating action. | Pass |
| **`About`** |
|  |  |  |  |  |
| Text Loading  | The text on the "About" page should match the content entered in the admin panel. | Compared displayed text with admin panel content. | Text matched admin panel content. | Pass |
| Updated Date    | Creation date of the text displayed at the bottom of the page. | Checked if the displayed date matches the creation date of the text. | Date displayed matched the creation date of the text. | Pass |
| Button: Non-Logged-in User | "Login First" message appears, indicating the user needs to log in first to book. | Clicked "Book Now" Button | Redirected to the login page. | Pass |
| Button: Logged-in User | "Book Now" button appears, allowing the user to book appointments. | Clicked "Book Now" Button | Redirected to the booking page. | Pass | 
| Button: hover | When the mouse hovers over the button, it should change color to indicate action. | Hovered over the button and observed the color change. | The button changed color when hovered over, indicating action. | Pass |
| **`Admin`** |
|  |  |  |  |  |
| Login to Django Panel | The admin should be able to log in to the Django panel using the provided credentials. | Logged in to the Django panel using admin credentials | Successfully accessed the Django panel | Pass |
| Add, Edit, and Delete Services | The admin should be able to add, edit, and delete services from the website. | Added, edited, and deleted services from the admin panel | Successfully managed services | Pass |
| Edit and Delete Bookings | The admin should be able to edit and delete bookings from the admin panel. | Edited and deleted bookings from the admin panel | Successfully managed bookings | Pass |
| Add, Edit, and Delete Content of About Page | The admin should be able to add, edit, and delete content on the About page from the admin panel. | Added, edited, and deleted content on the About page from the admin panel | Successfully managed About page content | Pass |
| New Menu in Navbar| When logged in as an admin, a new menu should appear in the navbar allowing direct access to the admin control panel, redirecting the admin to the panel. | Logged in as an admin and observed the appearance of a new menu in the navbar | New menu appeared in the navbar, providing access to the admin control panel | Pass |
| **`Footer`** |
|  |  |  |  |  |
| Icon-clicked | Clicking on social network icons in the footer opens new windows directing users to the respective social networks.| Clicked social networks Icons | Opens the pages in a new window. | Pass |


