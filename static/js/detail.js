// File: detail.js
// Author: Teodora Stokic
// Date: 26.06.2026
// Version: 1.2
// Description: Handles recipe detail interactions including delete confirmation,
// favorite (heart) toggle, star rating storage, and dynamic portion scaling.
//

// Delete: shows a confirm dialog before submitting the hidden delete form
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
  // Restore saved star rating and heart state from localStorage
  const saved = parseInt(localStorage.getItem(`stars-${recipeId}`)) || 0;
  if (localStorage.getItem(key) === "true") {
    heart.classList.add("active");
  }

  stars.forEach((s, j) => s.classList.toggle("active", j < saved));
  // Heart: toggle and save state to localStorage
  heart.addEventListener("click", () => {
    heart.classList.toggle("active");
    localStorage.setItem(key, heart.classList.contains("active"));
  });
  // Stars: highlight up to clicked star and save rating to localStorage
  stars.forEach((star, i) => {
    star.addEventListener("click", () => {
      stars.forEach((s, j) => s.classList.toggle("active", j <= i));
      localStorage.setItem(`stars-${recipeId}`, i + 1);
    });
  });
});

// Portions: scale all ingredient quantities when the input changes
const portionsInput = document.getElementById("portions-input");
const basePortions = parseInt(portionsInput.defaultValue);

portionsInput.addEventListener("input", () => {
  const factor = portionsInput.value / basePortions;
  document.querySelectorAll(".ingredient-quantity").forEach((el) => {
    const base = parseFloat(el.dataset.base);
    if (!isNaN(base)) el.textContent = Math.round(base * factor * 100) / 100;
  });
});
