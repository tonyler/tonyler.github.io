function runScript() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "script.py");
  xhr.onload = function() {
    if (xhr.status === 200) {
      document.getElementById("output").innerHTML = xhr.responseText;
    }
  };
  xhr.send();
}
