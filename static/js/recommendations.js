
$( document ).ready(function() {
    var idnum = 0;


    console.log( "ready! 123" );
    console.log("Chck saved item in storage :::: ",JSON.parse(localStorage.getItem("resp")))
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/recommendations/',
        success: function (json) {
            console.log("i AM js  ", JSON.parse(json));
            var cocktails = JSON.parse(json);
            console.log(cocktails);
            cocktails.forEach(function (co) {
                idnum = co.pk;
                html = '<div class="card" style="width:20rem;"><img id="testcard'+idnum.toString()+'" class="card-img-top"  alt="Card image cap"><div class="card-block"> <h4 class="card-title display-4" id="title'+idnum.toString()+'">Analyzing...</h4>  </div> </div>'
                fields = co.fields;
                console.log(fields.image)

                console.log(fields);
                $('#ctcards').append(html);
                $('#title'+ idnum).html(fields.name);
                 //
                $('#content'+idnum).html(fields.directions);
                $('#testcard'+idnum).attr("src", "media_cdn/"+fields.image);
                // idnum +=1

            })
        },
        error: function(error){
            console.log("error : ",error);        }
    })

});
