/**
 * Created by Adam on 3/24/2017.
 */

$(".show-menu").click(function () {

    console.log($(this).attr('name'));


    // var div = document.getElementById('menu-option');
    // while (div.firstChild) {
    //     div.removeChild(div.firstChild);
    // }


    $.ajax({
        url: $(this).attr('name'), // returns "[1,2,3,4,5,6]"
        dataType: 'json', // jQuery will parse the response as JSON
        success: function (outputfromserver) {
            // outputfromserver is an array in this case
            // just access it like one

            console.log(outputfromserver[1].name); // alert the 0th value

            for (var i = 0; i < outputfromserver.length; i++) {
                $( ".menu-option:nth-child(1)" ).append( "shit" );
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


