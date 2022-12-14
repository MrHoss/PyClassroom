const navButtons = document.querySelectorAll(".navBtn");
const navButtonsTitle = document.querySelectorAll(".navBtn h3");
const ProfileInfo = document.querySelector("#ProfileInfo");
const retractBtn = document.querySelector("#retractBtn");
const lateralMenu = document.querySelector("#lateral-menu");
//Navigation Buttons controller
navButtons.forEach(button => {button.addEventListener("click", function () {
    let url = `/${button.value}`;
    console.log(url)
    window.location.href = url;
    })
});

//Lateral menu expand/retract
retractBtn.addEventListener("click", function (){
    if (lateralMenu.style.width === "300px"){
        lateralMenu.style.width = "100px";
        ProfileInfo.style.opacity = 0;
        ProfileInfo.style.height = '0px';
        setTimeout(() => {
            ProfileInfo.style.display = 'none';
        },200)
        navButtonsTitle.forEach((title)=>title.style.display = 'none')

    }else{
        lateralMenu.style.width = "300px";
        ProfileInfo.style.display = 'block';
        setTimeout(() => {
            navButtonsTitle.forEach((title)=>title.style.display = 'block')
            ProfileInfo.style.height = '200px';
            ProfileInfo.style.opacity = 100;
            ProfileInfo.style.display = 'block';
        },200)
    }
});