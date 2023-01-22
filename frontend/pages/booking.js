function getBookings() {
    console.log("test");

    let date = document.getElementById("date").value;
    let place = document.getElementById("locations").value;


    let url = `http://127.0.0.1:1999/park?type=all&place=${place}&date=${date}`;

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

                let imageTd = document.createElement("td");
                let imageImage = document.createElement("img");
                imageImage.setAttribute("src", json[parking_id].image_url)
                imageTd.appendChild(imageImage)
                tr.appendChild(imageTd);

                container.appendChild(tr);
            }
        })
        .catch(error => {
            console.log(error);
        });
}
