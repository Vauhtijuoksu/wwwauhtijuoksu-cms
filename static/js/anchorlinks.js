$(document).ready(function(){
    return
    var anchormenu = $("#cms-vj-plugin-anchor-menu")
    if (anchormenu){
        var floating = $("#floating-menu > .floating-menu").html()
        var links = ""
        $(".anchor-link-tag").each(function () {
            if ($(this).text() !== ""){
                links += '<a href="#' + this.id + '" class="anchor-menu-link">' + $(this).text() + '</a>'
            }
        })
        if (links !== ""){
            anchormenu.html("<div>Tällä sivulla:</div>" + links)
            $("#floating-menu > .floating-menu").html('<div class="menu">' +links + '</div><div>|</div>' + floating)
        }
    }
});
