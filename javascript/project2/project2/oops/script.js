// const student={
//     fullName: "pritibha vishwakarma",
//     marks:8.55,
//     printMarks: function(){
//         console.log("marks=", this.marks);
//     },
// };



// const employee={
//     claTax(){
//         console.log("tax is 10%");
        
//     },
// };


// const pratibha={
//     salary: 50000,
// }

// const pratibha1={
//     salary: 50000,
// }

// const pratibha2={
//     salary: 50000,
//     claTax(){
//         console.log("tax is 5%");
//     }
// }

// const pratibha3={
//     salary: 50000,
// }

// const pratibha4={
//     salary: 50000,
// }


// pratibha.__proto__=employee;
// pratibha1.__proto__=employee;
// pratibha2.__proto__=employee;
// pratibha3.__proto__=employee;
// pratibha4.__proto__=employee;


let DATA="Secret information";

class User{
    constructor(name, email){
        this.name=name;
        this.emial=email;
    }
    viewData(){
        console.log("data=", DATA);
        
    }

}
let student1=new User("pratibha", "pratibha@255gmai.com")
let student2=new User("kratika", "kratika@255gmai.com")