function loginHandler() {
    //get username element
    let username_element=document.getElementById("username")
    let username = username_element.value
    let password_element=document.getElementById("password")
    let password = password_element.value
    // Here is where I would check if it is a valid login with the api
    if (username == "" || password == "") {
        return;
    }
    let url = "http://localhost:1999/user?username=user1&password=password1"
    fetch(url)
    .then(response => {
        return response.json();
    })
    .then(json => {
        console.log(json);
    })
    .catch(error => {
        console.log(error);
    })
}


// first, clear, then set the logged in cookies
function delete_cookie( name, path, domain ) {
    if( get_cookie( name ) ) {
        document.cookie = name + "=" +
        ((path) ? ";path="+path:"")+
        ((domain)?";domain="+domain:"") +
        ";expires=Thu, 01 Jan 1970 00:00:01 GMT";
    }
}

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


