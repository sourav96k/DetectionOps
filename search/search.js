const searchInput = document.getElementById("search");


searchInput.addEventListener("keyup", function(){

let value = searchInput.value.toLowerCase();


let cards = document.querySelectorAll(".card,.article");


cards.forEach(card=>{


let text = card.innerText.toLowerCase();


if(text.includes(value)){

card.style.display="block";

}

else{

card.style.display="none";

}


});


});
