const deletebutton = document.getElementById("delete-button");

if (deletebutton) {
  deletebutton.addEventListener("click", function (e) {
    e.preventDefault();

    if (confirm("Möchtest du dieses Rezept wirklich löschen?")) {
      document.getElementById("delete-form").submit();
    }
  });
}
