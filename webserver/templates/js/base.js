//load Transaction

function loadDoc(){
    const dbRef = firebase.database().ref();
    dbRef.child("RainProject").child("sensor").get().then((snapshot) => {
        console.log(snapshot.val());
        if (snapshot.exists()) {
        
        let content =``;
        let i =1;
          for(item in snapshot.val())
          {
              console.log(snapshot.val()[item].value);
            
                content += `<tr>
                            <td> ${i}  </td>
                            <td>${item}</td>
                            <td>${snapshot.val()[item].value}</td>
                            <td>${snapshot.val()[item].published_at}</td>
                        </tr>`;
                    i++;
            $("#content").html(content);
            }
            $("#tempContent").html(snapshot.val()["temperature"].value);
            $("#humidContent").html(snapshot.val()["humidity"].value);
            $("#clothesStatusContent").html(JSON.stringify(snapshot.val()["clothesHangingStatus"].value));
            $("#rainStatusContent").html(JSON.stringify(snapshot.val()["rainingStatus"].value));
            } 
        })
      }
      loadDoc();
      var intervalId = window.setInterval(function(){
        loadDoc();
      }, 1000);