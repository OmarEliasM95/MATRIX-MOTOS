function filtrarProductos(){
    var input= document.getElementById("busqueda");
    var filtro= input.value.toLowerCase();
    var tabla= document.getElementById("tablaProductos");
    var filas= tabla.getElementsByTagName("tr");

    for (var i = 1; i < filas.length; i++) {
        var celdas = filas[i].getElementsByTagName("td");
        var coincide = false;

        for (var j = 0; j < celdas.length; j++) {
            if (celdas[j]) {
                var texto = celdas[j].textContent || celdas[j].innerText;
                if (texto.toLowerCase().indexOf(filtro) > -1) {
                    coincide = true;
                    break;
                }
            }
        }

        filas[i].style.display = coincide ? "" : "none";
    }
}