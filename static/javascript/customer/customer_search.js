/**
 * Created by Adam on 3/24/2017.
 */

$(".show-menu").click(function () {

    console.log($(this).attr('name'));


    var div = document.getElementById('menu-option');
    while (div.firstChild) {
        div.removeChild(div.firstChild);
    }


    $.ajax({
        url: $(this).attr('name'), // returns "[1,2,3,4,5,6]"
        dataType: 'json', // jQuery will parse the response as JSON
        success: function (outputfromserver) {
            // outputfromserver is an array in this case
            // just access it like one

            for (var j=0; j<outputfromserver.length; j++) {
                $("#menu-start").load("templates/customer/customerReal/search/menu_preview.html");
            }

            for (var i = 1; i < (outputfromserver.length+1); i++) {
                $( "#menu-name:nth-child("+i+")" ).append( outputfromserver[i-1].name );
            }

            // for (var i = 0; i < outputfromserver.length; i++) {
            //     // console.log(outputfromserver[i]) can be used to get each value
            //     var para = document.createElement("p");
            //     var node = document.createTextNode(outputfromserver[i].name);
            //     para.className = i;
            //     para.appendChild(node);
            //     var element = document.getElementById("menu-option");
            //     element.appendChild(para);
            // }
        }


    });


});


