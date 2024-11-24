let speechbubble_display_index = 0
let speechbubble_content;

$(document).ready(function(){
    if ($("#vj-speechbubble-content-override") || $("#vj-speechbubble-content")) {
        get_speechbubble_content()
    }
});

function get_speechbubble_content(){
    if ($("#vj-speechbubble-content-override > template").length > 0 || $("#vj-speechbubble-content > template").length > 0){
        setTimeout(function (){
            get_speechbubble_content()
        }, 100)
        return
    }
    let override = $("#vj-speechbubble-content-override > .cms-plugin:not(template)")
    if (override && override.length > 0){
        speechbubble_content = override
    } else {
        speechbubble_content = $("#vj-speechbubble-content > .cms-plugin:not(template)")
    }

    let duration = 10000
    if (typeof ts_message_duration !== 'undefined') {
        duration = (ts_message_duration +2)*1000
    }
    if (speechbubble_content){
        show_speechbubble()
        if (speechbubble_content.length > 1) {
            setInterval(function () {
                next_speechbubble()
            }, duration)
        }
    }
}

function next_speechbubble(){
    speechbubble_display_index += 1;
    if (speechbubble_display_index >= speechbubble_content.length){
        speechbubble_display_index = 0
    }
    $("#vj-speechbubble > .speechbubble").addClass("fade")
    $("#vj-mobile-speechbubble > div > .speechbubble").addClass("fade")
    setTimeout(function (){
        show_speechbubble()
    }, 1000)
}

function show_speechbubble(){
    $("#vj-speechbubble > .speechbubble").html(speechbubble_content[speechbubble_display_index]).removeClass("fade");
    $("#vj-mobile-speechbubble >  div > .speechbubble").html(speechbubble_content.clone()[speechbubble_display_index]).removeClass("fade");
}