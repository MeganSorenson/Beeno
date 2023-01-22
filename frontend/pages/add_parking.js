
function handleAddParking() {
    console.log("test");

    let lon = document.getElementById("longitude").value;
    let lat = document.getElementById("latitude").value;
    let address = document.getElementById("address").value;
    let city = document.getElementById("city").value;
    let country = document.getElementById("country").value;
    let description = document.getElementById("description").value;
    let price = document.getElementById("price").value;
    let image_url = document.getElementById("image_url").value;
    let user_id = getCookie("user_id");

    let url = 'http://127.0.0.1:1999/park';
    let data = {
        "lon": lon,
        "lat": lat,
        "address": address,
        "city": city,
        "country": country,
        "description": description,
        "price": price,
        "user_id": user_id,
        "image_url": image_url
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
            if (json.status == "success") {
                location.reload();
            }
            console.log("llalala");

        })
        .catch(error => {
            console.log(error);
        });
}


$(document).ready(function () {
    console.log("ready!");
    let id = getCookie("user_id")

    fetch(`http://127.0.0.1:1999/park?type=user&user_id=${id}`)
        .then(response => {
            return response.json();
        })
        .then(json => {
            console.log(json);
            let container = document.getElementById("my_parking_stalls");
            for (const parking_id in json) {
                let tr = document.createElement("tr");

                let lonTd = document.createElement("td");
                lonTd.innerText = json[parking_id].lon
                tr.appendChild(lonTd);

                let latTd = document.createElement("td");
                latTd.innerText = json[parking_id].lat
                tr.appendChild(latTd);

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
                priceTd.innerText = json[parking_id].price
                tr.appendChild(priceTd);

                container.appendChild(tr);
            }
        })
        .catch(error => {
            console.log(error);
        });

});
