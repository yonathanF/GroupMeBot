// class Current {
//   constructor(day, month, year){
//     this.day = day;
//     this.month = month;
//     this.year = year;
//   }
//
//   get getDay(){
//     return this.day;
//   }
//
//   set setDay(val){
//     this.day = val;
//     return this.day;
//   }
//
//   get getMonth(){
//     return this.month;
//   }
//
//   set setMonth(val){
//     this.month = val;
//     return this.month;
//   }
//
//   get getYear(){
//     return this.year;
//   }
//
//   set setYear(val){
//     this.year = val;
//     return this.year;
//   }
// }
window.onload = function(){
  var today = new Date();
  var d = today.getDate();
  var m = today.getMonth()+1;
  var y = today.getFullYear();

  if (d < 10){
    d = "0" + d;
  }

  if (m < 10){
    m = "0" + m;
  }

  today = m + "/" + d + "/" +y;
  document.write(today);
  document.getElementById("container").innerHTML = today;
}
