/**
 * Created by sanketh on 1/7/17.
 */

// // Pages that NavBar Links to
// var navHome_Link = document.getElementById("navHome-Link");
// var navSafety_Link = document.getElementById("navSafety-Link");
// var navFindYourStyle_Link = document.getElementById("navFindYourStyle-Link");
// var navBecomeAStylist_Link = document.getElementById("navBecomeAStylist-Link");
// var navLogIn_Link = document.getElementById("navLogIn-Link");
//
// // NavBar Button Variables
// var navLogo = document.getElementById("navLogo");
// var navHome = document.getElementById("navHome");
// var navSafety = document.getElementById("navSafety");
// var navFindYourStyle = document.getElementById("navFindYourStyle");
// var navBecomeAStylist = document.getElementById("navBecomeAStylist");
// var navLogIn = document.getElementById("navLogIn");
// var navProfile = document.getElementById("navProfile");
//
// // Log in / Sign Up Page Button Variables.
var newUser = document.getElementById("new_user");
var logIn = document.getElementById("login");
//
// Log in / Sign up Page Form Variables
// var newUserFormDiv = document.getElementById("newUserFormDiv");
// var logInFormDiv = document.getElementById("logInFormDiv");
var newUserForm = document.getElementById("newUserForm");
// // var logInForm = document.getElementById("logInForm");
//
// Error Variables
var email_error = document.getElementById("email-error");
var username_error = document.getElementById("username-error");
var password_error = document.getElementById("password-error");
var isStylist_error = document.getElementById("is_stylist-error");
var phone_number_error = document.getElementById("phone_number-error");
//
function init() {
    newUserForm.onsubmit = newUserErrorHandling;
}
//
// function hideAll() {
//     if (navHome_Link) {
//         navHome_Link.setAttribute("class", "hidden");
//     }
//
//     if (navSafety_Link) {
//         navSafety_Link.setAttribute("class", "hidden");
//     }
//
//     if (navFindYourStyle_Link) {
//         navFindYourStyle_Link.setAttribute("class", "hidden");
//     }
//
//     if (navBecomeAStylist_Link) {
//         navBecomeAStylist_Link.setAttribute("class", "hidden");
//     }
//
//     if (navLogIn_Link) {
//         navLogIn_Link.setAttribute("class", "hidden");
//     }
// }
//
// function deSelectAll() {
//     if (navHome_Link) {
//         navHome.parentNode.setAttribute("class", "nav-item");
//     }
//
//     if (navSafety_Link) {
//         navSafety.parentNode.setAttribute("class", "nav-item");
//     }
//
//     if (navFindYourStyle_Link) {
//         navFindYourStyle.parentNode.setAttribute("class", "nav-item");
//     }
//
//     if (navBecomeAStylist_Link) {
//         navBecomeAStylist.parentNode.setAttribute("class", "nav-item");
//     }
//
//     if (navLogIn_Link) {
//         navLogIn.parentNode.setAttribute("class", "nav-item");
//     }
// }
//
function cleanUp() {
    var confirmation = document.getElementById("newUserConfirmation");
    confirmation.innerHTML = "";

    email_error.innerHTML = "";
    username_error.innerHTML = "";
    password_error.innerHTML = "";
    isStylist_error.innerHTML = "";
    phone_number_error.innerHTML = "";
}
//
// function show_navHome_Link() {
//     hideAll();
//     deSelectAll();
//     cleanUp();
//     navHome_Link.setAttribute("class", "visible");
//     navHome.parentNode.setAttribute("class", "nav-item active");
// }
//
// function show_navSafety_Link() {
//     hideAll();
//     deSelectAll();
//     cleanUp();
//     navSafety_Link.setAttribute("class", "visible");
//     navSafety.parentNode.setAttribute("class", "nav-item active");
// }
//
// function show_navFindYourStyle_Link() {
//     hideAll();
//     deSelectAll();
//     cleanUp();
//     navFindYourStyle_Link.setAttribute("class", "visible");
//     navFindYourStyle.parentNode.setAttribute("class", "nav-item active");
// }
//
// function show_navBecomeAStylist_Link() {
//     hideAll();
//     deSelectAll();
//     cleanUp();
//     navBecomeAStylist_Link.setAttribute("class", "visible");
//     navBecomeAStylist.parentNode.setAttribute("class", "nav-item active");
// }
//
// function show_navLogIn_Link() {
//     hideAll();
//     deSelectAll();
//     cleanUp();
//     navLogIn_Link.setAttribute("class", "visible");
//     navLogIn.parentNode.setAttribute("class", "nav-item active");
//
//     newUser.setAttribute("class", "btn btn-secondary");
//     logIn.setAttribute("class", "btn btn-primary");
//     newUserFormDiv.setAttribute("class", "visible");
//     logInFormDiv.setAttribute("class", "hidden");
// }
//
// function newUserButton() {
//     cleanUp();
//     newUser.setAttribute("class", "btn btn-secondary");
//     logIn.setAttribute("class", "btn btn-primary");
//
//     newUserFormDiv.setAttribute("class", "visible");
//     logInFormDiv.setAttribute("class", "hidden");
// }
//
// function logInButton() {
//     newUser.setAttribute("class", "btn btn-primary");
//     logIn.setAttribute("class", "btn btn-secondary");
//
//     newUserFormDiv.setAttribute("class", "hidden");
//     logInFormDiv.setAttribute("class", "visible");
// }
//
// ToDo: Fix all the variable name convention
//
function newUserErrorHandling() {
    event.preventDefault();
    $.ajax({
        url: $(newUserForm).attr("action"),
        type: "post",
        data: $(newUserForm).serialize(),
        success: function (data) {
            console.log(data);
            // var formData = JSON.parse(data);

            if (data.success == true) {
                // var confirmation = document.getElementById("newUserConfirmation");
                // confirmation.innerHTML = "You've successfully created a new account!";
                newUser.setAttribute("class", "tab-pane");
                logIn.setAttribute("class", "tab-pane active");
            } else {
                console.log("found Errors!");
                cleanUp();

                if (data.email) {
                    email_error.innerHTML = data.email;
                }
                if (data.username) {
                    username_error.innerHTML = data.username;
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
//
// ToDo: For later --> get rid of commented out portions involving is_stylist field.