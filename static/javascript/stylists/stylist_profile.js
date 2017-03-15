/**
 * Created by Adam on 3/8/2017.
 */

$(".menu-option").click(function () {
    var tmp1 = $(this).attr("role");
    // console.log(tmp1);
    $('#' + tmp1).collapse('toggle');
})

$('.portfolio-image').each(function () {
    if ($(this).height() > $(this).width()) {
        $(this).height('100%');
        var left_padding = (220 - $(this).width()) / 2;
        console.log(left_padding);
        $(this).css({'margin-left': left_padding});
    }
    else {
        $(this).width('100%');
        var top_padding = (220 - $(this).height()) / 2;
        console.log(top_padding);
        $(this).css({'margin-top': top_padding});
    }
});

$(".portfolio-image").click(function () {
    $("#popup-image").attr("src", $(this).attr("src"));
    $("#popup-modal").modal("show");
})

$(document).keyup(function (e) {
    if ((e.keyCode == 27) && ($('#popup-modal').hasClass("show"))) $("#popup-modal").modal("hide");
})

$(window).resize(function () {
    console.log('resize called');
    var width = $(window).width();
    if (width <= 575) {
        $('#profile-portfolio').removeClass('show')

        $("#portfolio-header").click(function () {
            $('#profile-portfolio').collapse('toggle');
        })
    }
    else {
        $('#profile-portfolio').addClass('show');
    }
})

    .resize();//trigger the resize event on page load.