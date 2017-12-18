
$(function() {
    $('#submitBtn').click(function() {
        var obj ={};

        obj['gender'] = $("#genderVal").text()
        obj['age'] = $("#ageVal").text()
        obj['major'] = $("#MajorVal").text()
        obj['race'] = $("#raceVal").text()
        obj['sat'] = $("#SatVal").text()
        obj['income'] = $("#incomeVal").text()
        obj['state'] = $("#stateVal").text()


        console.log(obj);
        $.ajax({
            type: 'POST',
            url: '/attributes',
            data: JSON.stringify(obj),
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                //callbackFunc(data);
            },
        });
    });

    var majorFlag = false;
    var genderFlag = false;
    var raceFlag = false;
    var satFlag = false;
    var incomeFlag = false;
    var ageFlag = false;
    var stateFlag = false;

    $("#majorList a").click(function(e){
        e.preventDefault(); // cancel the link behaviour
        var selText = $(this).text();
        $("#MajorVal").text(selText);
        majorFlag = true;
        checkAllSelected()
    });
    $("#genderList a").click(function(e){
        e.preventDefault(); // cancel the link behaviour
        var selText = $(this).text();
        $("#genderVal").text(selText);
        genderFlag = true;
        checkAllSelected()
    });
    $("#raceList a").click(function(e){
        e.preventDefault(); // cancel the link behaviour
        var selText = $(this).text();
        $("#raceVal").text(selText);
        raceFlag = true;
        checkAllSelected()
    });
    $("#SatList a").click(function(e){
        e.preventDefault(); // cancel the link behaviour
        var selText = $(this).text();
        $("#SatVal").text(selText);
        satFlag = true;
        checkAllSelected()
    });
    $("#incomeList a").click(function(e){
        e.preventDefault(); // cancel the link behaviour
        var selText = $(this).text();
        $("#incomeVal").text(selText);
        incomeFlag = true;
        checkAllSelected()
    });
    $("#ageList a").click(function(e){
        e.preventDefault(); // cancel the link behaviour
        var selText = $(this).text();
        $("#ageVal").text(selText);
        ageFlag = true;
        checkAllSelected()
    });
    $("#stateList a").click(function(e){
        e.preventDefault(); // cancel the link behaviour
        var selText = $(this).text();
        $("#stateVal").text(selText);
        stateFlag = true;
        checkAllSelected()
    });
    function checkAllSelected() {
        if (majorFlag && genderFlag && raceFlag && satFlag && incomeFlag && ageFlag && stateFlag) {
            $('#submitBtn').prop('disabled', false);
        } else {
            $('#submitBtn').prop('disabled', true);
        }
    }
});


//
//
//function callbackFunc(data) {
//
//    var featureList = document.getElementById("attrList");
//    $('#attrList li').remove();
//    $('#corrFeatures ').empty();
//
//    for (i = 0; i < data.topFeatures.length; i++) {
//        var featureListItem = document.createElement("li");
//         //create new text node
//        var featureListValue = document.createTextNode(data.topFeatures[i]);
//        //add text node to li element
//        featureListItem.appendChild(featureListValue);
//        featureList.appendChild(featureListItem);
//    }
//
//    for (j=0; j<data.groupedFeatures.length;j++) {
//        var corrDiv = document.getElementById('corrFeatures');
//        console.log(data.groupedFeatures);
//        $("#corrFeatures").append("<label>Cluster"+(j+1)+"</label> : <br />");
//
//        var temp = 'corrList'+(j+1);
//        $("#corrFeatures").append("<ul id="+temp+"></ul>");
//        var corrId = document.getElementById('corrList'+(j+1));
//        for (k=0; k< data.groupedFeatures[j].length; k++) {
//            var featureListItem = document.createElement("li");
//             //create new text node
//            var featureListValue = document.createTextNode(data.groupedFeatures[j][k]);
//            //add text node to li element
//            featureListItem.appendChild(featureListValue);
//            corrId.appendChild(featureListItem);
//        }
//
//    }




}