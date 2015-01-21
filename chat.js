function login() {
    // get first and only file from filelist object
    // This is only necessary if we use a keyfile instead of username and password
    var reader = new FileReader();
    // this is not finished

    // Make a bunch of hashes.
    var password = $("input#username").val();
    var hash = CryptoJS.SHA256(password);
    var double_hash = CryptoJS.SHA256(hash);
//    var encrypted = CryptoJS.AES.encrypt("private key", hash);
//    alert("double hash: " + double_hash + "\nencrypted private key: " + encrypted);

    // Hide login, reveal chat window
    $("form#login").fadeOut(1000);
    $("div#chat").fadeIn(1000);
}

$(document).ready(function() {
    $("button#login").click(login);
});
