/**
 * Created by Adam on 2/23/2017.
 */

$(".portfolio-image").click(function() {
    $("#popup-image").attr("src", $(this).attr("src"));
    $("#popup-modal").modal("show");
})