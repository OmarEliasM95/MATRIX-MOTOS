document.addEventListener("DOMContentLoaded", function() {
    const cerrarSesionBtn = document.querySelector('#cerrar-sesion-btn');
    const cerrarCajaBtn = document.querySelector('#btn-cerrar');

    if (cerrarSesionBtn) {
        cerrarSesionBtn.addEventListener('click', function(event) {
            event.preventDefault(); 
            Swal.fire({
                title: "¿Confirma cerrar la sesión en este momento?",
                text: "Se redirigirá al login",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Confirmar",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    document.getElementById('logout-form').submit();
                },
                allowOutsideClick: false,
                allowEscapeKey: false,
            });
        });
    }
    if (cerrarCajaBtn) {
        cerrarCajaBtn.addEventListener('click', function(event) {
            event.preventDefault(); 
            Swal.fire({
                title: "SE ENCUENTRA UNA CAJA ABIERTA",
                text: "Se recomienda cerrar la caja antes de cerrar sesión.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Cerrar sesión",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.isConfirmed) {
                    document.getElementById('logout-form').submit();
                } else {
                    window.location.href = '/menu/';
                }
            });
        });
    }
});
