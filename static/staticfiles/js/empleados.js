function filtrarEmpleados() {
    var input = document.getElementById("busqueda");
    var filtro = input.value.toLowerCase();
    
    var tabla = document.getElementById("tablaEmpleados");
    var filas = tabla.getElementsByTagName("tr");

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
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.btn-borrar').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();  
            const form = this.closest('form');

            Swal.fire({
                title: "¿Confirma la eliminación del usuario?",
                text: "Esta acción no se puede deshacer.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    form.submit(); 
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            });
        });
    });
});
function modal_editar(url){
    var $=jQuery.noConflict();
    $('#edicion').load(url, function(){
        $(this).modal('show');
    });
}
function modal_agregar(url){
    var $=jQuery.noConflict();
    $('#agregar').load(url,function(){
        $(this).modal('show');
    });
}