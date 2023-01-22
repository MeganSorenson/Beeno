function getBookings() {
    console.log("test");

    let date = document.getElementById("date").value;
    let place = document.getElementById("locations").value;


    let url = `http://127.0.0.1:1999/park?type=all&place=${place}&date=${date}`;

    let container = document.getElementById("available_stalls");
    while (container.childNodes.length > 2) {
        container.removeChild(container.lastChild);
    }

    fetch(url)
        .then(response => {
            return response.json();
        })
        .then(json => {
            console.log(json);
            let container = document.getElementById("available_stalls");
            for (const parking_id in json) {
                let tr = document.createElement("tr");

                let latTd = document.createElement("td");
                latTd.innerText = json[parking_id].lat
                tr.appendChild(latTd);

                let lonTd = document.createElement("td");
                lonTd.innerText = json[parking_id].lon
                tr.appendChild(lonTd);

                let addressTd = document.createElement("td");
                addressTd.innerText = json[parking_id].address
                tr.appendChild(addressTd);

                let placeTd = document.createElement("td");
                placeTd.innerText = json[parking_id].place
                tr.appendChild(placeTd);

                let descTd = document.createElement("td");
                descTd.innerText = json[parking_id].description
                tr.appendChild(descTd);

                let priceTd = document.createElement("td");
                let priceText = json[parking_id].price.toString() + "$ CAD";
                priceTd.innerText = priceText
                tr.appendChild(priceTd);

                let bookTd = document.createElement("td")
                let bButton = document.createElement("button");
                bButton.innerText = "Book!"
                bButton.classList.add("card__button");
                bButton.setAttribute("id", parking_id.toString());
                bButton.setAttribute("onclick", "handleBookingButton(this.id)")
                bookTd.appendChild(bButton);
                tr.appendChild(bookTd);

                let imageTd = document.createElement("td");
                let imageImage = document.createElement("img");
                imageImage.setAttribute("src", json[parking_id].image_url);
                imageTd.appendChild(imageImage);
                tr.appendChild(imageTd);



                container.appendChild(tr);
            }
        })
        .catch(error => {
            console.log(error);
        });
}


function handleBookingButton(parking_id_string) {
    console.log("button-booking test");

    let date = document.getElementById("date").value;
    let parking_id = Number(parking_id_string)
    let user_id = getCookie("user_id");

    let url = 'http://127.0.0.1:1999/book';
    let data = {
        "date": date,
        "parking_id": parking_id,
        "user_id": user_id
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
        })
        .catch(error => {
            console.log(error);
        });
}