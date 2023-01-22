function getBookings() {
    console.log("test");

    let location = document.getElementById("locations").value;


    let url = 'http://127.0.0.1:1999/user';

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