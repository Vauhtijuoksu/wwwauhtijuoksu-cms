let current = 1;

$( document ).ready(function() {
    update()
    $( "#prev" ).click(function() {
        current -= 1;
        update()
    });
    $( "#next" ).click(function() {
        current += 1;
        update()
    });
    $( ".incentive_button" ).click(function() {
        $(this).parent().find(".incentive_expand").toggleClass("hide");
        $(this).parent().find(".dropdown_arrow").toggleClass("rotate");
        $(this).toggleClass("pink");
    });
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


function update_choices() {
    var choices = []
    $(".incentive_field").prop("disabled", false);
    $('.incentive_choices').each(function (index) {
        if ($(this).is(':checked')) {
            if ($(this).val() == "choice" ) {
                var value = $(this).attr('id').split("_")
                if (value.length === 2){
                    choices.push({
                        id: value[0],
                        choice: null
                    })
                } else if (value.length === 3){
                    choices.push({
                        id: value[0],
                        choice: value[1]
                    })
                }
            }
            if ($(this).val() == "field" ) {
                var field = "#" + $(this).attr('id').split("_")[0] + "_" + $(this).attr('id').split("_")[1]  + "_field";
                var value = $(field).attr('id').split("_")
                if (value.length === 3){
                    choices.push({
                        id: value[0],
                        choice: $(field).val()
                    })
                }
                $(field).prop("disabled", true);
            }
        }

    });
    $("#generator").val(JSON.stringify(choices))
    $("#incentivecount").text(choices.length)
    if (choices.length > 0){
        $('.generate').show()
        if (choices.length > 1){
            $('.multiincentive').show()
        }
        else {
            $('.multiincentive').hide()
        }
    }
    else {
        $('.generate').hide()
        $('.multiincentive').hide()
    }
    console.log(choices)
}


function update() {
    $(".play").hide();
    $("#play_" + current).show();
}