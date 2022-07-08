console.log(23);
document.cookie = "user={name:Ken,gender:mike};expire=2h;secure=true;HttpOnly=true"
console.log(document.cookie.split(/[{}]/));

const person = {
    name:"Mike",
    gender:"male"
}

class Person{
    constructor(private age:number,private readonly gender:"male"|'female'|'other'){}
}