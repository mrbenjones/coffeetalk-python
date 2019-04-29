function explain_master() {
  var item = document.getElementById("phcb_description");
  if (item.style.display == "none"
    || item.style.display==undefined) {
    item.style.display = "block";
  }
  else {
    item.style.display = "none";
  }
}

