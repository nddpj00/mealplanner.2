function randomRecipe(getRandomRecipe) {
    console.log("hello")
    var randomRecipeOutput = getRandomRecipe[Math.floor(Math.random() * getRandomRecipe.length)];
    document.getElementById('vegModalHeader').value = randomRecipeOutput;
}