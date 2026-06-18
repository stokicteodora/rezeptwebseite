console.log("detail.js geladen");

const deletebutton = document.getElementById("delete-button");
console.log(deletebutton);

if (deletebutton) {
  deletebutton.addEventListener("click", function (e) {
    e.preventDefault();
    console.log("Löschen geklickt");

    if (confirm("Möchtest du dieses Rezept wirklich löschen?")) {
      document.getElementById("delete-form").submit();
    }
  });
}
