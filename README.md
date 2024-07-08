# Fitness tracker project

[View the deployed project here](https://fitness-tracker-mt-b349b401ceed.herokuapp.com/)

Fun Stats is a quiz website offering 4 different categories: History, Science, Arts and Sports. The quiz is unconventional in the sense that the answers to all questions lies in the figures or statistics behind a certain event or phenomenon. The aim is to let the user grasp how huge/small or old/recent an event or a phenomenon really is.

![Mockup](documentation/features/mockup.png)


## Contents
* [User Experience (UX)](#user-experience-ux) 
* [Design](#design)
    * [Color scheme](#color-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
    * [Wireframes](#wireframes)
    * [Accessibility](#accessibility)
* [Features](#features)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks, Libraries & Programs](#frameworks-libraries--programs)
* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Browser Compatibility](#browser-compatibility)
    * [Accessibility and Performance](#accessibility-and-performance)
    * [Test Cases and Results](#test-cases-and-results)
    * [Known Bugs](#known-bugs)
* [Deployment & Local Development](#deployment--local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
* [Credits](#credits)
    * [Code Used](#code-used)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgement](#acknowledgement)

- - -

## User Experience (UX)

### User Stories

#### First Time Visitor Goals

* I want to get informed about some interesting facts
* I want to increase my knowledge in different topics
* I want the game rules to be easily accessible
* I want to easily navigate from category to another


#### Returning Visitor Goals

* I want to know more facts 
* I want to check out other categories
* I want to improve my score

#### Frequent Visitor Goals

* I want to get a perfect score and solve as many questions with the exact correct answer
* I want to check out other categories

- - -

## Design

### Color Scheme

The colors chosen were based on pantone color palette like as in [here](https://www.pinterest.com/pin/128563764357456253/). The dashboard background was inspired by the "Active" color palette in the book "Color Harmony" by Leatrice Eiseman. The colors are to represent a vibrant, summer and outdoor moods.
<br>
<br>

<p align="center">
    <img src="documentation/design/color-palette.png" alt="Color Palette" height="400px">
</p>


### Typography

Google Fonts was used to import the chosen fonts. The three main fonts used across the website are

* [Segwick Ave](https://fonts.google.com/specimen/Sedgwick+Ave) for the page header or title
* [Platypi](https://fonts.google.com/specimen/Platypi) for the answers as well as the game rules text
* The `Indie Flower` font was inspired by [this page on Medium](https://bootcamp.uxdesign.cc/10-best-script-and-handwritten-google-fonts-afc4b77fdb0c). It was used mainly for the questions.

These fonts were chosen to convey the playful nature of the website since it is a quiz. Also, I wanted to deliver this hand-written feeling to attract users from different ages.

### Imagery

* The images chosen next as a cover to each category as well as the icons in the header are to reflect the category's nature.

### Wireframes

* Wireframes were created using [balsamiq](https://balsamiq.com/). The following images serve as a preliminary design for the website interface and intended functionality.

<p align="center">
<img src="documentation/design/index.png" alt="home" width="45%">
<img src="documentation/design/science.png" alt="science-quiz" width="45%">
</p>

<p align="center">
<img src="documentation/design/science_almost_correct.png" alt="home" width="45%">
<img src="documentation/design/science_bullseye.png" alt="science-quiz" width="45%">
</p>


### Accessibility

The website is as accessible as possible. Specifically by following these good-practice guidelines

* Accessible Rich Internet Applications (Aria) labels on interactive elements, links and icons
* Semantic HTML
* Using a hover state on all buttons on the website
* Sufficient color contrast throughout the website

I used the chrome extension [Web Disability Simulator](https://chrome.google.com/webstore/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) to check for **total** as well as **Yellow-blue color blindness (Tritanopia)** color blindness. The latter was checked as blue is the prevailing color throughout the website. The reults are shown here, respectively.

<p align="center">
<img src="documentation/design/total-color-blindness.png" alt="total blindness" width="60%">
<img src="documentation/design/tritanopia.png" alt="tritanopia" width="60%">
</p>

As can be seen, there is still enough contrast between the text and the background.

- - - 

### Features

The website consists of 
* Home page with quick links to different quiz categories, contact and about pages
* Four categories pages to display quiz questions, slider and score
* Contact page to message the website hosts
* About page to explain what the website is about and what it aims at

The main features of the website are

* A **favicon** in the browser tab.

<p align="center">
<img src="documentation/features/favicon.png" alt="favicon" width="20%">
</p>

* Easily accessible icons to choose a category through text or image. Also the icons have zoom and hover effect to highlight what category the user is about to select.

<p align="center">
<img src="documentation/features/hover-icons.png" alt="hover-zoom-effect" width="60%">
</p>

*  **Toggle dialog box** to present additional information regarding game rules **without filling the page with text**.

<p align="center">
<img src="documentation/features/toggle-box-closed.png" alt="togle-box-closed" width="60%"> <br><br>
<img src="documentation/features/toggle-box-open.png" alt="togle-box-closed" width="60%">
</p>

* Quiz main area where the category is shown in the title, the question is displayed underneath and a slider to select the answer within a certain range and a submit button to submit the answer. The user's choice is shown as they move the slider

* A score box where the user's points are recorded and updated

<p align="center">
<img src="documentation/features/quiz-main-area.png" alt="quiz-window" width="60%">
</p>

* A modal winow "Game Over!" when the user inputs a wrong answer

<p align="center">
<img src="documentation/features/modal-loss.png" alt="modal-window-loss" width="60%">
</p>


* A modal winow "Congrats!" when the user answers all answers correctly

<p align="center">
<img src="documentation/features/modal-win.png" alt="modal-window-win" width="60%">
</p>

* About and contact pages to provide more context and depth to the website by providing form to the user to fill and information to read about the website. These pages also have buttons to navigate to the homepage

<p align="center">
<img src="documentation/features/contact.png" alt="contact-page" width="60%"> <br><br>
<img src="documentation/features/about.png" alt="about-page" width="60%">
</p>



* Future Implementations that shall allow returning and frequent users to visit more often

    * After getting 10 correct answers, the difficulty level goes up, so now your answer has to be the exact correct answer
    * Showing users the total points they could have got if they answered all questions precisely
    * Score leaderboard to make the quiz app more competitive between users

- - -

## Technologies Used

### Languages

* HTML5
* CSS3
* JavaScript

### Frameworks, Libraries & Programs 

* [Git](https://git-scm.com/) for version control

* [Github](https://github.com/) to store code and other files

* [GitPod](https://gitpod.io/) IDE to create and edit the codes

* [Google Fonts](https://fonts.google.com/) to import the fonts used on the website.

* [Google Developer Tools](https://developers.google.com/web/tools) for troubleshooting, checking responsiveness and styling

* [Fontawesome](https://fontawesome.com/) for the icons near the header

* [Ilovemage](https://www.iloveimg.com/) to compress and resize images

* [Cloud Convert](https://cloudconvert.com/jpg-to-webp) to convert jpg to webp images

* [Techsini](https://techsini.com/multi-mockup/) to show the website image on a range of devices

* [Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check the performance, quality, and correctness of the webpage

* [Web Disability Simulator](https://chrome.google.com/webstore/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) to simulate other accessibility needs

* [Color Picker](https://imagecolorpicker.com/en) for choosing colors from color palettes

* [balsamiq](https://balsamiq.com/) for wireframes

* [JSON](https://www.json.org/json-en.html) for writing the questions database


- - -


## Testing

### Validator Testing

* [HTML Validator](https://validator.w3.org/) result for the `.html` files were as following:
    
    * For the index or home page

    <p align="center">
    <img src="documentation/testing/html-validator-index.png" alt="html-validation-index" width="90%">
    </p>

    * For the quiz pages (all categories) showed the same warnings

    <p align="center">
    <img src="documentation/testing/html-validator-quiz-pages.png" alt="html-validation-quiz" width="90%">
    </p>

    * For the contact page

    <p align="center">
    <img src="documentation/testing/html-validator-contact.png" alt="html-validation-contact" width="90%">
    </p>

    * For the about page

    <p align="center">
    <img src="documentation/testing/html-validator-about.png" alt="html-validation-about" width="90%">
    </p>

As seen, there are no errors and only warnings of no heading was obtained. This does not affect the functionality of the website by any means.

* [CSS Validator](https://jigsaw.w3.org/css-validator/) result for the `.css` file showed no errors, however it showed 9 warnings related to the importing of google fonts and using vendor extensions. These warnings do not affect the deployment of the website by any means

<p align="center">
<img src="documentation/testing/css-validation.png" alt="css validation" width="80%">
</p>

<p align="center">
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

<p align="center">
<img src="documentation/testing/css-warnings.png" alt="css validation" width="80%">
</p>

* [JavaScript Validator](https://jshint.com/) result for the `.js` file showed no errors, however it showed 8 warnings, all on one line where the database is imported. These warnings do not affect the logic handling, datastructure or flow control of the script.

<p align="center">
<img src="documentation/testing/js-validator.png" alt="js-validation" width="40%">
</p>

* [JSON Validator](https://jsonlint.com/) showed that the JSON file is valid

<p align="center">
<img src="documentation/testing/json-validator.png" alt="json-validation" width="50%">
</p>


### Browser Compatibility

* Testing has been carried out on the following browsers :
    * Chrome 123.0.6312.86 (Official Build) (64-bit)
    * Chrome 123.0.6312.99
    * Firefox 124.0.1 (64-bit) 

### Accessibility and performance

These tests were carried out using Lighthouse


`index.html`

<p align="center">
<img src="documentation/testing/lighthouse-home.png" alt="lighthouse-home" width="40%">
</p>


Quiz pages

<p align="center">
<img src="documentation/testing/lighthouse-quiz.png" alt="lighthouse-quiz" width="40%">
</p>


`contact.html`

<p align="center">
<img src="documentation/testing/lighthouse-contact.png" alt="lighthouse-contact" width="40%">
</p>

`about.html`

<p align="center">
<img src="documentation/testing/lighthouse-about.png" alt="lighthouse-about" width="40%">
</p>


The website scores very high on accessibility, best practices and search engine optimization. Performance can still be improved.

### Test Cases and Results

The following test cases were performed on each page

* Home page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Category hover with zoom | image and text are zoomed and box gets highlighted | mouse hover | image and text are zoomed and box shadow color changes | Pass |
| Toggle box for the game rules | Box opens with game rules when clicked | mouse click | game rules are displayed | Pass |
| Internal navigation | User is directed to About, Contact and category pages | mouse click | gets directed to the respective page | Pass |
| External navigation | User is directed to social media pages | mouse click | gets directed to the respective page in a new tab | Pass |

* Quiz pages

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Focus on slider on page load | the focus is on the slider to allow keyboard use to move slider | load or reload page | pressing up/down or left/right moves the slider | Pass |
| Submitting through Enter key | pressing enter shall allow the user to submit without using the mouse | Enter key press | answer is submitted | Pass |
| Submitting through button | user can submit through mouse click on submit button | mouse click | answer is submitted | Pass |
| Getting correct but not exact answers | if user gets correct but not exact answer, they get 1 point | submit +1 or -1 from the correct answer | score tally increases by 1 | Pass |
| Getting correct and exact answers | if user gets correct and exact answer, they get 3 points | submit the correct answer | score tally increases by 3 | Pass |
| Message on wrong answer | if user gets wrong answer, the quiz ends with game over message | submit the wrong answer | modal window appears with game over message | Pass |
| Message on finishing the quiz | if user gets correct or semi-correct answers, they get congrats message | finish the quiz successfully | modal window appears with congrats message | Pass |


* About page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Internal navigation in the same tab | User is the home page | mouse click | gets directed to the home page | Pass |


* Contact page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Internal navigation | User is the home page | mouse click | gets directed to the home page | Pass |
| Reject numbers in the name field | alert appears if numbers are entered in the name field | write numbers in name field | alert pops up | Pass |
| Submit form validation | user gets directed to thanks page | submit the form by clicking send button | directs to thanks page | Pass |


### Known Bugs

* The website depends on *Font Awesome* package. If *Font Awesome* is down, the icons do not load and so the footer would not look as intended. The icons next to quiz page headers also will not load. This was encountered once when *Font Awesome* was having major issues.

* In small displays, the range values sometimes are squeezed by the slider when the value has large string length. A compromisation has to be done by reducing the slider length to fit the minimum and maximum values. However, this will reduce the slider area, thus affecting the user interface on mobile devices.


- - -


## Deployment & Local Development

### Deployment

The website is deployed using GitHub Pages. To Deploy the website:

1. Go to the [fun-stats](https://github.com/mtelewa/fun-stats/) repository for this project on Github - this was the initial name of the website
2. Navigate to settings/pages
3. From the source dropdown select "Deploy from a branch" and press save
4. The site has now been deployed and the website goes live

### Local Development

#### How to Fork

To fork the repository:

1. Go to the [fun-stats](https://github.com/mtelewa/fun-stats/) repository
2. Click the "Fork" button in the top right corner.

#### How to Clone

To clone the repository:

1. Go to the [fun-stats](https://github.com/mtelewa/fun-stats/) repository
2. Click on the "Code" button, select "SSH" and copy the link
3. Open the terminal and change the current working directory to the location you want the cloned directory to be in
4. Use the command `git clone git@github.com:mtelewa/fun-stats.git` into the terminal

Note: For step no.4 to work, first generate SSH keys and add your generated key in Account Settings -> SSH Keys. More on this can be found on the [github docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

- - -

## Credits

### Code Used

* Hover to zoom effect [CSS snippet](https://www.w3schools.com/howto/howto_css_zoom_hover.asp)
* 



* 













https://stackoverflow.com/questions/33680908/how-to-redirect-to-url-by-cancel-button-in-django-crispy-forms


https://stackoverflow.com/questions/46314246/how-to-update-a-foreign-key-field-in-django-models-py



https://jqueryui.com/datepicker/
https://stackoverflow.com/questions/5250244/jquery-date-formatting


https://stackoverflow.com/questions/1353684/detecting-an-invalid-date-date-instance-in-javascript


https://stackoverflow.com/questions/25632918/django-crispy-forms-file-upload


https://api.jquery.com/jQuery.ajax/


https://stackoverflow.com/questions/72529252/how-to-get-select-option-value-in-views-django


API
https://api-ninjas.com/api/caloriesburned


https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters

https://stackoverflow.com/questions/3617797/regex-to-match-only-letters

https://stackoverflow.com/questions/40534715/how-to-embed-matplotlib-graph-in-django-webpage


https://towardsdatascience.com/upgrade-your-data-visualisations-4-python-libraries-to-enhance-your-matplotlib-charts-74361bc3b92e





### Content

* The idea and content of the webpage are my own. I had the inspiration for building a fitness tracker app and some challenges to tackle from [dev](https://dev.to/arafat4693/top-10-full-stack-projects-for-beginners-1338).

### Media

* [Runner image](https://www.freepik.com/free-photo/silhouette-young-fitness-man-running-sunrise_5212275.htm#fromView=search&page=1&position=10&uuid=98ede3d9-7cb9-4655-8895-97f967457ce1)
* [Swimmer image](https://www.freepik.com/free-photo/side-view-female-swimmer-with-cap-goggles-swimming-water_10296634.htm#fromView=search&page=1&position=2&uuid=4ffe75cb-1350-45fd-a92e-041aa8d949b9)
* [Kayaking image](https://www.freepik.com/free-photo/kayaking-man-paddling-kayak-canoeing-paddling_26921714.htm#fromView=search&page=1&position=9&uuid=61a985f1-7f60-4b00-916f-31656f04c379)
* [Lifting image](https://www.freepik.com/free-photo/low-angle-view-unrecognizable-muscular-build-man-preparing-lifting-barbell-health-club_25743546.htm#fromView=search&page=1&position=0&uuid=e541bca9-0193-4687-b077-c0d88bc50b43)
* [CyberPunk Plot](https://www.analyticsvidhya.com/blog/2021/07/cyberpunk-themed-charts-advanced-data-visualization-in-python/)


### Acknowledgement

I would like to thank my Code Institute mentor Jubril Akolade for his feedback and support


