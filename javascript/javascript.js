
// console.log('Hello, World!');

// let a=5;
// let b=2;

// console.log("a =", a, "& b=", b);
// console.log("a+b=", a+b);
// console.log("a-b=",a-b);
// console.log("a*b ", a*b);
// console.log("a/b=",a/b);
// console.log("a%b=",a%b);
// //unary operator
// a--;
// a++;
// console.log("a=",a);

// let a=5;
// let b=2;

// a+=b;
// console.log("a=",a);



// let age=16;
// if (age >= 18){
//     console.log("You are eligible for voting");
// }
// if (age<18){
//     console.log("you can't vote");
    
// }


// let num=10;
// if(num%7==0){
//     console.log("Even number");
// }else{
//     console.log("odd number");
    
// }


// let mode="blue";
// let color;

// if(mode==="dark"){
//     color="black";
// }else if(mode==="blue"){
//     color="blue";
// }else if(mode==="pink"){
//     color="pink";
// }else{
//     color="white";
// }
// console.log("color=",color);



// let age=18;
// let result=age>=18 ? "adult": "not adult";
// console.log(result);


// let name=prompt("Hello, World!");
// console.log(name);



// let score=prompt("Enter your score");
// if(score>=90 && score<=100){
//     console.log("Grade A");
// }else if (score>=70 && score <=89){
//     console.log("Grade B");
// }else if(score>=60 && score<=69){
//     console.log("Grade C"); 
// }
// else if(score>=50 && score<=59){
//     console.log("Grade D");
// }else{
//     console.log("Fail");
// }




// for (let count =1; count <= 100000; count++){
//     console.log("pratibha vishwakarma");
// }
// console.log("loop has endede");


// for (let i=1; i>=0; i++){
//     console.log("i= ", i);




// function countvouwels(str){
//     let count=0
//     for (const char of str){
//         console.log(char);
//         if(char==="a"|| char==="e" || char==="i" || char==="o" || char==="u"){
//             count++;
//         }
//       }
//       console.log(count);
      
// }


// let n=prompt("enter a number");
// let arr=[];
//  for (let i=1; i<=n; i++){
//     arr[i-1]=i;
//  }
//  console.log(arr);
// let sum=arr.reduce((res, curr)=>{
//    return res+curr;
// }) ;
// console.log(sum);

// console.dir(document.body.childNodes[1]);

// console.log(document.body.childNodes[1]);


// let heading=document.getElementsByClassName("heading");
// console.dir(heading);
// console.log(heading);

// let parahs=document.getElementsByTagName("p");
// console.dir(parahs);
// console.log(parahs);

// let element=document.querySelector("p");
// console.dir(element);


// let allelement=document.querySelectorAll("p");
// console.dir(allf felement);


// let newBtn=document.createElement("button");
// newBtn.innerText="Click Me!";

// newBtn.style.color="white";
// newBtn.style.backgroundColor="pink";
// document.querySelector("body").prepend(newBtn);




let btn1=document.querySelector("#btn1");

btn1.onclick=()=>{
    console.log("btn1 was clicked");
    let a=25;
    a++;
    console.log(a);
    
}

let div=document.querySelector("div");
div.onmouseover=() =>{
    console.log("you are inside div");
    
};

btn1.addEventListener("click", ()=>{
    console.log("button was clicked");
    
})
    
btn1.addEventListener("click",(ev)=>{
     console.log("");
     
})