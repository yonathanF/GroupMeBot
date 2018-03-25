// <span class="event"></span><span class="event"></span></td>
//<span class="event event-multiday"></span><span class="event event-multiday-start eventclass" style="background-color:#5a9ab2;"></span><span class="event"></td>

var modal = document.getElementById("myModal")
var span = document.getElementsByClassName("close")[0];
var days = document.getElementsByClassName("day");

for (i = 0; i < days.length; i++){
  days[i].onclick = function() {
    modal.style.display = "block";
  }
}


span.onclick = function(){
  modal.style.display = "none";
}


window.onclick = function(event) {
  if (event.target == modal){
    modal.style.display = "none";
  }
}

function writeSched(sentence){
  tex.style.fontFamily = "Courier";
  tex.style.fontSize = "18pt";
  document.getElementById("tex").innerHTML = sentence;
  return sentence;
}

writeSched("HEfklj");

var today = new Date();
var d = today.getDate();
var num = document.getElementsByClassName("number")

function currentDate(d){
  for (i = 0; num.length; i++){
     if (num[i].innerHTML == d){
       days[i].className = "day today";
     }
  }
}

currentDate(d);
