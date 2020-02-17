"use strict";
var SmallPrelude = require("../SmallPrelude/index.js");
var A = (function () {
    function A() {

    };
    A.value = new A();
    return A;
})();
var B = (function () {
    function B() {

    };
    B.value = new B();
    return B;
})();
var C = (function () {
    function C() {

    };
    C.value = new C();
    return C;
})();

// ADT is abbr for algebraic data types
var ADT1 = (function () {
    function ADT1(value0) {
        this.value0 = value0;
    };
    ADT1.create = function (value0) {
        return new ADT1(value0);
    };
    return ADT1;
})();

// ADT is abbr for algebraic data types
var ADT2 = (function () {
    function ADT2(value0, value1) {
        this.value0 = value0;
        this.value1 = value1;
    };
    ADT2.create = function (value0) {
        return function (value1) {
            return new ADT2(value0, value1);
        };
    };
    return ADT2;
})();

// ADT is abbr for algebraic data types
var ADT3 = (function () {
    function ADT3(value0) {
        this.value0 = value0;
    };
    ADT3.create = function (value0) {
        return new ADT3(value0);
    };
    return ADT3;
})();
var main = SmallPrelude.discard(SmallPrelude.println(A.value))(function () {
    return SmallPrelude.discard(SmallPrelude.println(B.value))(function () {
        return SmallPrelude.discard(SmallPrelude.println(C.value))(function () {
            return SmallPrelude.discard(SmallPrelude.println(new ADT1("this is a string")))(function () {
                return SmallPrelude.discard(SmallPrelude.println(new ADT2(1, 2.0)))(function () {
                    return SmallPrelude.println(new ADT3({
                        x: 22,
                        y: 33
                    }));
                });
            });
        });
    });
});
module.exports = {
    A: A,
    B: B,
    C: C,
    ADT1: ADT1,
    ADT2: ADT2,
    ADT3: ADT3,
    main: main
};
