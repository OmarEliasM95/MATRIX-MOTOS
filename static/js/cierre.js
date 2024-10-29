const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    return Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon,
        confirmButtonText: confirmButtonText,
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: true
    });
};

document.getElementById('cerrar-form').addEventListener('submit', function (event) {
    event.preventDefault()
    notificacionSwal('Éxito', 'Caja cerrada correctamente', 'success', 'Ok!').then((result) => {
        if (result.isConfirmed) {
            event.target.submit()
        }
    });
});
