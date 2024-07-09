# Fitness Tracker project

![Mockup](documentation/features/mockup.png)

Fitness Tracker is the app to help you stay on top of your fitness goals and lead a healthier life. Designed for both beginners and fitness enthusiasts, Fitness Tracker offers a comprehensive suite of features to track your physical activities with calories burnt counter, log your meals with calories intake counter, and set personalized weight targets.

Link to live site - [https://fitness-tracker-mt-b349b401ceed.herokuapp.com/](https://fitness-tracker-mt-b349b401ceed.herokuapp.com/)


## Contents
* [Concept](#concept)
* [User Experience (UX)](#user-experience-ux) 
    * [Target Audience](#target-audience)
    * [User Stories](#user-stories)
        * [Existing Users](#existing-users)
        * [New Users](#new-users)
        * [Site Owner](#site-owner)
* [Design](#design)
    * [Color scheme](#color-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
    * [Accessibility](#accessibility)
    * [Wireframes](#wireframes)
    * [Data Base](#data-base-management) 
* [Features](#features)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks, Libraries & Programs](#frameworks-libraries--programs)
* [Testing](#testing)
* [Deployment & Local Development](#deployment--local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
* [Credits](#credits)
    * [Code Used](#code-used)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgement](#acknowledgement)

- - -

## Concept

The app is for anyone who wants to keep track of their fitness level by creating a diary or logs of their activities and nutrition plans. The app consists of 4 main cards on the dashboard, these are:
1. Profile card: this here is not the usual social profile rather the metric profile (weight, target weight, height and birth date). This input is used to calculate the user's body mass index (BMI), basal metabolic rate (BMR) and a classification of the user's metrics.

2. Activity card: the user can log and track here any activity alongside the intensity, duration and distance. An API is fetched to compute the calories burnt by the user and displays the value on the card.

3. Nutrition card: the user can log and track their meals and the serving. Similar to the activity card, a calorie intake calculator API is fetched and displayed.

4. Calendar card (WIP): the user can view their logged in activities and meals, if desired. Only the calendar display has been implemented for a test user to show how it should look like. Creating and deleting events from/to the calendar has not been implemented yet.

The data in the first three cards are saved to the PostgreSQL database as custom models in Django. 

## User Experience (UX)

### Target Audience

Users of all ages and genders are welcome to use the app. The fact that users can update their height as well as other metrics encourages also users of young age to take part and track their fitness measures.

### User Stories

Agile methods have been utilised in the project using [Github's Projects Kanban board](https://github.com/users/mtelewa/projects/5/views/1). Here is a brief summary of the main user stories.

#### Existing users

* As a **Site User** I can **login to the website** so that **I can access my dashboard**
*  As a **Site User** I can **log my activity/nutrition/profile session** so that **I can track my performance**
* As a **Site User** I can **input a food item** so that **I get calories intake**
As a **Site User** I can **input activity duration and distance** so that **I get calories burnt count**
* As a **Site User** I can **input target weight** so that **I stay on track**
* As a **Site User** I can **input my birth date** so that **my age updates automatically and so measurements are accurate**
* As a **Site User** I can **update my profile attributes** so that **it shows on my profile page**
*  As a **Site User** I can **see plots of my activity/nutrition/profile data** so that **I track my performance**
* As a **Site User** I can **see the difference between target and current metrics on dashboard** so that **I can check how far i am from the target**


#### New Users

* As a **Site User** I can **create a metric profile** so that **it shows on my profile page**
* As a **Site User** I can **sign up to the website** so that **I can access my dashboard**

#### Site Owner

* As a **Site Owner** I can **connect to Django database** so that **I see apps on admin dashboard**
* As a **Site Owner** I can **show the dashboard only to authenticated users** so that **users sign up/in**

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

* [Libre Baskerville](https://fonts.google.com/specimen/Libre+Baskerville) for the page header or title
* [Lemonada](https://fonts.google.com/specimen/Lemonada) for the cards titles and the calorie counters
* [Palanquin](https://fonts.google.com/specimen/Palanquin). It was used for the cards paragraph text.

These fonts were chosen to convey an active dynamic environment.

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

    * 

- - -

## Technologies Used

### Languages

* HTML5
* CSS3
* JavaScript (with jQuery)
* Python3.12.3

### Frameworks, Libraries & Programs 

* [Git](https://git-scm.com/) for version control

* [Github](https://github.com/) to store code and other files

* [GitPod](https://gitpod.io/) IDE to create and edit the codes

* [Google Fonts](https://fonts.google.com/) to import the fonts used on the website.

* [Google Developer Tools](https://developers.google.com/web/tools) for troubleshooting, checking responsiveness and styling

* [Fontawesome](https://fontawesome.com/) for the icons near the header

* [Bootstrap](https://getbootstrap.com/) for the styling of the templates

* [Heroku](https://www.heroku.com/) for cloud application deployment

* [drawSQL](https://drawsql.app/) to desing the entity relationship diagram (ERD)

* [API Ninjas](https://api-ninjas.com/) for these 2 APIs:

    * Calories burnt [API](https://api-ninjas.com/api/caloriesburned)
    * Nutrition Calories [API](https://api-ninjas.com/api/nutrition)

* [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) to provide the database

* [Django](https://www.djangoproject.com/) to manage the backend database

* [Django Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) to manage forms

* [allauth template](https://docs.allauth.org/en/latest/common/templates.html) for signin, signup and logout templates

* [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adposition=&gad_source=1&gclid=CjwKCAjwnK60BhA9EiwAmpHZwy2kAjmhDnHieTvklfuHGv7o3aiSJqrMtHQM8C58vsCkbwrm9aQYnBoCYdwQAvD_BwE) to manage media uploads

* [Ilovemage](https://www.iloveimg.com/) to compress and resize images

* [Cloud Convert](https://cloudconvert.com/jpg-to-webp) to convert jpg to webp images

* [Techsini](https://techsini.com/multi-mockup/) to show the website image on a range of devices

* [Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check the performance, quality, and correctness of the webpage

* [Web Disability Simulator](https://chrome.google.com/webstore/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) to simulate other accessibility needs

* [Color Picker](https://imagecolorpicker.com/en) for choosing colors from color palettes

* [balsamiq](https://balsamiq.com/) for wireframes

* [JSON](https://www.json.org/json-en.html) for writing the fixtures

* In addition to some of the Python libraries imported in the python files which are listed in the `requirements.txt`

- - -


## Testing

Please refer to [TESTING.md](TESTING.md) for all the testing carriied out.

- - -


## Deployment & Local Development

### Deployment

The app is deployed using [Heroku](https://www.heroku.com/) platform. To Deploy the app:

1. Create a new app, add a unique app name (e.g. flight-scanner) and then choose the region
2. Click on "Create app"
3. Go to "Settings"
4. Under Config Vars add the following KEY-VALUE pairs
    * CAL_BURN_API_KEY : `API  Key obtained from API Ninjas`
    * CLOUDINARY_URL : `CLOUDINARY KEY`
    * DATABASE_URL : `PostgreSQL URL from Code Institute`
    * SECRET_KEY : `Provided by Django initialization or from https://djecrety.ir/`
    * PORT: `8000`
5. Go to "Deploy" and select "GitHub" in "Deployment method"
6. To connect Heroku app to the Github repository enter the repository name, click 'Search' and then 'Connect'.
7. Choose the branch you want to build your app from, here it was `main`
8. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
9. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

Note: In the CDE or IDE, a Procfile shall be created that contains the following command declared:
    ```
    web: gunicorn fitness_tracker.wsgi
    ```

### Local Development

#### How to Fork

To fork the repository:

1. Go to the [fitness-tracker](https://github.com/mtelewa/fitness-tracker) repository
2. Click the "Fork" button in the top right corner.

#### How to Clone

To clone the repository:

1. Go to the [fitness-tracker](https://github.com/mtelewa/fitness-tracker) repository
2. Click on the "Code" button, select "SSH" and copy the link
3. Open the terminal and change the current working directory to the location you want the cloned directory to be in
4. Use the command `git clone git@github.com:mtelewa/fitness-tracker.git` into the terminal

Note: For step no.4 to work, first generate SSH keys and add your generated key in Account Settings -> SSH Keys. More on this can be found on the [github docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

#### Local Run 

* Install all the packages in the `requirements.txt` using `pip install -r /path/to/requirements.txt`
* To run the server, in the terminal run `python3 manage.py runserver` and open the browser on the open port (usually `8000`)
* To migrate any database changes
`python3 manage.py makemigrations` followed by `python3 manage.py migrate`

- - -

## Credits

### Code Used

* Redirect cancel button in django crispy forms [snippet](https://stackoverflow.com/questions/33680908/how-to-redirect-to-url-by-cancel-button-in-django-crispy-forms)
* jQuert date formatting [snippet](https://jqueryui.com/datepicker/
https://stackoverflow.com/questions/5250244/jquery-date-formatting)
* Date validation in JS [snippet](https://stackoverflow.com/questions/1353684/detecting-an-invalid-date-date-instance-in-javascript)
* File upload in crispy forms [snippet](https://stackoverflow.com/questions/25632918/django-crispy-forms-file-upload)
* jQuery Ajax [snippet](https://api.jquery.com/jQuery.ajax/)
* Bootsrap `select` in django [snippet](https://stackoverflow.com/questions/72529252/how-to-get-select-option-value-in-views-django)
* Embed Matplotlib plots in django template [snippet](https://stackoverflow.com/questions/40534715/how-to-embed-matplotlib-graph-in-django-webpage)
* Regex to match letters only - used in activity custom model [snippet](https://stackoverflow.com/questions/3617797/regex-to-match-only-letters)
* Accept only alphanumeric characters in django form [snippet](https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters)
* CyberPunk plot [snippet](https://towardsdatascience.com/upgrade-your-data-visualisations-4-python-libraries-to-enhance-your-matplotlib-charts-74361bc3b92e)


### Content

* The idea and content of the webpage are my own. I had the inspiration for building a fitness tracker app and some challenges to tackle from [dev](https://dev.to/arafat4693/top-10-full-stack-projects-for-beginners-1338). The fixtures JSON files were made with the help of OpenAI's [GPT](https://chat.openai.com/).

### Media

* [Runner image](https://www.freepik.com/free-photo/silhouette-young-fitness-man-running-sunrise_5212275.htm#fromView=search&page=1&position=10&uuid=98ede3d9-7cb9-4655-8895-97f967457ce1)
* [Swimmer image](https://www.freepik.com/free-photo/side-view-female-swimmer-with-cap-goggles-swimming-water_10296634.htm#fromView=search&page=1&position=2&uuid=4ffe75cb-1350-45fd-a92e-041aa8d949b9)
* [Kayaking image](https://www.freepik.com/free-photo/kayaking-man-paddling-kayak-canoeing-paddling_26921714.htm#fromView=search&page=1&position=9&uuid=61a985f1-7f60-4b00-916f-31656f04c379)
* [Lifting image](https://www.freepik.com/free-photo/low-angle-view-unrecognizable-muscular-build-man-preparing-lifting-barbell-health-club_25743546.htm#fromView=search&page=1&position=0&uuid=e541bca9-0193-4687-b077-c0d88bc50b43)
* [CyberPunk Plot](https://www.analyticsvidhya.com/blog/2021/07/cyberpunk-themed-charts-advanced-data-visualization-in-python/)


### Acknowledgement

I would like to thank my Code Institute mentor Jubril Akolade for his feedback and support.
I am also thankful to Sean, my fellow student at CI for providing some tips and advise against pitfalls and generally for sharing some thoughts and nice conversations. I would like to thank Kay, our cohort facilitator for the continous motivation and support.


