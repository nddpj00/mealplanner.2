// when random recipe modal is closed this reloads page to allow another random selection

let buttons = document.querySelectorAll(".pageRefresh");

for(let i = 0; i < buttons.length; i++){
buttons[i].addEventListener('click', function() {
    location.reload();
});
}