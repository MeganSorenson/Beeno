$(document).ready(function () {
    console.log("ready!");
    let id = getCookie("user_id")

    fetch(`http://127.0.0.1:1999/park?type=bookings&user_id=${id}`)
        .then(response => {
            return response.json();
        })
        .then(json => {
            console.log(json);
            let container = document.getElementById("list_of_my_parking");
            for (const reservation_id in json) {
                let tr = document.createElement("tr");

                let idTd = document.createElement("td");
                idTd.innerText = reservation_id
                tr.appendChild(idTd);

                let dateTd = document.createElement("td");
                dateTd.innerText = json[reservation_id].date
                tr.appendChild(dateTd);

                let pidTd = document.createElement("td");
                pidTd.innerText = json[reservation_id].parking_id
                tr.appendChild(pidTd);

                container.appendChild(tr);
            }
        })
        .catch(error => {
            console.log(error);
        });

});

