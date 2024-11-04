// Get the button:
let top_div = document.getElementById("floating-menu");
let toolbar = document.getElementsByClassName("cms-toolbar");

document.getElementById("scroll_to_top_btn").onclick(function (e) {topFunction(e)});
window.addEventListener("scroll", scrollFunction)

function scrollFunction() {
  if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
    let pos = -20
    if (toolbar.length > 0){
      pos += toolbar[0].offsetHeight
      console.log(pos)
    }
    top_div.style.top = pos + "px";
  } else {
    top_div.style.top = "-200px";
  }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  return false
}