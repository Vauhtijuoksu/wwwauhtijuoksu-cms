// Get the button:

let cms_toolbar_height = 0
let vj_bg_offset_y = Math.floor(-Math.random()*4000)
let vj_bg_offset_x = Math.floor(-Math.random()*4000)

$(document).ready(function() {
    let cms_toolbar = $(".cms-toolbar").first()
    if (cms_toolbar){
        cms_toolbar_height = cms_toolbar.height()
    }
    onscroll = (event) => {
    get_scroll()
    }
    set_scroll(0, 0)
    $("#scroll_to_top_btn").click(function (e){goToTop(e)})

});

function set_scroll_menu(scroll) {
    if (scroll > 500 || scroll > 500) {
        $("#vj-scrolldown-menu").css("top", -20 + cms_toolbar_height + "px")
    } else {
        $("#vj-scrolldown-menu").css("top", "-200px")
    }
}

function goToTop(e=null) {
    e?.preventDefault()
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    return false
}


function get_scroll(){
  let scroll = window.scrollY
  let scroll_ratio = scroll/($(document).height()-$(window).height())
  set_scroll(scroll_ratio, scroll)
  set_scroll_menu(scroll)
}

function set_scroll(scroll_ratio, scroll){
    let win_height = $(window).height()
    $(".viuhti-speech").css("margin-top", win_height*(scroll_ratio*0.2+0.1)+"px")
    let left = 10*Math.sin(scroll*0.0008)
    $(".viuhti-speech > img").css("margin-top", win_height*scroll_ratio*0.04+"px").css("margin-left", left+"px").css("margin-right", -left+"px")
    $(".viuhti-speech > .speechbubble-positioner").css("margin-left", left*0.9+"px").css("margin-right", -left*0.9+"px")
    $(".parallax-background").css("background-position-y", Math.round(-scroll*0.04-vj_bg_offset_y*2)+"px").css("background-position-x", Math.round(scroll*0.004-vj_bg_offset_x*2)+"px");

}
