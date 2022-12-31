var btn = document.querySelector(".sai");
var getText = document.querySelector(".getText");
var content = document.querySelector(".getcontent");
var editorContent = document.querySelector(".editor");

btn.addEventListener("click", function() {
  var s = editorContent.innerHTML;
  content.style.display = "block";
  content.textContent = s;
});

getText.addEventListener("click", function() {
  const old = editorContent.textContent;
  content.style.display = "block";
  content.textContent = old;
});
function bold() {
    document.execCommand('bold');
}
function italic() {
    document.execCommand('italic');
}
function underline() {
    document.execCommand('underline');
}
function link() {
    var url = prompt("Enter the URL");
    document.execCommand("createLink", false, url);
}
function copy() {
    document.execCommand("copy", false, "");
}
function cut(){
    document.execCommand('cut',false,'');
}
function undo(){
    document.execCommand('undo',false,'');
}
function redo(){
    document.execCommand('redo',false,'');
}
function strikeThrough(){
    document.execCommand('strikeThrough',false,'')
}
function Delete(){
    document.execCommand('delete',false,'')
}
function justifyCenter(){
    document.execCommand('justifyCenter',false,'')
}
function justifyLeft(){
    document.execCommand('justifyLeft',false,'')
}
function justifyRight(){
    document.execCommand('justifyRight',false,'')
}
function justifyFull(){
    document.execCommand('justifyFull',false,'')
}
function insertOrderedList(){
    document.execCommand('insertOrderedList',false,'')
}
function insertOrderedList(){
    document.execCommand('insertOrderedList',false,'')
}
function changeColor() {
  var color = prompt("Enter your color in hex ex:#f1f233");
  document.execCommand("foreColor", false, color);
}


function getImage() {
  var file = document.querySelector("input[type=file]").files[0];

  var reader = new FileReader();

  let dataURI;

  reader.addEventListener(
    "load",
    function() {
      dataURI = reader.result;

      const img = document.createElement("img");
      img.src = dataURI;
      editorContent.appendChild(img);
    },
    false
  );

  if (file) {
    console.log("s");
    reader.readAsDataURL(file);
  }
}

function getWYSIWYG(){
    document.querySelector('[name="content"]').value = document.getElementById('editor').innerHTML;
}
