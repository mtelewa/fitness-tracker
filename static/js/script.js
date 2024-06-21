
// Sidebar
/* global bootstrap: false */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()


const updateButton = $('.btn-update');
const cardText = $('.card-text')
const weightText = $('#id_weight');
const targetWeightText = $('#id_target_weight');
const heightText = $('#id_height');

$(document).ready(function(){
  /**
   * Upon clicking update, crispy form appears
   * 
   */
  updateButton.click(function() {
    let showHide = $('.show-hide');
    let hideShow = $('.hide-show');
    // toggle class to hide displayed text
    showHide.toggleClass('d-none position-absolute');
    // toggle class to display and hide form
    hideShow.toggleClass('hide-show d-none')
    hideShow.toggleClass('hide-show d-block')
    // remove y-margin from the
    cardText.addClass('my-0');

    let weight = $('#weight-val');
    weightText.val(weight.text());

    let targetWeight = $('#target-weight-val');
    targetWeightText.val(targetWeight.text());

    let height = $('#height-val');
    heightText.val(height.text());

    // let birthdate = $('#age-val');
    // ageText.val();


  });
});
