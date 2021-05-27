//load Transaction

function loadDoc(){
    const dbRef = firebase.database().ref();
    dbRef.child("RainProject").child("sensor").get().then((snapshot) => {
        if (snapshot.exists()) {
        
        let content =``;
        let i =1;
          for(item in snapshot.val())
          {
            
                content += `<tr>
                            <td> ${i}  </td>
                            <td>${item}</td>
                            <td>${snapshot.val()[item].value}</td>
                            <td>${snapshot.val()[item].published_at}</td>
                        </tr>`;
                    i++;
            $("#content").html(content);
            }

            // Data for the Temperature
            $("#tempContent").html(snapshot.val()["temperature"].value);
            // Data for Humidity
            $("#humidContent").html(snapshot.val()["humidity"].value);
            // Data for Clothes hanging status
            if(snapshot.val()["clothesHangingStatus"].value == true){
              $("#clothesStatusContent").html("Clothes hanged");
            } else {
              $("#clothesStatusContent").html("No clothes hanged");
            }
            // Data for Raining status
            if(snapshot.val()["rainingStatus"].value == true){
              $("#rainStatusContent").html("Raining");
            } else {
              $("#rainStatusContent").html("Not Raining");
            }
            
          } 
        })
      }
      loadDoc();
      var intervalId = window.setInterval(function(){
        loadDoc();
      }, 1000);

//change system status
var switchStatus = false;
$(".checkSystem").on('change', function() {
    if ($(this).is(':checked')) {
        switchStatus = $(this).is(':checked');
        $("h3").css("color","#41a329");
        console.log(1);
        firebase.database().ref('ControlValues/').update({
          systemStatus:"online",
      });
    }
    else {
       switchStatus = $(this).is(':checked'); 
       $("h3").css("color","#ccc");
       console.log(2);
       firebase.database().ref('ControlValues/').update({
        systemStatus:"offline",
    });
    }
});