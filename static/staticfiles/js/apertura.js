const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    return Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon,  //success, warning, error, info 
        confirmButtonText: confirmButtonText,
    });
};
document.getElementById('apertura').addEventListener('submit', function(event) {
    event.preventDefault();
        notificacionSwal('Caja abierta', 'Con éxito', 'success', 'Ok!').then((result) => {
        if (result.isConfirmed) {
            document.getElementById('apertura').submit();
        }
    });
});
