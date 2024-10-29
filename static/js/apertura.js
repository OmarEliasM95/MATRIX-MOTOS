const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    return Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon,  // success, warning, error, info
        confirmButtonText: confirmButtonText,
    });
};

document.getElementById('apertura').addEventListener('submit', function(event) {
    event.preventDefault();

    const saldoInicial = parseFloat(document.querySelector('input[name="saldo_inicial"]').value);

    if (isNaN(saldoInicial) || saldoInicial < 0) {
        notificacionSwal('Error', 'El saldo inicial no puede ser menor a 0', 'error', 'Aceptar');
    } else {
        notificacionSwal('Caja abierta', 'Con éxito', 'success', 'Ok!').then((result) => {
            if (result.isConfirmed) {
                event.target.submit();  
            }
        });
    }
});
