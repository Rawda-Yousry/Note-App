const nameButton = document.getElementById("nameButton");
const firstName = document.getElementById("firstName");
const displayName = document.getElementById("welcome");

const displayMessage = () => {
  if (firstName.value == "") {
    alert("Empty Text");
  } else {
    displayName.innerHTML = `Welcome ${firstName.value}`;
    localStorage.setItem("firstName", firstName.value);
  }
};

if (localStorage.length != 0) {
  displayName.innerText = `Welcome back, ${localStorage.getItem("firstName")}`;
}
nameButton.addEventListener("click", displayMessage);
