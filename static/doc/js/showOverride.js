
$(document).ready(function(){
  var overridables = $(".overridable")
  overridables.each((i, elem) => {
    check_override(elem)
  })
});

function check_override(elem){
  var def = elem.querySelector('.default')
  var override = elem.querySelector('.override')
  var overridden = false
  override.childNodes.forEach((n) => {
    if (n.tagName === "DIV" && !(n.classList.contains("cms-placeholder"))){
      overridden = true
    }
  })
  if (overridden) {
    override.classList.remove("hidden")
  } else {
    def.classList.remove("hidden")
  }
}