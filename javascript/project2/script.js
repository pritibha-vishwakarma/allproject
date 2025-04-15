let boxes=document.querySelectorAll(".box");
let resetbtn=document.querySelector("#reset-btn");
let newGameBtn=document.querySelector("#new-btn");
let msgContainer=document.querySelector(".msg-container");
let msg=document.querySelector("#msg")
let turn0=true;

const winPatterns=[
    [0,1,2],
    [0,3,6],
    [0,4,8],
    [1,4,7],
    [2,5,8],
    [2,4,6],
    [3,4,5],
    [6,7,8] 
];

const resetGame=()=>{
    true0=true;
  enableBoxes();
  msgContainer.classList.add("hide");
}
boxes.forEach((box) =>{
    box.addEventListener("click", ()=>{
       console.log("box was clicked");
        if(turn0){
            box.innerText="0";
            turn0=false;
        }else{
            box.innerText="X";
            turn0=true;
        }
        box.disabled=true

        checkwinner();
    })
});

const disableBoxes=()=>{
    for(let box of boxes){
       box.disabled =true;
    }
};
const enableBoxes=()=>{
    for(let box of boxes){
        box.innerText="";
        box.disabled =false;
    }
};
const showwinner=(winner)=>  {

    msg.innerText="congratulation winner is (winner)";
    msgContainer.classList.remove("hide");
}
const checkwinner=()=>{ 
    for ( let pattern of winPatterns){
        // console.log(pattern[0], pattern[1], pattern[2]);
        // console.log(
            // boxes[pattern[0]].innerText,
            // boxes[pattern[1]].innerText,
        //     // boxes[pattern[2]].innerText
        // );
        let pos1Val=boxes[pattern[0]].innerText; 
        let pos2Val=boxes[pattern[1]].innerText;
        let pos3Val=boxes[pattern[2]].innerText;

        if(pos1Val !=""&& pos2Val != "" && pos3Val !=""){
            if(pos1Val === pos2Val && pos2Val === pos3Val){
                console.log("winner is", pos1Val);


        showwinner();      
            }
        }
    }
}
newGameBtn.addEventListener("click", resetGame);
resetbtn.addEventListener("click", ()=>{
    msgContainer.classList.add("hide");
    resetGame();
})