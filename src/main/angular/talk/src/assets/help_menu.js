function explain_master() {
  var item = document.getElementById("phcb_description");
  var button = document.getElementById("helpbutton");
  if (item.style.display == "none"
    || item.style.display==undefined) {
    item.style.display = "block";
    button.className="back";
  }
  else {
    item.style.display = "none";
    button.className="info";
  }
}

