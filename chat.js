function getkey() {
    // get first and only file from filelist object
    var reader = new FileReader();

    var password = $("input#username").val();
    var hash = CryptJS.SHA256(password);
    var double_hash = CryptJS.SHA256(hash);
    var encrypted = CryptJS.AES.encrypt("private key", hash);

    alert("double hash: " + double_hash + "\nencrypted private key: " + encrypted);

    // Hide login, reveal chat window
    $("form#login").hide();
    $("div#chat").show();
}

$(document).ready(function() {
    $("button#login").click(getkey);
});
