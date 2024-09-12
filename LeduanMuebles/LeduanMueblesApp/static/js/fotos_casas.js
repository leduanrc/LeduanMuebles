const contenedorFotos = document.querySelector('.contenedor-fotos');
const imagenes = document.querySelectorAll('.contenedor-fotos img');
const modalImagen = document.querySelector('.modal-imagen');
const cerrarModal = document.querySelector('.cerrar-modal');

// Función para mostrar el modal de imagen
const mostrarModal = (e) => {
  modalImagen.style.display = 'flex';
  modalImagen.querySelector('img').src = e.target.src;
}

// Función para cerrar el modal de imagen
const cerrarModalImagen = () => {
  modalImagen.style.display = 'none';
}

// Recorre las imágenes y añade un event listener para mostrar el modal
imagenes.forEach((imagen) => {
  imagen.addEventListener('click', mostrarModal);
});

// Añade un event listener al botón de cierre del modal
cerrarModal.addEventListener('click', cerrarModalImagen);
