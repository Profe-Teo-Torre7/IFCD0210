function agregar() {
    let padre = document.getElementById("lista");
    //let padre = document.querySelector("#lista");
    let li = document.createElement("li");
    li.textContent = "Elemento nuevo";
    padre.appendChild(li);
}
function eliminar() {
    let padre = document.getElementById("lista");
    let li = padre.lastChild;
    //console.log(li);
    if (li) { padre.removeChild(li) };
}