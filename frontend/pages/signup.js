function handleSignup() {
    console.log("test");

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let email = document.getElementById("email").value;
    let first_name = document.getElementById("first_name").value;
    let last_name = document.getElementById("last_name").value;
    let phone_number = document.getElementById("phone_number").value;

    let url = 'http://127.0.0.1:1999/user';
    let data = {
        "username": username,
        "password": password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number
    };

    let postData = {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    };

    fetch(url, postData)
        .then(response => {
            return response.json();
        })
        .then(json => {
            console.log(json);
            console.log("llalala");
            window.location.href = "/"
        })
        .catch(error => {
            console.log(error);
        });
}