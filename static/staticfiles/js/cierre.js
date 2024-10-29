const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    return Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon,
        confirmButtonText: confirmButtonText,
    });
};
document.getElementById('cierre').addEventListener('submit', function(event) {
    event.preventDefault();
        notificacionSwal('Caja cerrada', 'Con éxito', 'success', 'Ok!').then((result) => {
        if (result.isConfirmed) {
            document.getElementById('cierre').submit();
        }
    });
});
