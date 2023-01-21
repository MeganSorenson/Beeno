function loginHandler() {
    console.log("HELLo!");
    let testvar = document.getElementById("test-div")
    testvar.innerText="CHANGED!"
    let extraelement = document.createElement("div")
    extraelement.innerText="lalala"
    testvar.appendChild(extraelement)
}