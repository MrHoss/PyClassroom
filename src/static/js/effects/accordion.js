var accordionItems = document.querySelectorAll(".accordionItem");

accordionItems.forEach(function(item) {
  item.addEventListener("click", toggleAccordion);
});

function toggleAccordion() {
  this.classList.toggle("active");
  var content = this.nextElementSibling;
  if (content.style.maxHeight) {
    // close item
    content.style.maxHeight = null;
  } else {
    // open item
    content.style.maxHeight = "fit-content";
  }
}