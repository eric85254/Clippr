/**
 * Created by sanketh on 1/7/17.
 */


// Log in / Sign Up Page Button Variables.
var newUser = document.getElementById("new_user");
var logIn = document.getElementById("login");

// Log in / Sign up Page Form Variables
var newUserForm = document.getElementById("newUserForm");
var logInForm = document.getElementById("logInForm");

// Error Variables
var email_error = document.getElementById("email-error");
var password_error = document.getElementById("password-error");
var isStylist_error = document.getElementById("is_stylist-error");
var phone_number_error = document.getElementById("phone_number-error");

function init() {
    newUserForm.onsubmit = newUserErrorHandling;
}

function cleanUp() {
    var confirmation = document.getElementById("newUserConfirmation");
    confirmation.innerHTML = "";

    email_error.innerHTML = "";
    password_error.innerHTML = "";
    isStylist_error.innerHTML = "";
    phone_number_error.innerHTML = "";
}

function newUserErrorHandling() {
    event.preventDefault();
    $.ajax({
        url: $(newUserForm).attr("action"),
        type: "post",
        data: $(newUserForm).serialize(),
        success: function (data) {
            console.log(data);

            if (data.success == true) {
                newUser.setAttribute("class", "tab-pane");
                logIn.setAttribute("class", "tab-pane active");
            } else {
                console.log("found Errors!");
                cleanUp();

                if (data.email) {
                    email_error.innerHTML = data.email;
                }
                if(data.password2) {
                    password_error.innerHTML = data.password2;
                }
                if(data.is_stylist) {
                    isStylist_error.innerHTML = data.is_stylist;
                }
                if(data.phone_number) {
                    phone_number_error.innerHTML = data.phone_number;
                }
            }
        }
    });
    console.log("form submitted!");
}
//
window.onload = init;
