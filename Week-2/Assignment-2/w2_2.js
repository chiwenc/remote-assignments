const welcomeBlock = document.querySelector("#welcome");
const buttonCTA = document.querySelector(".call_to_action");


welcomeBlock.addEventListener('click', () => {
    if (welcomeBlock.textContent === "Welcome Message") {
        welcomeBlock.textContent = "Have a Good Time!";
    } else {
        welcomeBlock.textContent = "Welcome Message";
    };
});

buttonCTA.addEventListener('click', () => {
    const container3 = document.querySelector(".container3");
    
    if (container3.style.display === "none") {
        container3.style.display = "grid";
    } else {
        container3.style.display = "none";
    }
});