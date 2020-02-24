"use strict";
var $foreign = require("./foreign.js");
var Effect_Console = require("../Effect.Console/index.js");
var println = function ($0) {
    return Effect_Console.log($foreign.showAny($0));
};
module.exports = {
    println: println,
    showAny: $foreign.showAny
};
