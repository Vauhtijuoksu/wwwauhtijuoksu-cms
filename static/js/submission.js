function duplicate_subform_div (event, caller) {
    event.preventDefault()
    event.stopPropagation()

    const form_idx = $("input[id$='TOTAL_FORMS'").val()
    $("#empty-form")
        .before("<div class='row'>" + $("#empty-form").html()
            .replace(/__prefix__/g, form_idx) + "</div>")
    $("input[id$='TOTAL_FORMS'").val(parseInt(form_idx) + 1)
}
