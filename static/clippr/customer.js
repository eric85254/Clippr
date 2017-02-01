/**
 * Created by sanketh on 1/25/17.
 */

// All Divs
var menuMainDiv = document.getElementById('menu_main_div');
var stylistSearchDiv = document.getElementById('stylist_search');

//Buttons
var shortCutButton = document.getElementById('short_cut');
var longCutButton = document.getElementById('long_cut');
var createAppointmentButton = document.getElementById('create_appointment_button');

//Forms
var createAppointmentForm = document.getElementById('create_appointment_form');

//text
var menuChoiceText = document.getElementById('menu_choice');

//hidden fields
var menuMainField = document.getElementById('menu_main');

function init() {
    if (stylistSearchDiv) {
        stylistSearchDiv.setAttribute("class", "hidden");
        console.log('hiding search division');
    }

    if (shortCutButton) {
        shortCutButton.onclick = shortCutButtonAction;
    }

    if (longCutButton) {
        longCutButton.onclick = longCutButtonAction;
    }

    if (createAppointmentButton) {
        createAppointmentButton = createAppointment;
    }
}

function shortCutButtonAction() {
    menuChoiceText.innerHTML = "Short Cut";
    menuMainField.value = "short_cut";
    showStylistSearch();
}

function longCutButtonAction() {
    menuChoiceText.innerHTML = "Long Cut";
    menuMainField.value = "long_cut";
    showStylistSearch();
}

function createAppointment() {
    event.preventDefault();
    $.ajax({
        url: $(createAppointmentForm).attr("action"),
        type: "post",
        data: $(createAppointmentForm).serialize(),
        success: showStylistSearch()
    });
    console.log('sent menu choices!');
}

function showStylistSearch() {
    if (stylistSearchDiv) {
        stylistSearchDiv.setAttribute("class", "visible");
    }
    console.log('showing stylist search');
}

window.onload = init;