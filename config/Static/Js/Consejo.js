

function mostrarVentana() {
  document.getElementById("overlay").style.display = "block";
  document.getElementById("popup").style.display = "block";
}

function cerrarVentana() {
  document.getElementById("overlay").style.display = "none";
  document.getElementById("popup").style.display = "none";
}

function enviarComentario() {
  // Aquí puedes agregar lógica para enviar el comentario a tu servidor o hacer lo que necesites
  var comentario = document.getElementById("comentario").value;
  alert("Comentario enviado: " + comentario);

  // Cerramos la ventana emergente después de enviar el comentario
  cerrarVentana();
}