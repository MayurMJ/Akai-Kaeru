
$(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                callbackFunc(data);
            },
        });
    });


});
function callbackFunc(data) {

    var featureList = document.getElementById("attrList");
    $('#attrList li').remove();
    $('#corrFeatures ').empty();

    for (i = 0; i < data.topFeatures.length; i++) {
        var featureListItem = document.createElement("li");
         //create new text node
        var featureListValue = document.createTextNode(data.topFeatures[i]);
        //add text node to li element
        featureListItem.appendChild(featureListValue);
        featureList.appendChild(featureListItem);
    }

    for (j=0; j<data.groupedFeatures.length;j++) {
        var corrDiv = document.getElementById('corrFeatures');
        console.log(data.groupedFeatures);
        $("#corrFeatures").append("<label>Cluster"+(j+1)+"</label> : <br />");

        var temp = 'corrList'+(j+1);
        $("#corrFeatures").append("<ul id="+temp+"></ul>");
        var corrId = document.getElementById('corrList'+(j+1));
        for (k=0; k< data.groupedFeatures[j].length; k++) {
            var featureListItem = document.createElement("li");
             //create new text node
            var featureListValue = document.createTextNode(data.groupedFeatures[j][k]);
            //add text node to li element
            featureListItem.appendChild(featureListValue);
            corrId.appendChild(featureListItem);
        }

    }




}