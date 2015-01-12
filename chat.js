function getkey() {
    // get first and only file from filelist object
    var reader = new FileReader();

    // Hide login, reveal chat window
    $("form#login").hide();
    $("div#chat").show();
}

$(document).ready(function() {
    $("input#keyfile").change(getkey);
});
