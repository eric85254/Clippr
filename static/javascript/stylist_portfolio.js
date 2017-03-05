/**
 * Created by Adam on 2/23/2017.
 */

$(function () {
    if ($('.portfolio-image').height() > $('.portfolio-image').width()) {
        $('.portfolio-image').height( '100%' );
    }
    else
        $('.portfolio-image').width( '100%' );
        var padding = (300 - $('.portfolio-image').height())/2;
        console.log(padding);
        $('.portfolio-image').css({'margin-top': padding});;
})

$(".portfolio-image").click(function () {
    $("#popup-image").attr("src", $(this).attr("src"));
    $("#popup-modal").modal("show");
})

$(document).keyup(function (e) {
    if ((e.keyCode == 27) && ($('#popup-modal').hasClass("show"))) $("#popup-modal").modal("hide");
})