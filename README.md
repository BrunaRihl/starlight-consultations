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

#### User base

Individuals interested in Tarot, Runes, and Astrological Chart consultations, seeking guidance and insights on personal, spiritual, and emotional matters. This may also encompass those wishing to explore alternative methods of self-discovery and personal growth, as well as individuals seeking online support to share spiritual experiences and obtain consultation services.

#### Website Goals  

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

I developed a simple wireframe in PowerPoint for the game, aiming to ensure a consistent experience across mobile devices, computers, and tablets. I adjusted the size of buttons, texts, and cards, while maintaining the same layout for all cases.

I made some adjustments in relation to what I had planned for positioning and added some buttons to enhance functionality and user experience, aiming to ensure the game is accessible and enjoyable on any platform.

![ZodiacPairs wireframe](/assets/images/docs/wireframe.png)  


# Features

The game website consists of only one initial page that starts with a header, buttons to access information about the game rules and the zodiac constellations, play and replay buttons, as well as a game stats bar that is activated only when the player presses the "play" button. At this point, the game board with the cards is displayed. Additionally, there are three modal windows: one for the rules, another for game information, and a final one that is displayed when the game concludes.


## Background

High-resolution images, harmonizing with the game's theme, were chosen for the backgrounds. Tailored for an array of screen sizes, be it the expansive displays of computers or the more compact screens of smartphones and tablets, each image was curated to fit seamlessly. This approach was employed to elevate the visual experience, regardless of the device in use.

![ZodiacPairs backgrownd images - image hero](/assets/images/docs/sizes-bg.png)

### Favicon

The favicon has been added with the game logo in the browser tab.

![ZodiacPairs backgrownd images - image hero](/assets/images/docs/favicon-zp.png)

## Sections

### Header

In the header, there is a custom-designed logo created specifically for the game, accompanied by an inviting phrase encouraging users to play.

![ZodiacPairs header](/assets/images/docs/header.png)

### Informational Buttons

Below the header, users will find there are two informational buttons. 
  
![ZodiacPairs info buttons](/assets/images/docs/info-btns.png)

When clicked, one opens a modal window explaining the rules and scoring of the game, while the other provides a brief explanation about the zodiac sign constellations.

#### How to play:

![ZodiacPairs info buttons](/assets/images/docs/how-play.png)

#### Discover Zodiac Constellations:

![ZodiacPairs info buttons](/assets/images/docs/info-const.png)

### Play and Restart Buttons

* Following that, we have the 'Play' and 'Replay' buttons section. 
* The 'Play' button has been prominently styled to emphasize its role as the central starting point for the user experience

![ZodiacPairs info buttons](/assets/images/docs/play-btns.png)

### Game board:

* The game board is designed to display only when the player presses the 'Play' or 'Replay' buttons. 
* For the memory card game, images of zodiac constellations were used. 
* A custom back card with the game's name was created. 
* When the player matches the corresponding pairs of constellations, the name of the zodiac sign to which the constellation belongs is revealed.

![ZodiacPairs game board cards back](/assets/images/docs/cards-back.png)

![ZodiacPairs game board cards](/assets/images/docs/cards.png)

### Final Game Modal Window:

At the end of the game, a modal window is displayed, informing whether the player has won or lost, as well as presenting the final score, the number of moves required to find the card pairs, and the elapsed time.

![ZodiacPairs final game win](/assets/images/docs/win.png)

![ZodiacPairs final game lose](/assets/images/docs/lose.png)

## Features and resources to be added in the future

* Implement a ranking system to save the best scores of players.
* Create an option for users to change the cards with other images related to the zodiac theme.
* Add a level option to the game: easy, medium, and hard.

## Accessibility 

From the project's inception, the game website's design was planned with a focus on accessibility. Special attention was given to ensure there was adequate color contrast, an easily comprehensible structure, and intuitive navigation. Additionally, practices of semantic HTML were implemented, establishing a robust foundation for the user experience.

### LightHouse 

The accessibility, performance, best practices, and SEO (Search Engine Optimization) of the website were analyzed using the LightHouse tool available in Google Chrome's DevTools.

  * Desktop

![LightHouse - desktop](/assets/images/docs/lighthouse.png)

  * Mobile
  
![LightHouse - Mobile](/assets/images/docs/lignthouse-mobile.png)  

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
| **`Background`** |
|  |  |  |  |  |
| Background-image | The background image should change according to the screen size used by the user. | Opening the game in different screen sizes. | The background image change according to the screen size. | Pass |
| **`Buttons`** |
|  |  |  |  |  |
| Play Button clicked | After clicking the play button, the memory game board is displayed, and the timer starts counting seconds.| Clicked play button | The game board is displayed and the timer starts. | Pass |
| Play-hover | When hovering over the "Play" button, it transitions to a white color, signifying its clickability and responsiveness. | Hover over play button | play button transitions it to a white color. | Pass |
| How to Play-hover | When hovering over the "How to Play" button, it transitions to a gray color, signifying its clickability and responsiveness. | Hover over How to Play button | How to Play button transitions it to a gray color. | Pass |
| Discover Zodiac Constellations-hover | When hovering over the "Discover Zodiac Constellation" button, it transitions to a gray color, signifying its clickability and responsiveness. | Hover over Discover Zodiac Constellation button | Discover Zodiac Constellation button transitions it to a gray color. | Pass |
| Restart-hover | When hovering over the "Restart" button, it transitions to a gray color, signifying its clickability and responsiveness. | Hover over Restart button | Restart button transitions it to a gray color. | Pass |
| Restart Button clicked | When the 'Restart' button is pressed, all cards are flipped and shuffled, and the timer starts counting seconds | Clicked restart button | All cards are flipped and shuffled, and the timer starts counting seconds. | Pass |
| **`Cards`** |
|  |  |  |  |  |
| Card-clicked | When clicking on a card, it should flip to reveal the image. | Clicked card | Flip to reveal the image. | Pass |
| Cards-Match | When two open cards are a match, they remain open, revealing the name of the sign constellation, and unlock the game board for the next move.| Clicked two cards match | they remain open with the name of the sign constellation, and unlock the game board. | Pass |
| Cards-Unmatch | When two cards do not match, they flip back, releasing the game board for the next move.| Clicked two cards unmatch | they flip back, and unlock the game board. | Pass |
| **`Stats Bar`** |
|  |  |  |  |  |
| Pairs Match | When pairs match, the "Match" adds 1 point. | Clicked two cards match | The "match" adds 1 point. | Pass |
| Pairs Unmatch | When two cards do not match, the "Unmatch" adds 1 point. | Clicked two cards unmatch | The "Unmatch" adds 1 point. | Pass |
| Score | The score starts at zero and changes according to the user's moves. Making a pair adds 50 points, while each unmatch deducts 10 points.| Clicking on the cards and attempting to find the pairs. | The score correctly changes according to the pairs. | Pass |
| Time | The timer is expected to start counting seconds as soon as the user presses 'Play' or 'Replay', and it should stop when all pairs are found.|  Pressed 'Play' or 'Replay', and finishing game| The timer starts counting seconds as soon as the user presses 'Play' or 'Replay', and stops when all pairs are found.| Pass |
| Reset | The stats bar should reset to zero with each 'Play' or 'Restart' of the game. |  Finishing the game and pressing the 'Play/Restart' buttons. | Stats bar reset to zero| Pass |
| **`Info-Modals`** |
|  |  |  |  |  |
| How to play | When clicking the respective button, a modal window with information should open. It should close when clicking the 'x'.| Clicked 'How to play' and 'x' | Opens with information and and close correctly when requested. | Pass |
| Consttelations info | When clicking the respective button, a modal window with scrollable information and an image should open. It should close when clicking the 'x'.| Clicked 'Discover Zodiac Constellations' and 'x' | Opens with scrollable information and an image and it closes correctly when requested. | Pass |
| **`Final-Modal`** |
|  |  |  |  |  |
| Win Modal | When finishing game, if the score minus the seconds used in the game is above zero, the game should open a modal window with the text 'You Win', displaying final score, time used, and number of pairs clicked. The window should close when clicking the 'x'.| Finishing game with final score above zero| The window opened correctly, with the correct calculations and phrase, and closed when requested. | Pass |
| Lose Modal | When finishing game, if the score minus the seconds used in the game is below zero, the game should open a modal window with the text 'You Lose :(' displaying the final score, time used, and the number of pairs clicked. The window should close when clicking the 'x'| Finishing game with final score below zero| The window opened correctly, with the correct calculations and phrase, and closed when requested. | Pass |

### Validator Testing  

* HTML:  

No errors were found during the validation process using the official W3C validator.  

![W3C validator - Index](/assets/images/docs/html-check.png) 

* CSS:  

No errors were found during the validation process using the official Jigsaw validator. 

![Jigsaw validator - Css](/assets/images/docs/css-validator.png)  

* JavaScript: 
 
No errors were found during the validation process using the official JSHint, a JavaScript Code Quality Tool.

![Jigsaw validator - Css](/assets/images/docs/jshint.png)  


### Bugs

#### Solved Bugs

* Backgrownd image

During the project development, I encountered challenges while trying to set up a background image that would cover the entire page. The solution was to apply certain settings for the image directly to the < html > element instead of the < body >. This allowed the image to effectively fill the entire page, regardless of the browser's size.

![Solved bug - background image](/assets/images/docs/background-solved.png)

* Reset game

While working on the game development, I encountered an issue where the game status wasn't resetting properly upon finishing a match and requesting to play again. After some attempts, I realized that in addition to resetting the variable values to zero within the restartGame() function, it was also necessary to utilize the innerText property by adding the '0'(zero). This property proved to be crucial in directly inserting the zeroed values into the interface every time the game was restarted.

![Solved bug - reset stats](/assets/images/docs/reset-solved.png)  


* Adapting Content for Small Screens

Despite using the Flexbox model for the game website development, I noticed a scrolling issue where the game was not adapting ideally to smaller mobile screens. To address this, I utilized Google Developer Tools to systematically remove elements one by one. This allowed me to pinpoint that the logo was causing this problem due to its size. As a solution, I added a smaller fixed size for it in the media queries, which effectively resolved the issue.

#### Unsolved Bugs

No unfixed bugs on the website.


## Technologies Used
### Languages Used
Html, CSS and JavaScript

### Frameworks, Libraries & Programs Used

Visual Studio Code (VS Code): Utilized as a source code editor.

[Google Fonts](https://fonts.google.com/): Imported to integrate font styles into the website. 

[Font Awesome](https://fontawesome.com/): Incorporated to easily add icons across the website.

Google Dev Tools: Leveraged for debugging and testing features, as well as resolving issues related to responsiveness and styling. 

[The W3C Markup Validation Service](https://validator.w3.org/): Used to validate the accuracy and validity of HTML code.

[The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/): Employed to validate the correctness and compliance of CSS code. 

[The official JSHint](https://jshint.com/): Used to identify issues in my Javascript code. 

[GitHub](https://github.com/): Used to save and store the website files.

## Deployment  

* Go to the main page of your GitHub repository and click on the "Settings" button.

* In the left-hand side menu, navigate to the "Code and automation" section and select "Pages."

* In the build and deployment area, choose "Deploy from a branch" and select the "main" branch and the root directory ("/").

* Click on the "Save" button to confirm the settings.

* It may take a few minutes for the website to be displayed on GitHub Pages.

You can access the live website by clicking [here](https://brunarihl.github.io/ZodiacPairs-Memory-Game/).

## Credits

### Code

While working on the development of my game, there were occasions where I needed to conduct research that covered topics beyond the scope of the course or even required thorough revision. Below, I am sharing the links to the consulted sources:

* [Dev - Javascript DOM manipulation cheatsheet](https://dev.to/m0nm/javascript-dom-manipulation-cheatsheet-1jkb)

* [FreeCodeCamp - How to clone an array in JavaScript](https://www.freecodecamp.org/news/how-to-clone-an-array-in-javascript-1d3183468f6a/)

* [FreeCodeCamp - How to Build a Modal with JavaScript](https://www.freecodecamp.org/news/how-to-build-a-modal-with-javascript/)

* [FreeCodeCamp - Click Event in JavaScript](https://www.freecodecamp.org/portuguese/news/tutorial-sobre-button-onclick-em-html-e-evento-de-clique-em-javascript/)

* [Raul Esteves - Fisher-Yates Algorithm ](https://raullesteves.medium.com/algoritmo-de-fisher-yates-para-embaralhamento-de-arrays-ba13a0542e88)

* [w3schools - Window setInterval()](https://www.w3schools.com/jsref/met_win_setinterval.asp)

* [w3schools - JavaScript Timing Events](https://www.w3schools.com/js/js_timing.asp)

* [w3schools - JavaScript HTML DOM EventListener](https://www.w3schools.com/js/js_htmldom_eventlistener.asp)

* [FreeCodeCamp - CSS Background Image Size Tutorial](https://www.freecodecamp.org/portuguese/news/tutorial-de-tamanho-de-imagem-de-fundo-em-css-como-inserir-uma-imagem-de-fundo-de-pagina-inteira/#:~:text=A%20magia%20acontece%20com%20a,caso%2C%20todo%20o%20html%20)

* [Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/): used as a resource for implementing flexible and responsive layouts on the website. 

* [README Example](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md): To write the README file, I followed the structure and table format (testing section) from the readme-examples repository by Kera Cudmore.

* The foundation of the website's was established using the CI Love Maths project as a starting point.

### Content

I created the content on the website.
* [Space](https://www.space.com/15722-constellations.html) and [Constellation Guide](https://www.constellation-guide.com/constellation-map/zodiac-constellations/): websites used as a source of research for content related to the constellations of the zodiac signs.

### Media

PowerPoint: Utilized to create the design for my game project.

[Canva](https://www.canva.com/): used to create the custom design of the memory card game.

[Favicon.io](https://favicon.io/favicon-converter/): utilized to convert the star image from the logo into a favicon.

[Adobe Express](https://www.adobe.com/br/express/feature/image/resize): utilized for image manipulation and resizing.

MS Paint: used to edit the images. 

[Logo](https://logo.shapefactory.co/?a=3EBDF8&b=7661C5): utilized to create the logo. 

[Coolors](https://coolors.co/f08080-f4978e-f8ad9d-fbc4ab-ffdab9): utilized to create the color palette. 

[Unsplash](https://unsplash.com/) and [Freepik](https://br.freepik.com/): used to source images for the game website. 

[Am I Responsive?](https://ui.dev/amiresponsive) and [Morckup Generator](https://techsini.com/multi-mockup/index.php): utilized to view the website's appearance and responsiveness across a range of devices.

### Acknowledgments

I would like to extend my sincere gratitude to the individuals who offered their assistance and support throughout the entirety of this project:

Jubril Akolade, my mentor, for his guidance and constructive feedback.

Laura Mayock, the Cohort Facilitator at Code Institute, for consistently steering our studies in the most effective direction.

My friends Ivan Frezza and Bruna Andelieri, who provided valuable insights and clarified uncertainties about my code.

My husband Jasser, for always motivating me, for his unwavering support, and for his patience throughout my study period.