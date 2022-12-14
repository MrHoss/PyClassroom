const navButtons = document.querySelectorAll(".disc-btn");

navButtons.forEach(button => {button.addEventListener("click", function () {
    let url = `/quizzpp/${button.value}`;
    window.location.href = url;
    })
});
