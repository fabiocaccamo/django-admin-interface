
function openTab(evt, tabName) {
  var tabcontents, tablinks;
  tabcontents = document.getElementsByClassName("tabbed-changeform-tabcontent");
  for (let tabcontent of tabcontents) {
    tabcontent.classList.remove("active");
  }
  tablinks = document.getElementsByClassName("tabbed-changeform-tablinks");
  for (let tablink of tablinks) {
    tablink.classList.remove("active");
  }
  document.getElementById(tabName).classList.add("active");
  evt.currentTarget.classList.add("active");
}
