
// Sidebar
/* global bootstrap: false */
(function () {
  'use strict';
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });
})();


const updateButtons = $('.btn-update');
const deleteNutritionButton = $('#btn-delete-nutrition');
const deleteActivityButton = $('#btn-delete-activity');
const deleteProfileButton = $('#btn-delete-profile');
const deleteModalElement = $('#deleteModal');
let deleteModal;
let deleteConfirm;
if (deleteModalElement.length) {
  // Initialize the Bootstrap modal
  deleteModal = new bootstrap.Modal($('#deleteModal'));
}
const cardText = $('.card-text');
const weightText = $('#id_weight');
const targetWeightText = $('#id_weight_target');
const heightText = $('#id_height');
const birthdateText = $('#id_birthdate');
const ddash = $('.ddash');

$(document).ready(function(){
  /**
   * Upon clicking update, crispy form appears
   * and old data disappears
   */

  let showHide;
  let hideShow;

  updateButtons.click(function() {
    if (this.id == 'btn-update-metrics') {
      showHide = $('.show-hide-metrics');
      hideShow = $('.hide-show-metrics');
    } else if (this.id == 'btn-update-activity') {
      showHide = $('.show-hide-activity');
      hideShow = $('.hide-show-activity');
    } else if (this.id == 'btn-update-nutrition') {
      showHide = $('.show-hide-nutrition');
      hideShow = $('.hide-show-nutrition');
    } else if (this.id == 'btn-update-profile') {
      showHide = $('.show-hide-profile');
      hideShow = $('.hide-show-profile');
    } 
    // toggle class to hide displayed text
    showHide.toggleClass('d-none position-absolute');
    // toggle class to display and hide form
    hideShow.toggleClass('hide-show d-none');
    hideShow.toggleClass('hide-show d-block');
    // remove y-margin from the
    cardText.addClass('my-0');
  });


  // show default values
  let weight = $('#weight-val');
  weightText.val(weight.text());
  let targetWeight = $('#weight-target-val');
  targetWeightText.val(targetWeight.text());
  let height = $('#height-val');
  heightText.val(height.text());
  let birthdate = $('#birthdate-val');
  // if profile is created, show the user's birthdate
  // else show today's date
  if (isValidDate(new Date(birthdate.text()))){
    birthdateText.val($.datepicker.formatDate('dd-mm-yy', new Date(birthdate.text())));
  } else{
    birthdateText.val($.datepicker.formatDate('dd-mm-yy', new Date()));
  }

  // Date Picker
  $( function() {
    birthdateText.datepicker({ dateFormat: 'dd-mm-yy' });
  } );

  // Date validation
  function isValidDate(d) {
    return d instanceof Date && !isNaN(d);
  }

  // For new users with no previous records, show -- for None entries
  ddash.text('--');


  // Delete nutrition entries
  deleteNutritionButton.click(function() {
    deleteConfirm.href = 'nutrition_delete/';
    deleteModal.show();
  });

  // Delete profile entries
  deleteProfileButton.click(function() {
    deleteConfirm.href = 'profile_delete/';
    deleteModal.show();
  });

  // Delete activity entries
  deleteActivityButton.click(function() {
    deleteConfirm.href = 'activity_delete/';
    deleteModal.show();
  });

});


/**
 * Fetch Json data from the Calories burnt API
 * and display it as a selection in Bootstrap
 */
function fetchCaloriesBurnt(event) {

  var activityTypeValue = $('#id_activity_type').val();
  const CAL_BURN_API_KEY = JSON.parse($('#calBurnAPI').text());

  // Perform an asynchronous HTTP (Ajax) request
  $.ajax({
    url: `https://api.api-ninjas.com/v1/caloriesburned?activity=${activityTypeValue}`,
    headers: { 'X-Api-Key': CAL_BURN_API_KEY },
    method: 'GET',
    success: function(response) {
        var activity_list = response;
        var activities = [];
        for (var i = 0; i < activity_list.length; i++) {
            if (activity_list[i].hasOwnProperty('name')) {
                activities.push(activity_list[i].name);
            }
        }
        // Show activities list in the select menu
        var str = "";
        for (let i of activities) {
            str += `<option value="${i}">${i}</option>`;
        }
        $('#activity_list').html(
          `
          <select class="form-select" name="select-activity" aria-label="select activity">
            ${str}
          </select>
          `
        );
    },
    error: function(xhr) {
        console.log("Error:", xhr.status, xhr.responseText);
    }
  });
}