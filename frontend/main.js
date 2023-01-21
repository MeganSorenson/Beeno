function loginHandler() {
    console.log("HELLo!");
    let testvar = document.getElementById("test-div")
    testvar.innerText="CHANGED!"
    let extraelement = document.createElement("div")
    extraelement.innerText="lalala"
    testvar.appendChild(extraelement)
}

document.cookie = "username=John Doe";

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }