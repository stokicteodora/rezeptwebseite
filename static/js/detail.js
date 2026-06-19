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
  const stars = document.querySelectorAll(".detail-stars .fa-star");
  const recipeId = heart.dataset.recipeId;
  const key = `heart-${recipeId}`;
  const saved = parseInt(localStorage.getItem(`stars-${recipeId}`)) || 0;

  if (localStorage.getItem(key) === "true") {
    heart.classList.add("active");
  }

  stars.forEach((s, j) => s.classList.toggle("active", j < saved));

  heart.addEventListener("click", () => {
    heart.classList.toggle("active");
    localStorage.setItem(key, heart.classList.contains("active"));
  });

  stars.forEach((star, i) => {
    star.addEventListener("click", () => {
      stars.forEach((s, j) => s.classList.toggle("active", j <= i));
      localStorage.setItem(`stars-${recipeId}`, i + 1);
    });
  });
});
