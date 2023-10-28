function updateImage(name) {
    if(name.localeCompare("union") == 0) {
        document.getElementById("image").src = "images/union.jpg"
    } else if (name.localeCompare("thompson") == 0) {
        document.getElementById("image").src = "images/thompson.png"
    } else if(name.localeCompare("rpac") == 0) {
        document.getElementById("image").src = "images/rpac.jpg"
    }
}

function updateStartBox(input) {
    document.getElementById("from").value = input
}

function updateDestinationBox(input) {
    document.getElementById("to").value = input
}