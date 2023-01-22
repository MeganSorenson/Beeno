function loginHandler() {
    //get username element
    let username_element = document.getElementById("username")
    let username = username_element.value
    let password_element = document.getElementById("password")
    let password = password_element.value
    // Here is where I would check if it is a valid login with the api
    if (username == "" || password == "") {
        // display error
        return;
    }
    fetch(`http://127.0.0.1:1999/user?username=${username}&password=${password}`)
        .then(response => {
            return response.json();
        })
        .then(json => {
            console.log(json);
            if (json.status == "success") {
                setCookie("logged_in", "true", 10);
                setCookie("user_id", json.user_id, 10);
                window.location.href = "/pages/booking.html"
            } else {
                console.log("login failed")
            }
        })
        .catch(error => {
            console.log(error);
        });
}



