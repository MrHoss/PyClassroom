const navButtons = document.querySelectorAll(".navBtn");
const navButtonsTitle = document.querySelectorAll(".navBtn h3");
const ProfileInfo = document.querySelector("#ProfileInfo");
const retractBtn = document.querySelector("#retractBtn");
const lateralMenu = document.querySelector("#lateral-menu");
const menuList = document.querySelector(".menu-list");
//Navigation Buttons controller

navButtons.forEach(button => {button.addEventListener("click", function () {
    let url = '/'
    if(button.value){
        url = `/${button.value}`;
    }
    url = url.replace("%",'/')
    console.log(url)
    window.location.href = url;
    })
});
const addClass = () =>{
    lateralMenu.classList.add("hidden");
    retractBtn.innerHTML = `<i class="btn material-icons">
        menu
    </i>`;
    sessionStorage.setItem('lateralmenu','hidden');
}
const removeClass = () =>{
    lateralMenu.classList.remove("hidden");
    retractBtn.innerHTML = `<i class="btn material-icons">
        chevron_left
    </i>`;
    sessionStorage.removeItem('lateralmenu');
}
sessionStorage.getItem('lateralmenu') === 'hidden' ? addClass(): removeClass()
//Lateral menu expand/retract
retractBtn.addEventListener("click", function (){
    
    if(lateralMenu.classList.contains("hidden")){
        removeClass()
        
    }else{
        addClass()
        
    }
    
});