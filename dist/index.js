"use strict";
console.log(23);
document.cookie = "user={name:Ken,gender:mike};expire=2h;secure=true;HttpOnly=true";
console.log(document.cookie.split(/[{}]/));
const person = {
    name: "Mike",
    gender: "male"
};
class Person {
    constructor(age, gender) {
        this.age = age;
        this.gender = gender;
    }
}
