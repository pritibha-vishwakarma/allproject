let userscore=0;
let compscore=0;


const userScorePara=document.querySelector("#user-score");
const compScorePara=document.querySelector("#comp-score");

const choice=document.querySelectorAll(".choice");
 const msg=document. querySelector("#msg");
const genCompChoice=()=>{
    const options=["rock", "paper", "scissors"];
    const randIdx=Math.floor(Math.random()*3);
    return options[randIdx];
}
const drawgame=()=>{
    console.log("game was draw");
     msg.innerText="@ draw game"
}
const showwinner=(userwin, userchoice, compChoice)=>{
    if (userwin){
        userscore++;
         userScorePara.innerText=userscore;
        console.log("user win");
        msg.innerText=`🎉 you win! your ${userchoice} beats ${compChoice}`
        msg.style.backgroundColor="green"
    }else{
       compscore++;
        compScorePara.innerText=compscore;
        msg.innerText=`😢 you lose ${compscore} beats your ${userchoice}`
         msg.style.backgroundColor="orange"
    }
}

const playGame = (userchoice) => {
    // console.log("User choice:", userchoice);
    const compChoice = genCompChoice();
    // console.log("Comp choice =", compChoice);

    if (userchoice === compChoice) {
        drawgame();
    } else {
        let userwin = true;

        if (userchoice === "rock") {
            userwin = compChoice === "paper" ? false : true;
        } else if (userchoice === "paper") {
            userwin = compChoice === "scissors" ? false : true;
        } else if (userchoice === "scissors") {
            userwin = compChoice === "rock" ? false : true;
        }

        showwinner(userwin, userchoice, compChoice);
    }
};


choice.forEach((choice)=>{
    
    choice.addEventListener("click", ()=>{
    const userchoice=choice.getAttribute("id");
    playGame(userchoice);
    // console.log("choice was clicked", userchoice);
    

    });
});