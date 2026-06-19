const deletebutton = document.getElementById("delete-button");

if (deletebutton) {
  deletebutton.addEventListener("click", function (e) {
    e.preventDefault();

    if (confirm("Möchtest du dieses Rezept wirklich löschen?")) {
      document.getElementById("delete-form").submit();
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const heart = document.getElementById("heart-button");
  const recipeId = heart.dataset.recipeId;
  const key = `heart-${recipeId}`;

  if (localStorage.getItem(key) === "true") {
    heart.classList.add("active");
  }

  heart.addEventListener("click", () => {
    heart.classList.toggle("active");
    localStorage.setItem(key, heart.classList.contains("active"));
  });
});
