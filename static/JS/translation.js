// define language reload anchors
var dataReload = document.querySelectorAll("[data-reload]")
// language translations
var language = {
    eng :{
        leaderboard : "Leaderboard"
    },
    am :{
        leaderboard : "ውጤት"
    }
}
if(window.location.hash){
    if(window.location.hash == "#am"){
        leaderoard.textContent = language.am.leaderboard
    }
}
// define language reload on click iteration
document.getElementById("eng").onClick = function(){
    console.log("jfni")
}
document.getElementById("eng").addEventListener("click", function(){
    window.location.hash = "eng"
})