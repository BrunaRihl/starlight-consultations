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
* The 'Set up' epic encompasses the activities required to establish the initial development environment of the project, including installing tools, configuring version control systems, and organizing the project structure.

  * User Story: Early deployment
As a developer, I can deploy an initial version of the application on Heroku so that I can verify the functionality of the initial setup and continue testing the application during development.

  * User Story: Setting Up Initial Django Project Structure
As a developer, I can establish the foundational structure of a Django project for a reservation website so that I can ensure smooth progression in both development and deployment.

  * User Story: Database Integration 
As a developer I can establish database connectivity and media storage so that user data is successfully stored.

#### EPIC 2: Admin Dashboard

* The Admin Dashboard epic aims to create a robust and intuitive interface for administrators to manage various aspects of the website or application efficiently. This includes functionalities such as user management, content moderation and configuration. The goal is to provide administrators with comprehensive tools and features to oversee and control the platform effectively.

  * User Story: Website Administration Control
As an administrator, I can manage users, content, and settings on the website so that I can ensure a consistent and high-quality experience for end users.

  * User Story: Administrative Interface
As a developer, I can develop an intuitive administrative interface for administrators to efficiently manage users, content, and settings so that the website can be effectively controlled and maintained.

#### EPIC 3: About Page

* The About Page epic aims to improve the "About" section of the website, providing users with a more informative and engaging experience. This includes updating the page content, enhancing its visual design, and ensuring that it clearly conveys the company's message and values. The goal is to create an About page that is both attractive and effective in communicating the organization's objectives and identity to visitors.

  * User Story: View About Page 
As a site user, I can access the "About" page to obtain information about the company, team, or project so that I can learn more about its background and objectives.

  * User Story: Manage About Page Content
As an administrator, I can edit and update the content of the "About" page as needed so that I can keep it up-to-date with the latest information.

#### EPIC 4: Booking System

* The Booking System epic addresses the implementation of a system that allows users to make reservations for services offered on the website, while providing administrators with the necessary tools to efficiently manage these bookings. This involves creating intuitive interfaces for users to make reservations, as well as an administrative panel for administrators to manage all bookings. The goal is to provide users with an integrated and convenient experience while simplifying the administration process for the website team.

  * User Story: Make Online Booking
As a user, I can to be able to make an online booking to schedule a consultation with one of the services offered on the website so that I can easily arrange an appointment at my convenience.

  * User Story: Manage Bookings
As an administrator, I can access the admin dashboard to manage bookings, ensuring efficient organization and oversight of all scheduled appointments, so that I can effectively coordinate and optimize the booking process.


#### EPIC 5: User Authentication

* The User Authentication epic deals with implementing a system for user registration, login, and logout on the website. This enables users to create accounts, log in to access exclusive features, and log out when they wish to exit. The goal is to ensure the security of user accounts and provide a seamless and secure user experience.

  * User Story: Register Account
As a user, I can register an account so that I can access additional services on the website.

  * User Story: User Login
As a user, I can to be able to log in to my account so that I can access personalized features and services on the website.

  * User Story: User Logout
As a user, I can to be able to log out of my account so that I can securely end my session on the website.

#### EPIC 6: User Authentication

* The Accessibility epic aims to ensure that the website is accessible to all users, regardless of their abilities or needs. This involves implementing features and practices that make the site easy to use and understand for all users, including those with visual, auditory, or motor impairments. The goal is to provide an inclusive and accessible experience for all users, ensuring they can navigate the site, access information, and use the features effectively.


  * User Story: Website Accessibility
As a user, I can navigate the website with ease and access all content so that I can have an inclusive browsing experience and access information effectively.


  * User Story: Accessible Features
As a developer, I can implement accessible features on the website to ensure a positive user experience for all users, so that everyone can access and effectively use the website.


#### EPIC 7: Project Documentation

* The Project Documentation epic aims to create comprehensive documentation that clearly explains the purpose, functionality, and usage of the project. This includes crafting a README.md file to provide detailed information about the project, facilitating understanding and collaboration among users and contributors. The goal is to ensure that everyone involved can easily access the necessary information about the project, including its design, features, technologies used, testing procedures, deployment instructions, and credits for the resources utilized.

  * User Story: README Documentation
As a developer, I can create a README.md file to document and present the project to users and collaborators so that they can easily understand the purpose, functionality, and usage of the project.

#### EPIC 8: User Authentication

* This epic focuses on comprehensive testing procedures to ensure the reliability, functionality, and usability of the project. It involves documenting testing procedures, conducting backend and frontend tests, evaluating compatibility, and gathering user feedback for UI improvements. The goal is to ensure high-quality and usability of the software before deployment.

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

