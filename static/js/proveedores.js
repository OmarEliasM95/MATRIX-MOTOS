function filtrarProveedores() {
    const input = document.getElementById("busqueda");
    const filtro = input.value.toLowerCase();
    const tabla = document.getElementById("tablaProveedores");
    const filas = tabla.getElementsByTagName("tr");

    for (let i = 1; i < filas.length; i++) {
        const celdas = filas[i].getElementsByTagName("td");
        let coincide = false;

        for (let j = 0; j < celdas.length; j++) {
            if (celdas[j]) {
                const texto = celdas[j].textContent || celdas[j].innerText;
                if (texto.toLowerCase().indexOf(filtro) > -1) {
                    coincide = true;
                    break;
                }
            }
        }
        filas[i].style.display = coincide ? "" : "none";
    }
}
function modal_editar(url) {
    const $ = jQuery.noConflict();
    $('#edicion_prov').load(url, function () {
        $(this).modal('show');
    });
}
