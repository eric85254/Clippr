/**
 * Created by Adam on 2/23/2017.
 */

$('.portfolio-image').each(function () {
    if ($(this).height() > $(this).width()) {
        $(this).height('100%');
        var left_padding = (300 - $(this).width()) / 2;
        console.log(left_padding);
        $(this).css({'margin-left': left_padding});
    }
    else {
        $(this).width('100%');
        var top_padding = (300 - $(this).height()) / 2;
        console.log(top_padding);
        $(this).css({'margin-top': top_padding});
    }
});

$(".portfolio-image").click(function () {
    $("#popup-image").attr("src", $(this).attr("src"));
    $("#popup-modal").modal("show");
});

$(document).keyup(function (e) {
    if ((e.keyCode == 27) && ($('#popup-modal').hasClass("show"))) $("#popup-modal").modal("hide");
});