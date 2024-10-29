function filtrarEmpleados() {
    let input = document.getElementById('busqueda');
    let filter = input.value.toLowerCase();
    let table = document.getElementById('tablaEmpleados');
    let tr = table.getElementsByTagName('tr');
    
    for (let i = 1; i < tr.length; i++) {
        let td = tr[i].getElementsByTagName('td');
        let visible = false;

        for (let j = 0; j < td.length; j++) {
            if (td[j]) {
                let txtValue = td[j].textContent || td[j].innerText;
                if (txtValue.toLowerCase().indexOf(filter) > -1) {
                    visible = true;
                    break;
                }
            }
        }
        tr[i].style.display = visible ? "" : "none";
    }
}

function modal_agregar(url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById('agregar').innerHTML = data;
            $('#agregar').modal('show');
        })
        .catch(error => console.error('Error:', error));
}

function modal_editar(url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById('edicion').innerHTML = data;
            $('#edicion').modal('show');
        })
        .catch(error => console.error('Error:', error));
}

function modal_clave(url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById('clave').innerHTML = data;
            $('#clave').modal('show');
        })
        .catch(error => console.error('Error:', error));
}

document.querySelectorAll('.btn-borrar').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        let form = this.closest('form');
        
        Swal.fire({
            title: '¿Estás seguro?',
            text: "No podrás deshacer esta acción.",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                form.submit();
            }
        });
    });
});
