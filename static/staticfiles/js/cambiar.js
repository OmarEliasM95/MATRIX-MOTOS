const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    return Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon,  
        confirmButtonText: confirmButtonText,
    });
};
document.addEventListener("DOMContentLoaded", function() {
    const button = document.querySelector('#btn-guardar'); 
    button.addEventListener('click', function(event) {
        event.preventDefault();  
        const form = this.closest('form');
        Swal.fire({
            title: "¿Confirma el cambio de contraseña?",
            text: "",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Cambiar",
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
