$( document ).ready(function() {
    var idnum = 0;


    console.log( "ready! 456" );
    console.log("Chck saved item in storage :::: ");



    // var prediction = localStorage.getItem("resp");
    // console.log(prediction)

    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/recommendations/',
        success: function () {

            // cocktails.forEach(function (co)
            //  {
            // idnum = co.pk;
            // html = '<div class="card" style="width:20rem;"><img id="testcard'+idnum.toString()+'" class="card-img-top"  alt="Card image cap"><div class="card-block"> <h4 class="card-title display-4" id="title'+idnum.toString()+'">Analyzing...</h4> <p class="card-text" id="content'+idnum+'">content.</p> </div> </div>'

            // console.log("Media url is:  ", MEDIA_URL);
            // fields = co.fields;
            // console.log(fields.image)
            //
            // console.log(fields);
            var highest_probility = JSON.parse(localStorage.getItem("resp"));
            highest_probility = highest_probility[0];
            console.log(highest_probility);
            console.log("Detailed Resonse: ", JSON.parse(localStorage.getItem("resp"))[1]);

            $('#ctcards').append(highest_probility);
            // $('#title').value(highest_probility);
             //
            $('#content').html("Show adds please");
            // $('#testcard'+idnum).attr("src", MEDIA_URL+fields.image.slice(2));
            //     // idnum +=1
            //

        }
    })

});
