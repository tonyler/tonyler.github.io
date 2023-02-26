function runScript() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "script.py");
    xhr.onload = function() {
      if (xhr.status === 200) {
        alert(xhr.responseText);
      }
    };
    xhr.send();
  }
  