
$( document ).ready(function() {
    $("#incentive_code_holder").hide()
    $( ".incentive_dropdown" ).click(function() {
        $(this).parent().find(".incentive_expand").slideToggle();
        $(this).parent().find(".dropdown_arrow").toggleClass("rotate");
    });
    update_choices()
    $('.incentive_choices').change(
    function(){
        update_choices()
    });
    $( ".copybtn" ).click(function() {
        copyToClipboard( $($(this).parent()[0]).find(".incentive_code") );
        $(this).text("Koodi kopioitu!");
        $(this).removeClass("copy")
    });

    function copyToClipboard(element) {
        var $temp = $("<textarea>");
        $("body").append($temp);
        $temp.val($(element).text()).select();
        document.execCommand("copy");
        $temp.remove();
    }
});

function get_code() {
    var choices = get_choices()
    console.log(JSON.stringify(choices))
    fetch('https://api.dev.vauhtijuoksu.fi/generate-incentive-code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(choices)
    }).then( response =>
        response.json().then( data =>
            code_get(data)
    ));
    clear_choices()
    $('.generate').slideUp()
    $('.multiincentive').slideUp()
}

function code_get(data){
    $("#incentive_code_holder").slideDown();
    $("#incentive_code").text(data.code)
}


function get_choices() {
    var choices = []
    $(".incentive_field").prop("disabled", false);
    $('.incentive_choices').each(function (index) {
        if ($(this).is(':checked')) {
            if ($(this).val() == "choice" ) {
                var value = $(this).attr('id').split("_")
                if (value.length === 2){
                    choices.push({
                        id: value[0]
                    })
                } else if (value.length === 3){
                    choices.push({
                        id: value[0],
                        parameter: value[1]
                    })
                }
            }
            if ($(this).val() == "field" ) {
                var field = "#" + $(this).attr('id').split("_")[0] + "_" + $(this).attr('id').split("_")[1]  + "_field";
                var value = $(field).attr('id').split("_")
                if (value.length === 3){
                    choices.push({
                        id: value[0],
                        parameter: $(field).val()
                    })
                }
                $(field).prop("disabled", true);
            }
        }

    });
    return choices
}

function clear_choices() {
    $(".incentive_field").prop("disabled", false);
    $('.incentive_choices').each(function (index) {
        if ($(this).is(':checked')) {
            $(this).prop("checked", false);
        }

    });
}

function update_choices() {
    var choices = get_choices()
    $("#incentivecount").text(choices.length)
    if (choices.length > 0){
        $('.generate').slideDown()
        if (choices.length > 1){
            $('.multiincentive').slideDown()
        }
        else {
            $('.multiincentive').slideUp()
        }
    }
    else {
        $('.generate').slideUp()
        $('.multiincentive').slideUp()
    }
    $("#incentive_code_holder").slideUp()
}