const navButtons = document.querySelectorAll(".disc-btn");

navButtons.forEach(button => {button.addEventListener("click", function () {
    let url = `quizzpp/${button.textContent.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, "")}`;
    window.location.href = url;
    })
});
