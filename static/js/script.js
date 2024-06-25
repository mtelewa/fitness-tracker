
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
const cardText = $('.card-text');
const weightText = $('#id_weight');
const targetWeightText = $('#id_weight_target');
const heightText = $('#id_height');
const birthdateText = $('#id_birthdate');
const ddash = $('.ddash')

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

    let targetWeight = $('#weight-target-val');
    targetWeightText.val(targetWeight.text());

    let height = $('#height-val');
    heightText.val(height.text());

    let birthdate = $('#birthdate-val');
    birthdateText.val($.datepicker.formatDate('dd-mm-yy', new Date(birthdate.text())));

  });

  // Date Picker
  $( function() {
    birthdateText.datepicker({ dateFormat: 'dd-mm-yy' });
  } );

  // For new users with no previous records, show --
  ddash.text('--');

});
