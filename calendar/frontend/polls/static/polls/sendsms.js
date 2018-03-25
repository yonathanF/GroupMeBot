// var val = document.getElementById("tex").innerHTML;
// var btnc = document.getElementById("btncl");

function sendMessage(){
  const client = require('twilio')(accountSid, authToken);
  const accountSid = "AC68cadd7f2e0281e30db66d8fc7b7695d";
  const authToken = "693889b52a7de73338ed51acbf1ac96e";
  const numbers = ['+17034156746', '+17208082422'];
  const multiSid = "MG76f8feb0f0545f0838c14863f779134a";
  Promise.all(
    numbers.map(number => {
      return client.messages.create({
        to: number,
        from: "MG76f8feb0f0545f0838c14863f779134a",
        body: "hello"
      });
    })
  )
  .then((message) => console.log("Messages Sent!"));
}
