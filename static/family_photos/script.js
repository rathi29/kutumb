
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
function on(id) {
  document.getElementById("overlay" + id).style.display = "block";
}

function off() {
  // Close all overlays
  var overlays = document.querySelectorAll("[id^=overlay]");
  overlays.forEach(function(overlay) {
      overlay.style.display = "none";
  });
}

