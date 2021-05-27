


//load Transaction
var testStatus;
function loadDoc(){
const dbRef = firebase.database().ref();
dbRef.child("ControlValues").get().then((snapshot) => {
    if (snapshot.exists()) {
        console.log(snapshot.val());
        var switchStatus = false;
    let content =``;
    let i =1;
        for(item in snapshot.val())
        {
            let min=0,max=0;
            if(item=="humidityThreshold")
            {
                min="20";
                max="80";
            }
            else if(item=="rainThreshold"){
                min="0";
                max="1023";
            }
            else if(item == "sonicThreshold"){
                min="0";
                max="50";
            }
            console.log(min,max);
            if(item=="humidityThreshold"||item=="rainThreshold"||item=="sonicThreshold"){
            content += `<tr>
                        <td>${i}  </td>
                        <td>${item}</td>
                        <td><input id="${item}" type="number" min="${min}" max="${max}" value="${snapshot.val()[item]}" disabled></td>
                    </tr>`;
            }
            else if(item=="systemStatus" && snapshot.val()[item]=="online"){
                content += `<tr>
                        <td>${i}  </td>
                        <td>${item}</td>
                        <td>
                        <select id="sysStatus" name="status" disabled>
                        <option value="online">online</option>
                        <option value="offline">offline</option>
                      </select>
                      </td>
                    </tr>`; 
                    switchStatus = true;
            }
            else{
                content += `<tr>
                        <td>${i}  </td>
                        <td>${item}</td>
                        <td>
                        <select id="sysStatus" name="status" disabled>
                        <option value="offline">offline</option>
                        <option value="online">online</option>
                      </select>
                      </td>
                    </tr>`;   
                    switchStatus = false;
            }
            $(".checkSystem").on('change', function() {
                if ($(this).is(':checked')) {
                    switchStatus = $(this).is(':checked');
                    $("h3").css("color","#41a329");
                    firebase.database().ref('ControlValues/').update({
                      systemStatus:"online",
                  });
                }
                else {
                   switchStatus = $(this).is(':checked'); 
                   $("h3").css("color","#ccc");
                   firebase.database().ref('ControlValues/').update({
                    systemStatus:"offline",
                });
                }
            });
                i++;
                  
        $("#content").html(content);
        }
        var slider = document.getElementById("myRange");
        var output = document.getElementById("value");
        output.innerHTML = slider.value;
        slider.oninput = function() {
            output.innerHTML = this.value;
        }      
        } 
    })
    }
loadDoc();


function editThreshold(){
    $("#savebtn").css("display","unset");
    $("#editbtn").css("display","none");
    $("input").prop('disabled', false);
    $("#sysStatus").prop('disabled', false);
}

function saveThresholdChange(){
    $("#editbtn").css("display","unset");
    $("#savebtn").css("display","none");
    $("input").prop('disabled', true);
    $("#sysStatus").prop('disabled', true);
    var inputHumidityThreshold= $("#humidityThreshold").val();
    var inputRainThreshold = $("#rainThreshold").val();
    var inputSonicThreshold =$("#sonicThreshold").val();
    var inputStatus = $("#sysStatus").val();
    firebase.database().ref('ControlValues/').update({
        humidityThreshold:inputHumidityThreshold,
        rainThreshold:inputRainThreshold,
        sonicThreshold:inputSonicThreshold,
        systemStatus:inputStatus,
    });
}
