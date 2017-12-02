const $ = require('jquery');
const crypto = require('crypto-browserify');

const primeLength = 2048;
const diffHell = crypto.createDiffieHellman(primeLength);
diffHell.generateKeys('base64');

const newParagraph = $("<p>" + diffHell.getPublicKey('base64') + "</p>");
$("div#content").append(newParagraph);
