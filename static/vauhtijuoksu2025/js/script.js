// Get the button:

let cms_toolbar_height = 0
let vj_bg_offset_y = Math.floor(-Math.random()*4000)
let vj_bg_offset_x = Math.floor(-Math.random()*4000)
let moshtimeout = null
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

    $(".bottomforest").css("background-position-x", Math.round(-vj_bg_offset_x)+"px");
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
    const s = Math.round(scroll*4) % 3
    set_mosh(scroll)
    if (moshtimeout){
        clearTimeout(moshtimeout)
    }
    moshtimeout = setTimeout(set_mosh, 100)

    let win_height = $(window).height()
    $(".viuhti-speech").css("margin-top", win_height*(scroll_ratio*0.2+0.1)+"px")
    let left = 10*Math.sin(scroll*0.0008)
    $(".viuhti-speech > .sideviuhti").css("margin-top", win_height*scroll_ratio*0.03+"px").css("margin-left", left+"px").css("margin-right", -left+"px")
    $(".viuhti-speech > .speechbubble-positioner").css("margin-left", left*0.9+"px").css("margin-right", -left*0.9+"px")
    $("body").css("background-position-y", Math.round(-scroll*0.03-vj_bg_offset_y)+"px").css("background-position-x", Math.round(scroll*0.01-vj_bg_offset_x)+"px");
}
function set_mosh(scroll=0){
    const s = Math.round(scroll*5) % 3
    const mosh = [$(".viuhti-speech > .sideviuhti > .mosh0"), $(".viuhti-speech > .sideviuhti > .mosh1"), $(".viuhti-speech > .sideviuhti > .mosh2")]
    switch (s){
        case 0:
            mosh[0].show()
            mosh[1].hide()
            mosh[2].hide()
            break;
        case 1:
            mosh[1].show()
            mosh[2].hide()
            mosh[0].hide()
            break;
        case 2:
            mosh[2].show()
            mosh[0].hide()
            mosh[1].hide()
            break;
    }
}
