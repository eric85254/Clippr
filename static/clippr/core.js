/**
 * Created by sanketh on 1/7/17.
 */
var navHome_Link = document.getElementById("navHome-Link");
var navSafety_Link = document.getElementById("navSafety-Link");
var navFindYourStyle_Link = document.getElementById("navFindYourStyle-Link");
var navBecomeAStylist_Link = document.getElementById("navBecomeAStylist-Link");
var navLogIn_Link = document.getElementById("navLogIn-Link");

function init() {
    hideAll();
    show_navHome_Link();

    var navHome = document.getElementById("navHome");
    navHome.onclick = show_navHome_Link;

    var navSafety = document.getElementById("navSafety");
    navSafety.onclick = show_navSafety_Link;

    var navFindYourStyle = document.getElementById("navFindYourStyle");
    navFindYourStyle.onclick = show_navFindYourStyle_Link;

    var navBecomeAStylist = document.getElementById("navBecomeAStylist");
    navBecomeAStylist.onclick = show_navBecomeAStylist_Link;

    var navLogIn = document.getElementById("navLogIn");
    navLogIn.onclick = show_navLogIn_Link;
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

function show_navHome_Link() {
    hideAll();
    navHome_Link.setAttribute("class", "visible");
}

function show_navSafety_Link() {
    hideAll();
    navSafety_Link.setAttribute("class", "visible");
}

function show_navFindYourStyle_Link() {
    hideAll();
    navFindYourStyle_Link.setAttribute("class", "visible");
}

function show_navBecomeAStylist_Link() {
    hideAll();
    navBecomeAStylist_Link.setAttribute("class", "visible");
}

function show_navLogIn_Link() {
    hideAll();
    navLogIn_Link.setAttribute("class", "visible");
}

window.onload = init;