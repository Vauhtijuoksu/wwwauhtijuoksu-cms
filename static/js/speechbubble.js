let speechcontentindex = 0
let speechcontents = 0

let height = 0;
$(document).ready(function(){
    var duration = 10000
    var durationdiv = $("#prioritymessageduration")
    speechcontents = $(".prioritymessagecontent").length

    if (durationdiv){
        duration = (parseInt(durationdiv.text())+2) * 1000
    }
    if (speechcontents){
        show_speech()
        if (speechcontents > 1) {
            setInterval(function () {
                next_speech()
            }, duration)
        }
    }
    onscroll = (event) => {get_scroll()}
    set_scroll(0, 0)
});

function get_scroll(){
    let sp = window.scrollY
    let scroll = window.scrollY/($(document).height()-$(window).height())
    set_scroll(scroll, sp)
}

function set_scroll(scroll_ratio, scroll){
    let win_height = $(window).height()
    $(".sidebox").css("margin-top", win_height*(scroll_ratio*0.2 -0.05)+"px")
    let left = 10*Math.sin(scroll*0.0008)
    $(".sidebox > div > img").css("margin-top", win_height*scroll_ratio*0.05+"px").css("margin-left", left+"px").css("margin-right", -left+"px")
    $(".sidebox > div > .speechbubble-positioner").css("margin-left", left*0.5+"px").css("margin-right", -left*0.5+"px")
    $("body").css("background-position-y", Math.round(-scroll*0.02-20)+"px");

}

function next_speech(){
    speechcontentindex += 1;
    if (speechcontentindex >= speechcontents){
        speechcontentindex = 0
    }
    let bubble = $(".speechbubble")
    bubble.addClass("fade")
    setTimeout(function (){
        show_speech()
    }, 1000)
}

function show_speech(){
    let bubble = $(".speechbubble")
    bubble.html($("#prioritymessage_"+speechcontentindex).html())
    bubble.removeClass("fade")
}