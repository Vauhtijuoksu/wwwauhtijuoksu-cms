
$(document).ready(function(){
  var initial = localStorage.getItem("darkmodeEnabled")
  if (initial === "true") setDarkmodeEnabled(true)

  $("#darkmode").click(() => {
    setDarkmodeEnabled(true)
  })
  $("#lightmode").click(() => {
    setDarkmodeEnabled(false)
  })

});

function setDarkmodeEnabled(v) {
  var darkmode = $("#darkmode")
  var lightmode = $("#lightmode")
  var page = $("#page")
  if (v) {
    darkmode.addClass("hidden")
    lightmode.removeClass("hidden")
    page.addClass("darkmode")
    localStorage.setItem("darkmodeEnabled", "true")
  } else {
    lightmode.addClass("hidden")
    darkmode.removeClass("hidden")
    page.removeClass("darkmode")
    localStorage.setItem("darkmodeEnabled", "false")
  }
}