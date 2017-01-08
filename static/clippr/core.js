/**
 * Created by sanketh on 1/7/17.
 */
var navHome_Link = document.getElementById("navHome-Link");
var navSafety_Link = document.getElementById("navSafety-Link");
var navFindYourStyle_Link = document.getElementById("navFindYourStyle-Link");
var navBecomeAStylist_Link = document.getElementById("navBecomeAStylist-Link");
var navLogIn_Link = document.getElementById("navLogIn-Link");

var navLogo = document.getElementById("navLogo");
var navHome = document.getElementById("navHome");
var navSafety = document.getElementById("navSafety");
var navFindYourStyle = document.getElementById("navFindYourStyle");
var navBecomeAStylist = document.getElementById("navBecomeAStylist");
var navLogIn = document.getElementById("navLogIn");
var navProfile = document.getElementById("navProfile");

function init() {
    hideAll();
    show_navHome_Link();

    navLogo.onclick = show_navHome_Link;
    navHome.onclick = show_navHome_Link;
    navSafety.onclick = show_navSafety_Link;
    navFindYourStyle.onclick = show_navFindYourStyle_Link;
    navBecomeAStylist.onclick = show_navBecomeAStylist_Link;
    navLogIn.onclick = show_navLogIn_Link;
    navProfile.onclick = show_navLogIn_Link;
}

function hideAll() {
    if (navHome_Link) {
        navHome_Link.setAttribute("class", "hidden");
    }

    if (navSafety_Link) {
        navSafety_Link.setAttribute("class", "hidden");
    }

    if (navFindYourStyle_Link) {
        navFindYourStyle_Link.setAttribute("class", "hidden");
    }

    if (navBecomeAStylist_Link) {
        navBecomeAStylist_Link.setAttribute("class", "hidden");
    }

    if (navLogIn_Link) {
        navLogIn_Link.setAttribute("class", "hidden");
    }
}

function deSelectAll() {
    if (navHome_Link) {
        navHome.parentNode.setAttribute("class", "nav-item");
    }

    if (navSafety_Link) {
        navSafety.parentNode.setAttribute("class", "nav-item");
    }

    if (navFindYourStyle_Link) {
        navFindYourStyle.parentNode.setAttribute("class", "nav-item");
    }

    if (navBecomeAStylist_Link) {
        navBecomeAStylist.parentNode.setAttribute("class", "nav-item");
    }

    if (navLogIn_Link) {
        navLogIn.parentNode.setAttribute("class", "nav-item");
    }
}

function show_navHome_Link() {
    hideAll();
    deSelectAll();
    navHome_Link.setAttribute("class", "visible");
    navHome.parentNode.setAttribute("class", "nav-item active");
}

function show_navSafety_Link() {
    hideAll();
    deSelectAll();
    navSafety_Link.setAttribute("class", "visible");
    navSafety.parentNode.setAttribute("class", "nav-item active");
}

function show_navFindYourStyle_Link() {
    hideAll();
    deSelectAll();
    navFindYourStyle_Link.setAttribute("class", "visible");
    navFindYourStyle.parentNode.setAttribute("class", "nav-item active");
}

function show_navBecomeAStylist_Link() {
    hideAll();
    deSelectAll();
    navBecomeAStylist_Link.setAttribute("class", "visible");
    navBecomeAStylist.parentNode.setAttribute("class", "nav-item active");
}

function show_navLogIn_Link() {
    hideAll();
    deSelectAll();
    navLogIn_Link.setAttribute("class", "visible");
    navLogIn.parentNode.setAttribute("class", "nav-item active");
}

window.onload = init;