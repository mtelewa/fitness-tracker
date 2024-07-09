### Validator Testing

* [HTML Validator](https://validator.w3.org/) result for the template files were as following:
    
    First for unauthorized access, the 'Validate by URI' was used and showed no errors

    * For the index template (as well as activity, nutrition, profile)

    <p align="center">
    <img src="documentation/testing/html-validator-index.png" alt="html-validation-index" width="90%">
    </p>

    Next, the validation was performed by 'Direct Input' by passing the page source. The templates (activity, nutrition and profile) showed some errors all related to one element - the SVG figure. Since this error did not affect how the figure is displayed and does not interact with other elements on the page, it was not handled.

    <p align="center">
    <img src="documentation/testing/svg-error.png" alt="svg-error" width="90%">
    </p>

    * For the index and calendar templates, an error was raised from the iframe element. The styling of the iframe width and height was also performed from the CSS file but it was ignored. So it was left within the html file. The errors do not affect how the template is displayed.

    <p align="center">
    <img src="documentation/testing/index-error.png" alt="iframe-error" width="90%">
    </p>

The aforementioned errors and warnings do not affect the functionality of the website by any means.

* [CSS Validator](https://jigsaw.w3.org/css-validator/) result for the `.css` file showed no errors, however it showed 4 warnings related to the importing of google fonts and using vendor extensions. These warnings do not affect the deployment of the website by any means

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

* [JavaScript Validator](https://jshint.com/) result for the `.js` file showed no errors, however it showed 1 warning and 1 unused variable. The warning does not affect the logic handling, data structure or flow control of the script. The unused variable is in fact an event handler function that fetched data from the calories API when user types in an activity or a meal.

<p align="center">
<img src="documentation/testing/js-validator.png" alt="js-validation" width="40%">
</p>

* [JSON Validator](https://jsonlint.com/) showed that the JSON files used in the fixtures are valid

<p align="center">
<img src="documentation/testing/json-validator.png" alt="json-validation" width="50%">
</p>

* [Python PEP8 CI Linter](https://pep8ci.herokuapp.com/) was used to check all python scripts. All clear, no errors found!


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

Dashboard

<p align="center">
<img src="documentation/testing/lighthouse-dashboard.png" alt="lighthouse-dhashboard" width="40%">
</p>

`profile.html`

<p align="center">
<img src="documentation/testing/lighthouse-profile.png" alt="lighthouse-profile" width="40%">
</p>

`activity.html`

<p align="center">
<img src="documentation/testing/lighthouse-activity.png" alt="lighthouse-activity" width="40%">
</p>

`nutrition.html`

<p align="center">
<img src="documentation/testing/lighthouse-nutrition.png" alt="lighthouse-nutrition" width="40%">
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